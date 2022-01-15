from .constants import PROMPTS


def read_prompts():
    with open(PROMPTS, "r") as f:
        data = f.readlines()
    return [d.strip() for d in data]
