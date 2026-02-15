from intent_classifier import classify_intent

def route(prompt):

    intent = classify_intent(prompt)

    if intent=="greeting":
        return "Hello. How can I assist with your research?"

    if intent=="nonsense":
        return "Input unclear. Please enter a valid research question."

    return None
