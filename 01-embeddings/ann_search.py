"""Approximate search with an HNSW index, built before any query arrives."""
import hnswlib

from similarity import model, passages

vecs = model.encode(passages)

index = hnswlib.Index(space="cosine", dim=384)
index.init_index(max_elements=len(vecs))
index.add_items(vecs)

index.set_ef(50)  # search width: higher means better recall, and slower

query = model.encode("How do I reset my password?")
labels, distances = index.knn_query(query, k=2)
for i, d in zip(labels[0], distances[0]):
    print(f"{1 - d:.2f}  {passages[i]}")
