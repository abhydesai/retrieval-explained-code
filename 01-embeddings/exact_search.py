"""Exact nearest-neighbor search: score everything, sort, take the top k."""
import numpy as np

from similarity import model, passages

query = model.encode("How do I reset my password?")
vecs = model.encode(passages)

scores = vecs @ query / (
    np.linalg.norm(vecs, axis=1) * np.linalg.norm(query)
)

k = 2
top_k = np.argsort(scores)[::-1][:k]
for i in top_k:
    print(f"{scores[i]:.2f}  {passages[i]}")
