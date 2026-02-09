from typing import List

class PromptContext:
    def __init__(self):
        self.contexts: List[str] = []

    def add_context(self, text: str):
        self.contexts.append(text)

    def get_context(self) -> str:
        return "\n".join(self.contexts)
