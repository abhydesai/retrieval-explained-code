"""HyDE: search with a generated, hypothetical answer, not the question."""
from pathlib import Path

from corpus import QUESTION, retriever
from llm import ask


def hypothetical_answer(question):
    prompt = (
        "Write a short passage (3-4 sentences) that plausibly answers this "
        "question, in the style of technical documentation. It does not "
        "need to be factually correct.\n\n"
        f"Question: {question}"
    )
    return ask(prompt)


if __name__ == "__main__":
    hypothetical = hypothetical_answer(QUESTION)
    Path("hypothetical.txt").write_text(hypothetical)  # log the input that ran
    print("hypothetical:", hypothetical)
    print()
    hyde_hits = retriever.search(hypothetical, k=5)
    for p in hyde_hits:
        print(p.id, "-", p.text[:60])

    # The hypothetical is a search key only. Discard it here.
    # Only passages in hyde_hits may be shown, cited, or passed downstream.
