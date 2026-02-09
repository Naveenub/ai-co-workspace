from .embeddings import embed_text
from .chroma_store import store_in_chroma
from .qdrant_store import store_in_qdrant

def query_vectors(query: str):
    vec = embed_text(query)
    # Just return simulated results
    store_in_chroma(vec, {"query": query})
    store_in_qdrant(vec, {"query": query})
    return [f"Result {i+1} for '{query}'" for i in range(3)]
