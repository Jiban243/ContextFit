import hashlib
import json
import random
from datetime import datetime, timezone
from pathlib import Path


def job_id(record, repeat, config):
    payload = {
        "request": record,
        "repeat": repeat,
        "config": config,
        "runner_version": "v1",
    }
    raw = json.dumps(payload, sort_keys=True).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def run_batch(records, predict, output_path, config, repeats=3):
    """Run sequential requests, saving each attempt and skipping successes."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    completed = set()
    if output_path.exists():
        for line in output_path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                entry = json.loads(line)
                if entry["status"] == "ok":
                    completed.add(entry["job_id"])

    jobs = [
        (record, repeat)
        for repeat in range(1, repeats + 1)
        for record in records
    ]
    random.Random(42).shuffle(jobs)

    counts = {"ok": 0, "error": 0, "skipped": 0}

    for record, repeat in jobs:
        identifier = job_id(record, repeat, config)
        label = f'{record["question_id"]} | repeat {repeat}'

        if identifier in completed:
            counts["skipped"] += 1
            print("SKIP:", label)
            continue

        entry = {
            "job_id": identifier,
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "repeat": repeat,
            "config": config,
            "request": record,
        }

        try:
            entry["result"] = predict(record)
            entry["status"] = "ok"
        except Exception as exc:
            entry["status"] = "error"
            entry["error_type"] = type(exc).__name__
            entry["error"] = str(exc)

        with output_path.open("a", encoding="utf-8") as file:
            file.write(json.dumps(entry, ensure_ascii=False) + "\n")

        counts[entry["status"]] += 1
        if entry["status"] == "ok":
            completed.add(identifier)

        print(entry["status"].upper() + ":", label)

    return counts
