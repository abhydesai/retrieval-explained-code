"""Checkpoint 2: where does retrieval rank the evidence?"""
from support import retrieve

question = "What is the refund window for annual plans?"
results = retrieve(question, k=20)
for rank, p in enumerate(results, 1):
    mark = "  <-- evidence" if "45 days" in p["text"] else ""
    print(f"{rank:2d}  {p['score']:.3f}  {p['id']}{mark}")
