"""A small support knowledge base, a retriever, and the prompt the system sends.

The corpus is section-level chunks of six help-center pages. Swap retrieve(),
build_prompt() and llm.ask() for your own system's hooks.
"""
from sentence_transformers import SentenceTransformer

CORPUS = [
    {"id": "refund-policy.md#Monthly plans",
     "text": "Monthly plans can be refunded within 30 days of the charge. "
             "After 30 days the current month is not refundable."},
    {"id": "refund-policy.md#How refunds are paid",
     "text": "Refunds go back to the original payment method and usually "
             "appear within 5 to 10 business days."},
    {"id": "refund-policy.md#Requesting a refund",
     "text": "To request a refund, open Billing, choose the charge, and "
             "select Request refund. Refund requests are reviewed within "
             "two business days."},
    {"id": "refund-policy.md#Partial refunds",
     "text": "Seats removed in the middle of a billing period are not "
             "refunded; the remaining time stays available until renewal."},
    {"id": "refund-policy.md#Annual plans",
     "text": "Annual subscriptions can be cancelled for a full refund within "
             "45 days of purchase. After that, cancellation stops the next "
             "renewal but the current year is not refunded."},
    {"id": "refund-policy.md#Exceptions",
     "text": "Charges disputed with your bank cannot also be refunded through "
             "Billing while the dispute is open."},
    {"id": "billing.md#Plans",
     "text": "Every plan is offered monthly or annually. Annual billing costs "
             "the same as ten months of the monthly price."},
    {"id": "billing.md#Renewals",
     "text": "Annual plans renew automatically on the purchase anniversary. "
             "We email a reminder 30 days before each annual renewal."},
    {"id": "billing.md#Switching plans",
     "text": "Switching from monthly to annual takes effect immediately, and "
             "the unused part of the month is credited to the annual charge."},
    {"id": "billing.md#Invoices",
     "text": "Invoices for every charge, monthly or annual, are available "
             "under Billing and can be downloaded as PDF."},
    {"id": "billing.md#Failed payments",
     "text": "If a renewal payment fails we retry it three times over seven "
             "days before the subscription is paused."},
    {"id": "account.md#Cancelling",
     "text": "You can cancel your plan at any time from Billing. Cancelling "
             "turns off renewal; the plan stays active until the end of the "
             "period you paid for."},
    {"id": "account.md#Deleting your account",
     "text": "Deleting your account removes all workspaces and cannot be "
             "undone. Cancel any active plan first."},
    {"id": "account.md#Changing the owner",
     "text": "The account owner can transfer ownership to another admin from "
             "Settings, under Members."},
    {"id": "security.md#Two-factor authentication",
     "text": "Turn on two-factor authentication from Settings to protect "
             "sign-in with a code from your phone."},
    {"id": "security.md#Sessions",
     "text": "Sessions expire after 30 days without activity, and you can "
             "sign out of every device from Settings."},
    {"id": "storage.md#Limits",
     "text": "Each workspace includes 100 GB of storage on monthly and annual "
             "plans alike."},
    {"id": "storage.md#Retention",
     "text": "Deleted files stay in the trash for 30 days before they are "
             "removed for good."},
]

_model = SentenceTransformer("all-MiniLM-L6-v2")
_emb = _model.encode([d["text"] for d in CORPUS], normalize_embeddings=True)


def retrieve(question, k):
    scores = _emb @ _model.encode(question, normalize_embeddings=True)
    order = sorted(range(len(CORPUS)), key=lambda i: -scores[i])[:k]
    return [{**CORPUS[i], "score": float(scores[i])} for i in order]


def build_prompt(question, passages):
    ctx = "\n\n".join(p["text"] for p in passages)
    return (
        "Answer using only the context below.\n\n"
        f"Context:\n{ctx}\n\n"
        f"Question: {question}"
    )
