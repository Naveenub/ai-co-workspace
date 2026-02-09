import openai
from app.core.config import settings
from app.services.llm.base import BaseLLM

openai.api_key = settings.OPENAI_API_KEY

class OpenAIModel(BaseLLM):
    def generate(self, prompt: str) -> str:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
