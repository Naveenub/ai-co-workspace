def store_in_qdrant(vector: list[float], metadata: dict):
    return {"status": "stored in Qdrant", "vector": vector, "metadata": metadata}
