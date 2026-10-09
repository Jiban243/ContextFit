import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHUNKS_PATH = ROOT / "data/processed/chunks.jsonl"
OUT = ROOT / "data/evaluation"

# Each row contains:
# question, required answer points, one sufficient evidence set.
DEV = [
    (
        "Why use separate virtual environments for applications?",
        ["They isolate dependencies so applications can use conflicting package versions."],
        ["python_venv_chunk001"],
    ),
    (
        "What does the PYTHONPATH variable do?",
        ["It supplies directories used to initialize the module search path."],
        ["python_modules_chunk007"],
    ),
    (
        "When is the finally clause executed?",
        ["It executes before the try statement completes, whether or not an exception occurs."],
        ["python_errors_chunk011"],
    ),
    (
        "Which command leaves an active virtual environment?",
        ["Run deactivate."],
        ["python_venv_chunk003"],
    ),
    (
        "How can I inspect an installed package and export installed versions for another environment?",
        [
            "Use python -m pip show PACKAGE to inspect a package.",
            "Use python -m pip freeze to produce requirements-format output.",
        ],
        ["python_venv_chunk005", "python_venv_chunk006"],
    ),
    (
        "What monthly fee does the documentation specify for a hosted virtual-environment service?",
        ["State that the supplied documentation does not specify this fee."],
        [],
    ),
]

DIRECT = [
    (
        "Which Python version is installed in an environment created by python3.12 -m venv?",
        ["Python 3.12, because venv uses the interpreter that runs the command."],
        ["python_venv_chunk002"],
    ),
    (
        "How do I install exactly version 2.6.0 of requests using pip?",
        ["Run python -m pip install requests==2.6.0."],
        ["python_venv_chunk004"],
    ),
    (
        "What does pip do if I repeat the installation command for an already installed requested version?",
        ["It notices that the requested version is installed and does nothing."],
        ["python_venv_chunk004"],
    ),
    (
        "How can another developer install the packages listed in requirements.txt?",
        ["Run python -m pip install -r requirements.txt."],
        ["python_venv_chunk006"],
    ),
    (
        "Does import fibo directly add fib and fib2 to the current namespace?",
        ["No. It adds the module name fibo; access its functions through that module."],
        ["python_modules_chunk002"],
    ),
    (
        "How can I reload a changed module during an interactive interpreter session?",
        ["Use importlib.reload(modulename), after importing importlib."],
        ["python_modules_chunk006"],
    ),
    (
        "Where does Python cache compiled modules, and how does it detect stale cached code?",
        [
            "It stores compiled modules in __pycache__ using version-tagged .pyc names.",
            "It checks the source modification date against the compiled version.",
        ],
        ["python_modules_chunk008"],
    ),
    (
        "Does reading a program from a .pyc file make its execution faster than reading it from .py?",
        ["No. Compiled files load faster, but the program itself does not run faster for that reason."],
        ["python_modules_chunk009"],
    ),
    (
        "What happens if an exception in a try clause matches none of its except clauses?",
        ["It propagates to outer handlers; if none handles it, execution stops with an error."],
        ["python_errors_chunk004"],
    ),
    (
        "If several except clauses could match an exception, which one runs?",
        ["The first matching except clause runs."],
        ["python_errors_chunk005"],
    ),
    (
        "Why put successful follow-up work in a try statement's else clause?",
        [
            "It runs when the try clause raises no exception.",
            "It avoids accidentally catching exceptions from follow-up work in the original handlers.",
        ],
        ["python_errors_chunk007"],
    ),
    (
        "How can I add explanatory notes to a caught exception, and where are those notes displayed?",
        [
            "Call add_note with a string.",
            "The standard traceback displays the notes after the exception in insertion order.",
        ],
        ["python_errors_chunk018"],
    ),
]

MULTI = [
    (
        "How can I create a virtual environment named tutorial-env and then install dependencies from requirements.txt into it?",
        [
            "Create it with python -m venv tutorial-env and activate it.",
            "Then run python -m pip install -r requirements.txt.",
        ],
        ["python_venv_chunk002", "python_venv_chunk006"],
    ),
    (
        "How can I upgrade requests and record the resulting installed package versions for sharing?",
        [
            "Run python -m pip install --upgrade requests.",
            "Export versions with python -m pip freeze > requirements.txt.",
        ],
        ["python_venv_chunk005", "python_venv_chunk006"],
    ),
    (
        "How can I import fibo under the name fib and reload that module after editing it?",
        [
            "Use import fibo as fib.",
            "After importing importlib, call importlib.reload(fib).",
        ],
        ["python_modules_chunk005", "python_modules_chunk006"],
    ),
    (
        "What does Python's compiled-module cache help with, and can compileall generate these files for a directory?",
        [
            "The cache speeds up module loading.",
            "compileall can create .pyc files for modules in a directory.",
        ],
        ["python_modules_chunk008", "python_modules_chunk009"],
    ),
    (
        "How do I explicitly link a new exception to its cause, and how do I suppress automatic exception chaining?",
        [
            "Use raise NewException from original_exception to indicate the cause.",
            "Use raise NewException from None to suppress automatic chaining.",
        ],
        ["python_errors_chunk009", "python_errors_chunk010"],
    ),
    (
        "How can several exception instances be raised together and only those of a chosen type handled?",
        [
            "Wrap exception instances in an ExceptionGroup and raise it.",
            "Use except* to handle matching types within the group.",
        ],
        ["python_errors_chunk015", "python_errors_chunk016"],
    ),
]

