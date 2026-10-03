"""Checkpoint 1: is the evidence in the corpus at all?"""
from support import CORPUS

needle = "45 days"
hits = [d for d in CORPUS if needle in d["text"]]
print(len(hits), hits[0]["id"] if hits else "NOT IN CORPUS")
