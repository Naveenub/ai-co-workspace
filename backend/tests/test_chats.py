from app.tasks.summarization import summarize_chat

def test_summarization():
    messages = ["Hello", "World"]
    summary = summarize_chat(messages)
    assert len(summary) > 0
