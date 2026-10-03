# RAG Search and Diagnosis — companion code

Runnable code for the **RAG Search and Diagnosis** video series. Every video that shows
code has its code here, in the exact form the video shows it: clone the repo, install the
folder's requirements, `cd` into the video's folder, and run the commands the video runs.

| Folder | What it holds |
|---|---|
| [`02-chunking/`](./02-chunking/) | Video 02, chunking documents for search: a short travel policy and four ways to cut it |

One folder per video, named for it. Folders for the other videos are added as those
videos are made.

## Setup

Python 3.10 or newer.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r 02-chunking/requirements.txt
cd 02-chunking
```
