# 02 — Chunking documents for search

`travel-policy.md` is the document every script cuts. Sizes are counted in characters, so
the boundaries are easy to see; real systems usually budget in tokens.

| Command | What it shows |
|---|---|
| `python split_fixed.py 100` | fixed-size chunks of 100 characters; one sentence is split across two chunks |
| `python split_fixed.py 1000` | one chunk holding the whole policy |
| `python split_fixed.py 100 --overlap 20` | 100-character windows that step forward 80 characters, so neighbours share 20 |
| `python split_sections.py` | a cut before every second-level heading: the title, then three whole sections |
| `python recursive_split.py` | headings first, with a 400-character budget; then the meals section alone with a budget of 100 |
| `python records.py` | each section as a record with an id, its source and its section, and an `embed_text` that leads with the title and heading |

`recursive_split.py` needs `langchain-text-splitters` (see `requirements.txt`); the other
scripts use only the standard library.
