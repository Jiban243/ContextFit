import json
import re
from pathlib import Path

from rank_bm25 import BM25Okapi


def tokenize(text):
    """Use identical word processing for documents and questions."""
    return re.findall(r"[a-z0-9_]+", text.lower())


class BM25Retriever:
    def __init__(self, chunks_path):
        path = Path(chunks_path)
        self.chunks = [
            json.loads(line)
            for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]

        if not self.chunks:
            raise ValueError("The chunk collection is empty.")

        ids = [chunk["chunk_id"] for chunk in self.chunks]
        if len(ids) != len(set(ids)):
            raise ValueError("Duplicate chunk IDs found.")

        corpus = [tokenize(chunk["text"]) for chunk in self.chunks]

        if any(not tokens for tokens in corpus):
            raise ValueError("A chunk contains no searchable words.")

        self.vocabulary = {
            token for tokens in corpus for token in tokens
        }
        self.index = BM25Okapi(corpus, k1=1.5, b=0.75)

    def search(self, question, top_k=10):
        if not isinstance(question, str) or not question.strip():
            raise ValueError("Question must be a non-empty string.")

        if type(top_k) is not int or top_k < 1:
            raise ValueError("top_k must be a positive integer.")

        query_tokens = tokenize(question)

        if not set(query_tokens).intersection(self.vocabulary):
            return []

        scores = self.index.get_scores(query_tokens)

        # Stable ordering when scores are equal.
        ranked = sorted(
            range(len(self.chunks)),
            key=lambda i: (
                -float(scores[i]),
                self.chunks[i]["chunk_id"],
            ),
        )

        results = []
        for index in ranked:
            if scores[index] <= 0:
                continue

            results.append({
                **self.chunks[index],
                "score": float(scores[index]),
            })

            if len(results) == top_k:
                break

        return results