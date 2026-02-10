"""
Vector Router
Abstracts multiple vector stores (Chroma, Qdrant)
"""

from .chroma_store import ChromaStore
from .qdrant_store import QdrantStore
from .embeddings import Embeddings

class VectorRouter:
    def __init__(self, store_type="chroma"):
        self.embeddings = Embeddings()
        if store_type == "qdrant":
            self.store = QdrantStore()
        else:
            self.store = ChromaStore()

    def add(self, key: str, text: str):
        vector = self.embeddings.encode(text)
        self.store.add_vector(key, vector)

    def get(self, key: str):
        return self.store.get_vector(key)

    def encode(self, text: str):
        return self.embeddings.encode(text)

    def encode_batch(self, texts: list):
        return self.embeddings.encode_batch(texts)

    def all(self):
        return self.store.all_vectors()
