"""Count how many labeled answer passages each search input retrieves."""
from pathlib import Path

from corpus import QUESTION, retriever

# Passages we've labeled as actually answering the question
relevant = {"mem-leak-01", "conn-pool-03"}


def hits_at_k(query, k=5):
    ids = {p.id for p in retriever.search(query, k=k)}
    return len(ids & relevant)


drifted = "python memory leak fixes"  # a rewrite that guessed the diagnosis

for name, q in [
    ("raw question", QUESTION),
    ("rewrite", Path("rewrite.txt").read_text()),
    ("hyde", Path("hypothetical.txt").read_text()),
    ("drifted rewrite", drifted),
]:
    print(f"{name:16s} hits@5 = {hits_at_k(q)} / {len(relevant)}")
