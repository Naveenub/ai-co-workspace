from app.services.memory.summarizer import summarize

def summarize_chat(messages: list[str]) -> str:
    return summarize(messages)
