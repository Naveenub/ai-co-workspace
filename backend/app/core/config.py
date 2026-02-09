import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./dev.db"
    OPENAI_API_KEY: str = ""
    OLLAMA_MODEL_PATH: str = "./models"
    CHROMA_URL: str = "http://localhost:8001"
    QDRANT_URL: str = "http://localhost:6333"
    PORT: int = 8000
    DEBUG: bool = True

settings = Settings()
