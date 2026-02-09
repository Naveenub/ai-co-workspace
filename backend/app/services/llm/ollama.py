from app.services.llm.base import BaseLLM

class OllamaModel(BaseLLM):
    def generate(self, prompt: str) -> str:
        # Placeholder for Ollama integration
        return f"Ollama response for: {prompt}"
