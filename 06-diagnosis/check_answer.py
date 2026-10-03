"""Checkpoint 4: given the evidence, does the model answer correctly?"""
from llm import ask
from support import build_prompt, retrieve

question = "What is the refund window for annual plans?"
results = retrieve(question, k=20)

evidence = next(p for p in results if "45 days" in p["text"])
print("evidence only:", ask(build_prompt(question, [evidence])))
print()
print("top 10:", ask(build_prompt(question, results[:10])))
