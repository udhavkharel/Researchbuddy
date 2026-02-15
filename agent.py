import ollama
from config import MODEL_NAME,SYSTEM_PROMPT
from router import route
from db import save,load_history



def build_messages(user_prompt):

    history = load_history()

    messages=[{"role":"system","content":SYSTEM_PROMPT}]

    for role,msg in history:
        messages.append({"role":role,"content":msg})

    messages.append({"role":"user","content":user_prompt})

    return messages


def ask_llm(prompt):

    messages=build_messages(prompt)

    response = ollama.chat(
        model=MODEL_NAME,
        messages=messages
    )

    return response["message"]["content"]


def chat(prompt):

    routed = route(prompt)

    if routed:
        save("user",prompt)
        save("assistant",routed)
        return routed

    reply = ask_llm(prompt)

    save("user",prompt)
    save("assistant",reply)

    return reply


