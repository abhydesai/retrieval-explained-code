"""The baseline: search with the question exactly as the user typed it."""
from corpus import QUESTION, retriever

baseline_hits = retriever.search(QUESTION, k=5)
for p in baseline_hits:
    print(p.id, "-", p.text[:60])
