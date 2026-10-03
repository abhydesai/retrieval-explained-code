"""Turn a question into a vector with a small local embedding model."""
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

vec = model.encode("How do I reset my password?")
print(vec.shape)
print(vec[:4])
