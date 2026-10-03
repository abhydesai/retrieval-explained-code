"""Heading-aware chunking: cut before every second-level heading."""
import re
from pathlib import Path

DOC = Path("travel-policy.md").read_text()


def split_by_section(text):
    parts = re.split(r"\n(?=## )", text)
    return [p.strip() for p in parts if p.strip()]


if __name__ == "__main__":
    for i, chunk in enumerate(split_by_section(DOC)):
        print(f"--- chunk {i}: {len(chunk)} characters ---")
        print(chunk)
