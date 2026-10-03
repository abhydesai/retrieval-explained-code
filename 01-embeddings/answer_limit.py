"""Similar is not the same as answered: rank three passages for a pool question."""
from similarity import cosine, model

query = model.encode("Is the community pool open in winter?")

passages = [
    "The community pool is open daily in summer, 8am to 8pm.",
    "All outdoor facilities close from November through March.",
    "Yoga classes run every Tuesday evening in the main hall.",
]
vecs = model.encode(passages)

for text, v in zip(passages, vecs):
    print(f"{cosine(query, v):.2f}  {text}")
