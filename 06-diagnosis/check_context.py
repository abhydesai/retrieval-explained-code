"""Checkpoint 3: does the evidence reach the prompt the system sends?"""
from support import build_prompt, retrieve

question = "What is the refund window for annual plans?"
results = retrieve(question, k=20)

prompt = build_prompt(question, results[:5])   # what the system actually sends
print("top 5, evidence in prompt:", "45 days" in prompt)

prompt = build_prompt(question, results[:10])  # widen the cutoff
print("top 10, evidence in prompt:", "45 days" in prompt)
