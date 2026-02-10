"""
Embeddings generator
Converts text into numerical vectors for RAG retrieval
"""

from typing import List
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

class Embeddings:
    """
    Simple TF-IDF embeddings for prototype.
    Replace with OpenAI, SentenceTransformers, or Ollama embeddings for production.
    """
    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def fit(self, corpus: List[str]):
        self.vectorizer.fit(corpus)

    def encode(self, text: str):
        return self.vectorizer.transform([text]).toarray()[0]

    def encode_batch(self, texts: List[str]):
        return self.vectorizer.transform(texts).toarray()
