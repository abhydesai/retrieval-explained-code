# 01 — Embeddings and vector search

A small local embedding model (`all-MiniLM-L6-v2`) turns text into 384 numbers; cosine
similarity scores how closely two of those vectors point the same way; search ranks passages by
that score, exactly or through an approximate index.

| Command | What it shows |
|---|---|
| `python embed.py` | a question becomes a vector of 384 numbers |
| `python similarity.py` | cosine similarity between the question and three passages |
| `python exact_search.py` | exact search: score every passage, sort, keep the top two |
| `python ann_search.py` | the same search through an HNSW index, built before the query arrives |
| `python answer_limit.py` | a pool question whose most similar passage does not answer it |

The first run downloads the model (about 90 MB).
