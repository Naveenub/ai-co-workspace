from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.services.vector.vector_router import query_vectors
from app.db.models.memory import Memory
from app.api.deps import get_db

router = APIRouter()

@router.get("/query")
def query_rag(query: str, db: Session = Depends(get_db)):
    # Fetch top vector matches
    results = query_vectors(query)
    # Optionally store in memory
    return {"query": query, "results": results}
