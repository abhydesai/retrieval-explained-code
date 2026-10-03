"""How long the cross-encoder takes as the shortlist grows."""
import time

from first_stage import passages, query
from rerank import reranker

pairs = [(query, passage) for passage in passages]
reranker.predict(pairs * 100)  # warm up once before timing

# The four candidates, repeated, stand in for longer shortlists
for size in [4, 40, 400, 4000]:
    batch = pairs * (size // 4)
    start = time.perf_counter()
    reranker.predict(batch)
    elapsed = time.perf_counter() - start
    print(f"{size:4d} pairs  {elapsed * 1000:5.0f} ms")
