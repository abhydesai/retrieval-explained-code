"""Keyword, semantic and hybrid search over six short passages.

    python search.py keyword "HTTP 429 too many requests"
    python search.py semantic "How do I speed up my application?"
    python search.py hybrid "avoid 429 errors when sending calls too quickly"
"""
import argparse

from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer

passages = [
    "HTTP 429 Too Many Requests means the client sent too many requests "
    "in a given time window.",
    "Slow the pace of outgoing calls with exponential backoff when the "
    "server signals rate limiting.",
    "Response latency drops when you cache frequent lookups instead of "
    "recomputing them.",
    "Set the API_TIMEOUT environment variable to control how long the "
    "client waits for a reply.",
    "Authentication tokens expire after one hour; refresh them before "
    "further use.",
    "Batching several operations into one call reduces network overhead.",
]

bm25 = BM25Okapi([p.lower().split() for p in passages])
model = SentenceTransformer("all-MiniLM-L6-v2")
doc_emb = model.encode(passages, normalize_embeddings=True)


def keyword_scores(query):
    return bm25.get_scores(query.lower().split())


def semantic_scores(query):
    return doc_emb @ model.encode(query, normalize_embeddings=True)


def top_k(scores, k):
    return sorted(range(len(passages)), key=lambda i: -scores[i])[:k]


def rrf(rankings, k=60):
    scores = {}
    for ranking in rankings:
        for rank, doc_id in enumerate(ranking):
            scores[doc_id] = scores.get(doc_id, 0) + 1 / (k + rank + 1)
    return scores


parser = argparse.ArgumentParser()
parser.add_argument("method", choices=["keyword", "semantic", "hybrid"])
parser.add_argument("query")
parser.add_argument("--k", type=int, default=3)
args = parser.parse_args()

if args.method == "hybrid":
    keyword_ids = top_k(keyword_scores(args.query), args.k)
    semantic_ids = top_k(semantic_scores(args.query), args.k)
    fused = rrf([keyword_ids, semantic_ids])
    for rank, i in enumerate(sorted(fused, key=fused.get, reverse=True), 1):
        found_by = [name for name, ids in
                    [("keyword", keyword_ids), ("semantic", semantic_ids)]
                    if i in ids]
        print(f"{rank}  P{i + 1}  {fused[i]:.4f}  {' + '.join(found_by)}")
else:
    score_fn = keyword_scores if args.method == "keyword" else semantic_scores
    scores = score_fn(args.query)
    for rank, i in enumerate(top_k(scores, args.k), start=1):
        print(f"{rank}  P{i + 1}  {scores[i]:.3f}  {passages[i][:44]}")
