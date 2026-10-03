"""First stage: rank four passages by embedding similarity (a bi-encoder)."""
from sentence_transformers import SentenceTransformer, util

query = (
    "I no longer have access to my email account - "
    "how can I reset my password?"
)

passages = [
    "To reset your password, click 'Forgot password' and follow "
    "the reset link we send to your email address.",
    "You can change which email notifications you receive from "
    "the account preferences page.",
    "If you can no longer receive email, contact support with "
    "your username. We will verify your identity and restore "
    "access to your account.",
    "Keep your account safe: use a strong, unique password and "
    "enable two-factor authentication.",
]


def first_stage():
    model = SentenceTransformer("all-MiniLM-L6-v2")
    scores = util.cos_sim(model.encode(query), model.encode(passages))[0]
    return sorted(zip(scores.tolist(), passages), reverse=True)


if __name__ == "__main__":
    for score, passage in first_stage():
        print(f"{score:.3f}  {passage[:60]}...")
