"""Rewrite the question as one search query, then search with the rewrite."""
from pathlib import Path

from corpus import QUESTION, retriever
from llm import ask


def rewrite(question):
    prompt = (
        "Rewrite this user question as one concise, self-contained search "
        "query. Preserve the original intent; do not add assumptions or "
        "guess at causes. Return only the query.\n\n"
        f"Question: {question}"
    )
    return ask(prompt)


if __name__ == "__main__":
    rewritten = rewrite(QUESTION)
    Path("rewrite.txt").write_text(rewritten)  # log the input that ran
    print("rewrite:", rewritten)
    print()
    for p in retriever.search(rewritten, k=5):
        print(p.id, "-", p.text[:60])
