import re

GREETINGS = ["hi","hello","hey","good morning","good evening"]

COMMANDS = [
    "write","generate","create","build",
    "summarize","explain","list","define","show"
]

RESEARCH_TERMS = [
    "research","paper","method","dataset",
    "model","algorithm","theory","experiment",
    "evaluation","nlp","ai","tokenization"
]


def classify_intent(text:str)->str:
    t=text.lower().strip()

    if any(g in t for g in GREETINGS):
        return "greeting"

    if any(t.startswith(c) for c in COMMANDS):
        return "command"

    if any(w in t for w in RESEARCH_TERMS) or "?" in t:
        return "research"

    if len(t)<3:
        return "nonsense"

    if not re.search("[a-zA-Z]",t):
        return "nonsense"

    return "general"
