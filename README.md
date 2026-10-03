# Retrieval Explained — companion code

Runnable code for the **Retrieval Explained** video series. Every video that shows
code has its code here, in the exact form the video shows it: clone the repo, install the
folder's requirements, `cd` into the video's folder, and run the commands the video runs.

| Folder | Video |
|---|---|
| [`01-embeddings/`](./01-embeddings/) | 01, embeddings and vector search: embed a question, cosine similarity, exact and approximate search |
| [`02-chunking/`](./02-chunking/) | 02, chunking documents: a short travel policy and four ways to cut it |
| [`03-hybrid-search/`](./03-hybrid-search/) | 03, keyword, semantic and hybrid search over six passages |
| [`04-query-transformation/`](./04-query-transformation/) | 04, query transformation: rewriting, expansion and HyDE |
| [`05-reranking/`](./05-reranking/) | 05, reranking: a bi-encoder first stage and a cross-encoder second stage |
| [`06-diagnosis/`](./06-diagnosis/) | 06, diagnosing a bad answer through four checkpoints |

One folder per video, named for it. Each folder has its own README listing the commands the
video runs.

## Setup

Python 3.10 or newer. One virtual environment at the repo root serves every folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r 01-embeddings/requirements.txt   # or the folder you are working in
cd 01-embeddings
```

Videos 04 and 06 call a language model. Copy that folder's `.env.example` to `.env` and fill in
any OpenAI-compatible provider: a base URL, a model name and an API key. Never commit `.env`.

The embedding models download from Hugging Face on first use. Once they are downloaded, these
settings keep the library's progress bars and warnings out of the output:

```bash
export HF_HUB_OFFLINE=1 TRANSFORMERS_VERBOSITY=error HF_HUB_DISABLE_PROGRESS_BARS=1
```
