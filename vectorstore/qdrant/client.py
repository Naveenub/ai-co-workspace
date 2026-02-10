"""
Qdrant Vector Store Client
Placeholder implementation for live Qdrant integration.
"""

class QdrantStore:
    def __init__(self):
        self.store = {}  # Temporary placeholder dict

    def add_vector(self, key: str, vector):
        """Add a vector to the store."""
        self.store[key] = vector

    def get_vector(self, key: str):
        """Retrieve a vector from the store."""
        return self.store.get(key)

    def all_vectors(self):
        """Return all stored vectors."""
        return self.store
