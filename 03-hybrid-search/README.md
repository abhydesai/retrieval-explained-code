# 03 — Keyword, semantic and hybrid search

Six short passages searched three ways: keyword search with BM25, semantic search with
embeddings, and hybrid search that fuses the two rankings with reciprocal rank fusion.

| Command | What it shows |
|---|---|
| `python search.py keyword "HTTP 429 too many requests"` | an exact code only one passage contains |
| `python search.py keyword "How do I speed up my application?"` | a question that shares no words with the caching passage |
| `python search.py semantic "How do I speed up my application?"` | the same question matched on meaning |
| `python search.py semantic "429" --k 6` | a bare identifier, searched by meaning |
| `python search.py hybrid "avoid 429 errors when sending calls too quickly"` | both rankings fused, with which search found each passage |

`--k` sets how many results each search returns (default 3). Keyword scores are BM25 and
semantic scores are cosine similarities: the two scales are not comparable, which is why hybrid
search fuses ranks instead of scores.
