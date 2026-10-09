import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / "data/evaluation/test_grades_proposed.jsonl"
stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S_%fZ")

backup_dir = ROOT / "review_backups" / stamp
backup_dir.mkdir(parents=True, exist_ok=False)
shutil.copy2(path, backup_dir / path.name)

records = [
    json.loads(line)
    for line in path.read_text(encoding="utf-8-sig").splitlines()
    if line.strip()
]

for record in records:
    record.update({
        "human_correctness_0_2": None,
        "human_grounding": None,
        "human_abstention_pass": None,
        "human_reviewer": "",
        "human_notes": "",
        "review_status": "assistant_proposed",
    })

path.write_text(
    "".join(json.dumps(record, ensure_ascii=False) + "\n"
            for record in records),
    encoding="utf-8",
)

# Archive the misleading generated summaries.
for name in ("evaluation_summary_human.json", "evaluation_summary_human.md"):
    summary = ROOT / "reports" / name
    if summary.exists():
        shutil.move(str(summary), str(backup_dir / name))

print(f"Reset human review fields for {len(records)} records.")
print("Original file and previous human summaries backed up to:", backup_dir)
print("Proposed grades and benchmark results are unchanged.")