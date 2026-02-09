class PromptBuilder:
    def build(self, system: str, user_input: str) -> str:
        return f"{system}\nUser: {user_input}\nAssistant:"
