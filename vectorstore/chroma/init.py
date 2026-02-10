"""
Chroma VectorStore Package

Provides a local, pickle-based vector store for testing embeddings.
"""

from .client import ChromaStore

__all__ = ["ChromaStore"]
