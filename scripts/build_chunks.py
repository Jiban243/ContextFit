import hashlib
import json
from collections import Counter
from pathlib import Path

from transformers import AutoTokenizer

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data/processed/documents.jsonl"
OUTPUT = ROOT / "data/processed/chunks.jsonl"
MODEL_ID = "Qwen/Qwen2.5-1.5B-Instruct"
MAX_TOKENS = 300


def token_count(tokenizer, text):
    return len(tokenizer.encode(text, add_special_tokens=False))


def split_block(tokenizer, text):
    """Split oversized blocks using original-text character offsets."""
    if token_count(tokenizer, text) <= MAX_TOKENS:
        return [text]

    encoded = tokenizer(
        text,
        add_special_tokens=False,
        return_offsets_mapping=True,
    )
    offsets = encoded["offset_mapping"]
    pieces = []
    start = 0
    previous_end = 0

    while start < len(offsets):
        end = min(start + MAX_TOKENS, len(offsets))

        while end > start:
            char_end = offsets[end - 1][1]
            piece = text[previous_end:char_end]

            if token_count(tokenizer, piece) <= MAX_TOKENS:
                break
            end -= 1

        if end == start:
            raise ValueError("Could not split block within token limit.")

        if piece.strip():
            pieces.append(piece)

        previous_end = char_end
        start = end

    tail = text[previous_end:]
    if tail.strip():
        pieces.append(tail)

    return pieces


def main():
    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_ID, use_fast=True
    )
    documents = [
        json.loads(line)
        for line in INPUT.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]

    chunks = []

    for document in documents:
        grouped = []
        current = ""

        for block in document["blocks"]:
            for piece in split_block(tokenizer, block):
                candidate = (
                    current + "\n\n" + piece if current else piece
                )

                if token_count(tokenizer, candidate) <= MAX_TOKENS:
                    current = candidate
                else:
                    if current:
                        grouped.append(current)
                    current = piece

        if current:
            grouped.append(current)

        for number, text in enumerate(grouped, start=1):
            count = token_count(tokenizer, text)
            assert 0 < count <= MAX_TOKENS

            chunks.append({
                "chunk_id": (
                    f'{document["document_id"]}_chunk{number:03d}'
                ),
                "document_id": document["document_id"],
                "title": document["title"],
                "url": document["url"],
                "document_text_sha256": document["text_sha256"],
                "text": text,
                "token_count": count,
                "text_sha256": hashlib.sha256(
                    text.encode("utf-8")
                ).hexdigest(),
            })

    ids = [chunk["chunk_id"] for chunk in chunks]
    assert len(ids) == len(set(ids)), "Duplicate chunk IDs."
    assert chunks, "No chunks generated."

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", encoding="utf-8") as file:
        for chunk in chunks:
            file.write(json.dumps(chunk, ensure_ascii=False) + "\n")

    manifest = {
        "model_id": MODEL_ID,
        "max_chunk_tokens": MAX_TOKENS,
        "overlap_tokens": 0,
        "chunker_version": "block_packing_v1",
        "documents_sha256": hashlib.sha256(
            INPUT.read_bytes()
        ).hexdigest(),
        "chunks_sha256": hashlib.sha256(
            OUTPUT.read_bytes()
        ).hexdigest(),
        "tokenizer_backend_sha256": hashlib.sha256(
            tokenizer.backend_tokenizer.to_str().encode("utf-8")
        ).hexdigest(),
        "chunk_count": len(chunks),
    }

    OUTPUT.with_name("chunk_manifest.json").write_text(
        json.dumps(manifest, indent=2),
        encoding="utf-8",
    )

    for document_id, count in Counter(
        chunk["document_id"] for chunk in chunks
    ).items():
        print(f"{document_id}: {count} chunks")

    print(f"\nTotal chunks: {len(chunks)}")
    print(
        "Token range:",
        min(c["token_count"] for c in chunks),
        "to",
        max(c["token_count"] for c in chunks),
    )
    print("Saved:", OUTPUT)

    print("\nFirst chunk:")
    print(chunks[0]["chunk_id"])
    print(chunks[0]["text"])


if __name__ == "__main__":
    main()