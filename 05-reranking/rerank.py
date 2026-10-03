"""Second stage: rerank the candidates with a cross-encoder."""
from sentence_transformers import CrossEncoder

from first_stage import passages, query

reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")


def rerank(candidates):
    pairs = [(query, passage) for passage in candidates]
    scores = reranker.predict(pairs)
    return sorted(zip(scores.tolist(), candidates), reverse=True)


if __name__ == "__main__":
    for score, passage in rerank(passages):
        print(f"{score:6.2f}  {passage[:60]}...")
