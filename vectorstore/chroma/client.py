"""
Chroma Vector Store Client
Handles storing and retrieving embeddings using local pickle storage.
"""

import pickle
from pathlib import Path

STORE_PATH = Path(__file__).parent / "embeddings.db"

class ChromaStore:
    def __init__(self):
        self.store = {}
        self.load()

    def add_vector(self, key: str, vector):
        """Add a vector to the store."""
        self.store[key] = vector
        self.save()

    def get_vector(self, key: str):
        """Retrieve a vector from the store."""
        return self.store.get(key)

    def all_vectors(self):
        """Return all stored vectors."""
        return self.store

    def save(self):
        """Persist the store to disk."""
        STORE_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(STORE_PATH, "wb") as f:
            pickle.dump(self.store, f)

    def load(self):
        """Load the store from disk if exists."""
        if STORE_PATH.exists():
            with open(STORE_PATH, "rb") as f:
                self.store = pickle.load(f)
        else:
            self.store = {}
