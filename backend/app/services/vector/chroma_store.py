"""
Chroma vector store integration
Uses local pickled storage for prototyping
"""

import pickle
from pathlib import Path

STORE_PATH = Path(__file__).parent / "../../../vectorstore/chroma/embeddings.db"

class ChromaStore:
    def __init__(self):
        self.store = {}
        self.load()

    def add_vector(self, key: str, vector):
        self.store[key] = vector
        self.save()

    def get_vector(self, key: str):
        return self.store.get(key)

    def all_vectors(self):
        return self.store

    def save(self):
        STORE_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(STORE_PATH, "wb") as f:
            pickle.dump(self.store, f)

    def load(self):
        if STORE_PATH.exists():
            with open(STORE_PATH, "rb") as f:
                self.store = pickle.load(f)
        else:
            self.store = {}
