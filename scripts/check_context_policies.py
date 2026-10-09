import json
import sys
from pathlib import Path

from transformers import AutoTokenizer

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from contextfit.retrieval import BM25Retriever
from contextfit.context_policies import POLICIES, build_request


def main():
    tokenizer = AutoTokenizer.from_pretrained(
        "Qwen/Qwen2.5-1.5B-Instruct"
    )
    retriever = BM25Retriever(
        ROOT / "data/processed/chunks.jsonl"
    )

    question = "What does the PYTHONPATH variable do?"
    candidates = retriever.search(question, top_k=10)

    records = []
    diagnostics = []

    for policy in POLICIES:
        record, info = build_request(
            question_id="dev_pythonpath",
            question=question,
            candidates=candidates,
            policy=policy,
            tokenizer=tokenizer,
        )
        records.append(record)
        diagnostics.append(info)

        print(
            f"{policy}: "
            f"{info['selected_count']} chunks | "
            f"{info['context_tokens']} context tokens | "
            f"{info['prompt_tokens']} prompt tokens"
        )
        print("Sources:", ", ".join(record["source_ids"]))

        assert info["prompt_tokens"] <= 4016
        if policy == "budget_900":
            assert info["context_tokens"] <= 900

    # Empty retrieval should remain empty under every policy.
    for policy in POLICIES:
        record, _ = build_request(
            "empty_check", question, [], policy, tokenizer
        )
        assert record["context"] == ""
        assert record["source_ids"] == []

    output_dir = ROOT / "data/requests"
    output_dir.mkdir(parents=True, exist_ok=True)

    with (output_dir / "development_smoke.jsonl").open(
        "w", encoding="utf-8"
    ) as file:
        for record in records:
            file.write(json.dumps(record, ensure_ascii=False) + "\n")

    (output_dir / "development_smoke_diagnostics.json").write_text(
        json.dumps(diagnostics, indent=2),
        encoding="utf-8",
    )

    print("\nPASS: token limits and empty-context handling.")
    print("Saved three development requests.")


if __name__ == "__main__":
    main()