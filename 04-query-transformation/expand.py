"""Expansion: search several alternative queries and merge the results."""
from pathlib import Path

from corpus import QUESTION, retriever
from llm import ask


def expand(question, n=3):
    prompt = (
        f"Write {n} alternative search queries for this question, one per "
        "line. Vary the terminology but keep the same information need. "
        "Return only the queries.\n\n"
        f"Question: {question}"
    )
    reply = ask(prompt)
    return [line.strip() for line in reply.splitlines() if line.strip()]


rewritten = Path("rewrite.txt").read_text()  # the rewrite that ran
queries = [rewritten] + expand(QUESTION)
for q in queries:
    print("query:", q)

seen, merged = set(), []
for q in queries:
    for p in retriever.search(q, k=5):
        if p.id not in seen:
            seen.add(p.id)
            merged.append(p)

print()
expansion_hits = merged[:5]
for p in expansion_hits:
    print(p.id, "-", p.text[:60])
