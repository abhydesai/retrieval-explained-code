"""Second stage: rerank the same candidates with a cross-encoder."""
import time

from sentence_transformers import CrossEncoder

from first_stage import first_stage, passages, query

reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

pairs = [(query, passage) for passage in passages]
rerank_scores = reranker.predict(pairs)

reranked = sorted(zip(rerank_scores.tolist(), passages), reverse=True)
for score, passage in reranked:
    print(f"{score:6.2f}  {passage[:60]}...")

start = time.perf_counter()
reranker.predict(pairs)
elapsed = time.perf_counter() - start
print(f"Reranked {len(pairs)} passages in {elapsed * 1000:.0f} ms")


def hit_at_k(ranking, answer_passage, k):
    top_k = [passage for _, passage in ranking[:k]]
    return answer_passage in top_k


answer = passages[2]  # the 'contact support' passage
ranked = first_stage()

print("Answer in top-1 before rerank:", hit_at_k(ranked, answer, k=1))
print("Answer in top-1 after  rerank:", hit_at_k(reranked, answer, k=1))
