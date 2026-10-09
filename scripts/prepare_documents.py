import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"

SOURCES = [
    {
        "document_id": "python_venv",
        "url": "https://docs.python.org/3.13/tutorial/venv.html",
    },
    {
        "document_id": "python_modules",
        "url": "https://docs.python.org/3.13/tutorial/modules.html",
    },
    {
        "document_id": "python_errors",
        "url": "https://docs.python.org/3.13/tutorial/errors.html",
    },
]


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def main():
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    documents = []

    for source in SOURCES:
        document_id = source["document_id"]
        html_path = RAW_DIR / f"{document_id}.html"
        metadata_path = RAW_DIR / f"{document_id}.metadata.json"

        if html_path.exists() != metadata_path.exists():
            raise RuntimeError(
                f"Incomplete snapshot for {document_id}. "
                "Both HTML and metadata must be present."
            )

        if html_path.exists():
            raw = html_path.read_bytes()
            metadata = json.loads(
                metadata_path.read_text(encoding="utf-8")
            )
            if sha256(raw) != metadata["html_sha256"]:
                raise ValueError(f"Snapshot changed: {html_path}")
            print("Using saved snapshot:", document_id)

        else:
            response = requests.get(source["url"], timeout=60)
            response.raise_for_status()
            raw = response.content

            metadata = {
                **source,
                "resolved_url": response.url,
                "downloaded_at_utc": datetime.now(
                    timezone.utc
                ).isoformat(),
                "html_sha256": sha256(raw),
            }

            html_path.write_bytes(raw)
            metadata_path.write_text(
                json.dumps(metadata, indent=2),
                encoding="utf-8",
            )
            print("Downloaded:", document_id)

        soup = BeautifulSoup(raw, "html.parser")
        article = soup.select_one('div.body[role="main"]')

        if article is None:
            raise ValueError(
                f"Main article not found for {document_id}"
            )

        heading = article.find("h1")
        if heading is None:
            raise ValueError(f"Title missing for {document_id}")

        title = heading.get_text(" ", strip=True).replace("¶", "").strip()

        for element in article.select(
            "a.headerlink, script, style"
        ):
            element.decompose()

        # Keep paragraphs and code examples as separate blocks.
        blocks = []
        for element in article.find_all(
            ["h1", "h2", "h3", "h4", "p", "pre"]
        ):
            if element.name == "pre":
                text = element.get_text().strip()
            else:
                text = element.get_text(" ", strip=True)

            if text:
                blocks.append(text)

        text = "\n\n".join(blocks)

        if len(text) < 500:
            raise ValueError(
                f"Unexpectedly short document: {document_id}"
            )

        documents.append({
            **metadata,
            "title": title,
            "blocks": blocks,
            "text": text,
            "text_sha256": sha256(text.encode("utf-8")),
        })

        print(
            f"  {len(blocks)} blocks; "
            f"{len(text):,} characters"
        )

    output_path = PROCESSED_DIR / "documents.jsonl"

    with output_path.open("w", encoding="utf-8") as file:
        for document in documents:
            file.write(
                json.dumps(document, ensure_ascii=False) + "\n"
            )

    print(f"\nSaved {len(documents)} documents to {output_path}")


if __name__ == "__main__":
    main()