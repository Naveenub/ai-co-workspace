from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.models.artifact import Artifact
from app.schemas.artifact import ArtifactCreate, ArtifactOut
from app.api.deps import get_db

router = APIRouter()

@router.post("/", response_model=ArtifactOut)
def create_artifact(artifact: ArtifactCreate, db: Session = Depends(get_db)):
    db_artifact = Artifact(
        workspace_id=artifact.workspace_id,
        title=artifact.title,
        content=artifact.content,
        type=artifact.type
    )
    db.add(db_artifact)
    db.commit()
    db.refresh(db_artifact)
    return db_artifact

@router.get("/", response_model=List[ArtifactOut])
def list_artifacts(db: Session = Depends(get_db)):
    return db.query(Artifact).all()
