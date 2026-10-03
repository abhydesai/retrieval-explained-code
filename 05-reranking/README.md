# 05 — Reranking search results

A fast first stage ranks candidates by embedding similarity; a cross-encoder then reads the
question and each candidate together and reorders them.

| Command | What it shows |
|---|---|
| `python first_stage.py` | four passages ranked by embedding similarity |
| `python rerank.py` | the same four reranked by a cross-encoder, the time it took, and whether the passage that answers the question is now first |

The reranker's margin on this example is small, and it depends on the wording of the
question: change the query and the order can change too. Treat it as an illustration of what a
cross-encoder does, and measure on your own questions before relying on it.
