import sys
from importlib.metadata import version

from rank_bm25 import BM25Okapi
from transformers import AutoTokenizer


def main():
    print("Python:", sys.version.split()[0])

    for package in ("rank-bm25", "transformers", "tokenizers"):
        print(f"{package}: {version(package)}")

    documents = [
        "customers can request a refund within fourteen days",
        "support is available monday through friday",
        "shipping takes five business days",
    ]

    index = BM25Okapi([text.split() for text in documents])
    scores = index.get_scores("refund".split())
    best_index = max(range(len(scores)), key=lambda i: scores[i])

    assert best_index == 0, "Retrieval check failed."
    print("\nRetrieval check: PASS")
    print("Retrieved:", documents[best_index])

    tokenizer = AutoTokenizer.from_pretrained(
        "Qwen/Qwen2.5-1.5B-Instruct"
    )

    text = "[doc1] Customers can request a refund within 14 days."
    token_ids = tokenizer.encode(text, add_special_tokens=False)

    assert token_ids, "Tokenizer returned no tokens."
    assert tokenizer.chat_template, "Chat template is missing."

    print("\nTokenizer check: PASS")
    print("Sample token count:", len(token_ids))
    print("Model weights were not loaded.")


if __name__ == "__main__":
    main()