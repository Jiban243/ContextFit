import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_jsonl(path):
    records = []
    with path.open(encoding="utf-8-sig") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(
                    f"{path.name}, line {line_number}: {exc}"
                ) from exc
    return records


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    chunks = read_jsonl(ROOT / "data/processed/chunks.jsonl")
    chunk_ids = {chunk["chunk_id"] for chunk in chunks}
    seen_ids = set()

    for split, expected_count in (("dev", 6), ("test", 24)):
        path = ROOT / f"data/evaluation/{split}_gold.jsonl"
        records = read_jsonl(path)

        require(
            len(records) == expected_count,
            f"{path.name}: expected {expected_count} records, "
            f"found {len(records)}",
        )

        for record in records:
            qid = record.get("question_id")
            require(
                isinstance(qid, str) and qid.strip(),
                f"{path.name}: missing question_id",
            )
            require(qid not in seen_ids, f"Duplicate question_id: {qid}")
            seen_ids.add(qid)

            require(record.get("split") == split, f"{qid}: wrong split")
            require(
                isinstance(record.get("question"), str)
                and record["question"].strip(),
                f"{qid}: missing question",
            )
            require(
                type(record.get("answerable")) is bool,
                f"{qid}: answerable must be true or false",
            )

            groups = record.get("sufficient_evidence_sets")
            require(isinstance(groups, list), f"{qid}: invalid evidence sets")

            if record["answerable"]:
                require(bool(groups), f"{qid}: answerable but no evidence")
                points = record.get("expected_answer_points")
                require(
                    isinstance(points, list)
                    and bool(points)
                    and all(isinstance(p, str) and p.strip() for p in points),
                    f"{qid}: missing or invalid expected answer points",
                )
            else:
                require(groups == [], f"{qid}: unanswerable has gold evidence")

            for group in groups:
                require(
                    isinstance(group, list) and bool(group),
                    f"{qid}: evidence group must be a non-empty list",
                )
                require(
                    all(isinstance(cid, str) for cid in group),
                    f"{qid}: chunk IDs must be strings",
                )
                require(
                    len(group) == len(set(group)),
                    f"{qid}: duplicate chunk ID within evidence group",
                )
                for cid in group:
                    require(cid in chunk_ids, f"{qid}: unknown chunk {cid}")

            category = record.get("category")
            require(
                category in {"direct", "multi", "unanswerable"},
                f"{qid}: invalid category {category!r}",
            )
            if not record["answerable"]:
                require(category == "unanswerable", f"{qid}: wrong category")
            else:
                expected_category = (
                    "direct" if any(len(group) == 1 for group in groups)
                    else "multi"
                )
                require(
                    category == expected_category,
                    f"{qid}: category should be {expected_category}",
                )

        print(f"PASS: {path.name} — {len(records)} records")
        print("Categories:", dict(Counter(r["category"] for r in records)))

    print("\nPASS: JSON structure, unique IDs, and evidence references.")
    print("Answer correctness and human review are not checked by this script.")


if __name__ == "__main__":
    main()