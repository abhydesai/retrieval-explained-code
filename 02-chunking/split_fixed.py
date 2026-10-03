"""Fixed-size chunking: slice the policy every `size` characters."""
import argparse
from pathlib import Path

DOC = Path("travel-policy.md").read_text()


def split_fixed(text, size, overlap=0):
    step = size - overlap
    return [text[i:i + size] for i in range(0, len(text), step)]


parser = argparse.ArgumentParser()
parser.add_argument("size", type=int)
parser.add_argument("--overlap", type=int, default=0)
args = parser.parse_args()

step = args.size - args.overlap
for i, chunk in enumerate(split_fixed(DOC, args.size, args.overlap)):
    start = i * step
    print(f"--- chunk {i}: characters {start} to {start + len(chunk)} ---")
    print(chunk)
