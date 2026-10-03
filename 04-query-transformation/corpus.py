"""A small collection of engineering notes, and a semantic retriever over it."""
from dataclasses import dataclass

from sentence_transformers import SentenceTransformer

QUESTION = (
    "hey, my python service keeps getting slower the longer it runs "
    "- any idea what's going on?"
)

PASSAGES = {
    "mem-leak-01": (
        "Memory leaks in long-running Python services: objects that stay "
        "referenced by caches, globals or registered callbacks are never "
        "freed, so resident memory grows for hours and garbage collection "
        "pauses lengthen until throughput degrades."
    ),
    "profile-02": (
        "To find out why a Python function is slow, profile it with "
        "cProfile and sort the report by cumulative time to see which "
        "calls dominate."
    ),
    "conn-pool-03": (
        "Connection pool exhaustion in a service: when database connections "
        "are checked out and never returned, requests queue for a free "
        "connection, and response times climb steadily for as long as the "
        "process keeps running."
    ),
    "startup-04": (
        "Make a Python service start faster by importing heavy modules "
        "lazily and deferring expensive initialisation until first use."
    ),
    "async-05": (
        "Use asyncio to keep a Python service responsive while it waits on "
        "network calls, instead of blocking a thread per request."
    ),
    "gil-06": (
        "Python threads share the global interpreter lock, so CPU-bound "
        "work runs faster in separate processes than in threads."
    ),
    "vectorize-07": (
        "Speed up numeric Python code by replacing loops with vectorised "
        "NumPy operations."
    ),
    "logging-08": (
        "Configure log rotation so log files do not fill the disk on "
        "servers that stay up for weeks."
    ),
    "tests-09": (
        "Slow test suites can be sped up by running tests in parallel with "
        "pytest-xdist and caching fixtures."
    ),
    "deploy-10": (
        "Roll out a new version of a service gradually and watch error "
        "rates before sending it all traffic."
    ),
}


@dataclass
class Passage:
    id: str
    text: str
    score: float


class Retriever:
    def __init__(self, passages):
        self.ids = list(passages)
        self.texts = list(passages.values())
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.emb = self.model.encode(self.texts, normalize_embeddings=True)

    def search(self, query, k=5):
        q = self.model.encode(query, normalize_embeddings=True)
        scores = self.emb @ q
        order = sorted(range(len(self.ids)), key=lambda i: -scores[i])[:k]
        return [Passage(self.ids[i], self.texts[i], float(scores[i]))
                for i in order]


retriever = Retriever(PASSAGES)
