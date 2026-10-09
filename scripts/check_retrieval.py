import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from contextfit.retrieval import BM25Retriever


def main():
    retriever = BM25Retriever(
        ROOT / "data/processed/chunks.jsonl"
    )

    questions = [
        "Why use separate virtual environments for applications?",
        "What does the PYTHONPATH variable do?",
        "When is the finally clause executed?",
    ]

    for question in questions:
        print("\nQUESTION:", question)

        hits = retriever.search(question, top_k=3)
        assert hits, "Expected retrieval results."

        # The same query should produce the same ordered results.
        repeated = retriever.search(question, top_k=3)
        assert hits == repeated, "Retrieval order changed."

        for rank, hit in enumerate(hits, start=1):
            print(
                f"\n{rank}. {hit['chunk_id']} "
                f"| score={hit['score']:.3f}"
            )
            print(hit["text"][:500].replace("\n", " "))

    assert retriever.search("zzzxxyyqq_nonexistent") == []
    print("\nPASS: repeatable ranking and no-match handling.")


if __name__ == "__main__":
    main()