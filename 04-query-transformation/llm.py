"""One function that sends a prompt to a language model and returns its reply.

Any OpenAI-compatible provider works: set LLM_BASE_URL, LLM_MODEL and
LLM_API_KEY in a .env file next to this one (see .env.example).
"""
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
    base_url=os.environ["LLM_BASE_URL"],
    api_key=os.environ["LLM_API_KEY"],
)


def ask(prompt):
    resp = client.chat.completions.create(
        model=os.environ["LLM_MODEL"],
        messages=[{"role": "user", "content": prompt}],
    )
    return resp.choices[0].message.content.strip()
