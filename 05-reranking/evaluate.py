"""Is the passage that answers the question in the top k?"""
from first_stage import first_stage, passages
from rerank import rerank

answer = passages[2]  # the 'contact support' passage


def hit_at_k(ranking, k):
    top_k = [passage for _, passage in ranking[:k]]
    return answer in top_k


before = first_stage()
after = rerank(passages)

for k in [1, 4]:
    print(f"top {k}:  before {hit_at_k(before, k)}  after {hit_at_k(after, k)}")
