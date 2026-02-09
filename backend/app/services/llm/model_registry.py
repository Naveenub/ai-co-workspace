from app.services.llm.openai import OpenAIModel
from app.services.llm.ollama import OllamaModel

class LLMRegistry:
    def __init__(self):
        self.models = {
            "openai": OpenAIModel(),
            "ollama": OllamaModel()
        }

    def get_model(self, name: str):
        return self.models.get(name, None)

registry = LLMRegistry()
