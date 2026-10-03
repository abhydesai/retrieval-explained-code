"""Cosine similarity: score three passages against one question."""
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

passages = [
    "To change your password, open Settings and choose Security.",
    "Our office is closed on public holidays.",
    "You can update your login credentials from the account page.",
]


def cosine(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


if __name__ == "__main__":
    query = model.encode("How do I reset my password?")
    vecs = model.encode(passages)

    for text, v in zip(passages, vecs):
        print(f"{cosine(query, v):.2f}  {text}")
