# 06 — Diagnosing a bad answer

A support assistant gives a wrong or incomplete answer about the refund window for annual
plans. Four checkpoints find where the evidence was lost: in the corpus, in retrieval, in the
context sent to the model, or in generation.

| Command | What it shows |
|---|---|
| `python ask.py` | the system as it runs: the top 5 passages, and the model's answer from them |
| `python check_corpus.py` | the evidence is in the corpus |
| `python check_retrieval.py` | where retrieval ranks it among all the passages |
| `python check_context.py` | whether it reaches the prompt at a cutoff of 5, and of 10 |
| `python check_answer.py` | what the model answers given only the evidence, and given the top 10 |

`support.py` holds the corpus (section-level chunks of six help pages), the retriever and the
prompt. `ask.py` and `check_answer.py` call a language model: copy `.env.example` to `.env` and
fill in any OpenAI-compatible provider.
