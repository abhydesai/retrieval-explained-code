"""The system as it runs: retrieve the top 5 passages and answer from them."""
from llm import ask
from support import build_prompt, retrieve

question = "What is the refund window for annual plans?"
results = retrieve(question, k=5)
print(ask(build_prompt(question, results)))
