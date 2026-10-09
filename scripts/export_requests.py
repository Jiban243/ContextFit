import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from transformers import AutoTokenizer
from contextfit.retrieval import BM25Retriever
from contextfit.context_policies import (
    MAX_INPUT_TOKENS,
    POLICIES,
    build_request,
)
from check_evaluation import main as check_evaluation

MODEL_ID = "Qwen/Qwen2.5-1.5B-Instruct"


def read_jsonl(path):
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8-sig").splitlines()
        if line.strip()
    ]


def write_jsonl(path, records):
    text = "".join(
        json.dumps(record, ensure_ascii=False) + "\n"
        for record in records
    )
    path.write_text(text, encoding="utf-8")


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    check_evaluation()

    chunks_path = ROOT / "data/processed/chunks.jsonl"
    retriever = BM25Retriever(chunks_path)
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

    # Build everything before writing any output.
    outputs = {}
    input_hashes = {
        "data/processed/chunks.jsonl": sha256(chunks_path),
    }

    for split in ("dev", "test"):
        gold_path = ROOT / f"data/evaluation/{split}_gold.jsonl"
        questions = read_jsonl(gold_path)
        input_hashes[gold_path.relative_to(ROOT).as_posix()] = sha256(
            gold_path
        )

        requests = []
        diagnostics = []

        for item in questions:
            # Retrieval uses only the question, never the expected answer.
            candidates = retriever.search(item["question"], top_k=10)

            for policy in POLICIES:
                record, info = build_request(
                    question_id=item["question_id"],
                    question=item["question"],
                    candidates=candidates,
                    policy=policy,
                    tokenizer=tokenizer,
                )

                requests.append(record)
                diagnostics.append({
                    **info,
                    "split": split,
                    "candidate_ids": [
                        candidate["chunk_id"] for candidate in candidates
                    ],
                })

        keys = {
            (record["question_id"], record["policy"])
            for record in requests
        }
        expected_count = len(questions) * len(POLICIES)

        if len(requests) != expected_count or len(keys) != expected_count:
            raise ValueError(f"{split}: duplicate or missing requests")

        outputs[split] = (requests, diagnostics)

    # Separate folders preserve previous exports.
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S_%fZ")
    output_dir = ROOT / "data/requests" / f"export_{run_id}"
    output_dir.mkdir(parents=True, exist_ok=False)

    for split, (requests, diagnostics) in outputs.items():
        write_jsonl(output_dir / f"{split}_requests.jsonl", requests)
        write_jsonl(
            output_dir / f"{split}_diagnostics.jsonl", diagnostics
        )

        print(f"\n{split}: {len(requests)} requests")
        for policy in POLICIES:
            rows = [r for r in diagnostics if r["policy"] == policy]
            counts = [r["prompt_tokens"] for r in rows]
            empty = sum(r["selected_count"] == 0 for r in rows)
            print(
                f"  {policy}: {len(rows)} requests | "
                f"prompt tokens {min(counts)}–{max(counts)} | "
                f"empty contexts {empty}"
            )

    source_hashes = {}
    for name in ("retrieval.py", "context_policies.py", "validation.py"):
        path = ROOT / "src/contextfit" / name
        source_hashes[path.relative_to(ROOT).as_posix()] = sha256(path)

    manifest = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "model_id": MODEL_ID,
        "tokenizer_backend_sha256": hashlib.sha256(
            tokenizer.backend_tokenizer.to_str().encode("utf-8")
        ).hexdigest(),
        "chat_template": tokenizer.chat_template,
        "candidate_top_k": 10,
        "policies": list(POLICIES),
        "max_input_tokens": MAX_INPUT_TOKENS,
        "input_sha256": input_hashes,
        "source_sha256": source_hashes,
        "output_sha256": {
            path.name: sha256(path)
            for path in sorted(output_dir.glob("*.jsonl"))
        },
        "annotation_review_status": "not_certified_by_exporter",
    }
    (output_dir / "export_manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print(f"\nSaved to: {output_dir}")
    print("PASS: exported 18 development and 72 test requests.")
    print("Expected answers and gold evidence were excluded from requests.")


if __name__ == "__main__":
    main()