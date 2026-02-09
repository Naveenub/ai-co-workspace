from app.services.vector.embeddings import embed_text
from app.services.vector.vector_router import store_in_chroma, store_in_qdrant

def embed_and_store(text: str, metadata: dict):
    vec = embed_text(text)
    store_in_chroma(vec, metadata)
    store_in_qdrant(vec, metadata)
    return vec
