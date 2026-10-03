"""Count how many labeled answer passages each search input retrieves."""
from corpus import QUESTION, retriever
from hyde import hypothetical_answer
from rewrite import rewrite

# Passages we've labeled as actually answering the question
relevant = {"mem-leak-01", "conn-pool-03"}


def hits_at_k(query, k=5):
    ids = {p.id for p in retriever.search(query, k=k)}
    return len(ids & relevant)


drifted = "python memory leak fixes"  # a rewrite that guessed the diagnosis

for name, q in [
    ("raw question", QUESTION),
    ("rewrite", rewrite(QUESTION)),
    ("hyde", hypothetical_answer(QUESTION)),
    ("drifted rewrite", drifted),
]:
    print(f"{name:16s} hits@5 = {hits_at_k(q)} / {len(relevant)}")
