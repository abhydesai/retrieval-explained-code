# 05 — Reranking search results

A fast first stage ranks candidates by embedding similarity; a cross-encoder then reads the
question and each candidate together and reorders them.

| Command | What it shows |
|---|---|
| `python first_stage.py` | four passages ranked by embedding similarity |
| `python rerank.py` | the same four reranked by a cross-encoder |
| `python timing.py` | how long the cross-encoder takes for 4, 40, 400 and 4000 pairs |
| `python evaluate.py` | whether the passage that answers the question is in the top 1 and the top 4, before and after reranking |

The reranker's margin on this example is small, and it depends on the wording of the
question: change the query and the order can change too. Treat it as an illustration of what a
cross-encoder does, and measure on your own questions before relying on it.

`timing.py` repeats the four candidates to stand in for longer shortlists. The times depend on
your hardware and on batching; the number of pairs the model has to read does not.
