REQUIRED_FIELDS = (
    "question_id",
    "question",
    "policy",
    "context",
    "source_ids",
)


def validate_record(record):
    if not isinstance(record, dict):
        raise ValueError("Each request must be a dictionary.")

    missing = [key for key in REQUIRED_FIELDS if key not in record]
    if missing:
        raise ValueError(f"Missing required fields: {missing}")

    for key in ("question_id", "question", "policy"):
        value = record[key]
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{key} must be a non-empty string.")

    if not isinstance(record["context"], str):
        raise ValueError("context must be a string.")

    sources = record["source_ids"]
    if not isinstance(sources, list):
        raise ValueError("source_ids must be a list.")

    if any(not isinstance(s, str) or not s.strip() for s in sources):
        raise ValueError("Each source ID must be a non-empty string.")

    if len(sources) != len(set(sources)):
        raise ValueError("source_ids must not contain duplicates.")

    if not record["context"].strip() and sources:
        raise ValueError("Empty context must have no source IDs.")

    for source_id in sources:
        if f"[{source_id}]" not in record["context"]:
            raise ValueError(
                f"Source marker [{source_id}] is missing from context."
            )
