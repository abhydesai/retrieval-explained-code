# 04 — Query transformation

A casual question searches badly against documentation-style notes. Three ways to change what
goes into the search: rewrite the question, expand it into several queries, or generate a
hypothetical answer and search with that (HyDE).

| Command | What it shows |
|---|---|
| `python baseline.py` | the question searched exactly as typed |
| `python rewrite.py` | one rewritten query, and what it retrieves |
| `python expand.py` | several alternative queries, searched separately and merged |
| `python hyde.py` | a generated hypothetical answer used as the search query |
| `python evaluate.py` | how many of the two labeled answer passages each input retrieves |

`corpus.py` holds the ten notes and a semantic retriever over them. The scripts other than
`baseline.py` call a language model: copy `.env.example` to `.env` and fill in any
OpenAI-compatible provider. Model output varies from run to run, so your rewrites and counts
may differ from the video's.