UNANSWERABLE = [
    "What exact maximum disk space can a Python virtual environment occupy?",
    "What pip version is currently installed on my laptop?",
    "Which private package-index URL does our company require?",
    "What numerical speedup is guaranteed when loading a cached .pyc module?",
    "What maximum number of exception notes does this documentation specify?",
    "What is the current latest requests release on PyPI?",
]


def make_record(identifier, split, category, row):
    question, points, sources = row

    return {
        "question_id": identifier,
        "split": split,
        "category": category,
        "question": question,
        "answerable": bool(sources),
        "expected_answer_points": points,
        # All IDs in one group together form a sufficient evidence set.
        # Additional alternative groups may be added during review.
        "sufficient_evidence_sets": [sources] if sources else [],
        "review_status": "pending",
        "review_notes": "",
    }


def main():
    chunks = {
        c["chunk_id"]: c
        for line in CHUNKS_PATH.read_text(encoding="utf-8").splitlines()
        if line.strip()
        for c in [json.loads(line)]
    }

    development = [
        make_record(
            f"dev_{i:03d}",
            "dev",
            "unanswerable" if not row[2] else
            ("multi" if len(row[2]) > 1 else "direct"),
            row,
        )
        for i, row in enumerate(DEV, 1)
    ]

    heldout = []
    for category, rows in (("direct", DIRECT), ("multi", MULTI)):
        for row in rows:
            heldout.append(make_record(
                f"test_{len(heldout) + 1:03d}",
                "test",
                category,
                row,
            ))

    for question in UNANSWERABLE:
        heldout.append(make_record(
            f"test_{len(heldout) + 1:03d}",
            "test",
            "unanswerable",
            (
                question,
                ["State that the answer cannot be determined from the supplied documentation."],
                [],
            ),
        ))

    records = development + heldout
    assert len(development) == 6
    assert len(heldout) == 24
    assert len({r["question"] for r in records}) == 30

    for record in records:
        for group in record["sufficient_evidence_sets"]:
            for source_id in group:
                if source_id not in chunks:
                    raise ValueError(f"Unknown evidence ID: {source_id}")

    OUT.mkdir(parents=True, exist_ok=True)

    # Avoid overwriting annotations after someone has reviewed them.
    destinations = [
        OUT / "dev_gold.jsonl",
        OUT / "test_gold.jsonl",
        OUT / "annotation_review.md",
        OUT / "evaluation_manifest.json",
    ]
    if any(path.exists() for path in destinations):
        raise FileExistsError(
            "Evaluation outputs already exist. Preserve existing reviews "
            "and edit those files directly."
        )

    for name, subset in (
        ("dev_gold.jsonl", development),
        ("test_gold.jsonl", heldout),
    ):
        with (OUT / name).open("w", encoding="utf-8") as file:
            for record in subset:
                file.write(json.dumps(record, ensure_ascii=False) + "\n")

    review = ["# ContextFit annotation review\n"]
    for record in records:
        review.append(
            f"\n## {record['question_id']} — {record['category']}\n"
            f"\n{record['question']}\n"
        )
        for point in record["expected_answer_points"]:
            review.append(f"- Expected: {point}\n")

        if not record["answerable"]:
            review.append(
                "\nCheck the entire corpus: no passage should supply "
                "the requested answer. Do not confuse an absent answer "
                "with a retrieval failure.\n"
            )

        for group in record["sufficient_evidence_sets"]:
            for source_id in group:
                review.append(
                    f"\n### {source_id}\n\n"
                    + chunks[source_id]["text"] + "\n"
                )

    (OUT / "annotation_review.md").write_text(
        "".join(review), encoding="utf-8"
    )

    manifest = {
        "status": "draft_pending_human_review",
        "dev_count": 6,
        "test_count": 24,
        "chunks_sha256": hashlib.sha256(
            CHUNKS_PATH.read_bytes()
        ).hexdigest(),
        "note": "Do not pass gold answers or evidence labels to inference.",
    }
    (OUT / "evaluation_manifest.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )

    print("Created 6 development and 24 held-out draft records.")
    print("All supporting chunk IDs exist.")
    print("Review:", OUT / "annotation_review.md")


if __name__ == "__main__":
    main()