from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.models.workspace import Workspace
from app.schemas.workspace import WorkspaceCreate, WorkspaceOut
from app.api.deps import get_db

router = APIRouter()

@router.post("/", response_model=WorkspaceOut)
def create_workspace(workspace: WorkspaceCreate, db: Session = Depends(get_db)):
    db_workspace = Workspace(name=workspace.name, description=workspace.description)
    db.add(db_workspace)
    db.commit()
    db.refresh(db_workspace)
    return db_workspace

@router.get("/", response_model=List[WorkspaceOut])
def list_workspaces(db: Session = Depends(get_db)):
    return db.query(Workspace).all()
