"""
Qdrant vector store integration
Placeholder for live Qdrant client connection
"""

class QdrantStore:
    def __init__(self):
        self.store = {}  # Placeholder dict for testing

    def add_vector(self, key: str, vector):
        self.store[key] = vector

    def get_vector(self, key: str):
        return self.store.get(key)

    def all_vectors(self):
        return self.store
