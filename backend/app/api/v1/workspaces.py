from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models.workspace import Workspace
from app.schemas.workspace import WorkspaceCreate, Workspace as WorkspaceSchema

router = APIRouter()

@router.post("/", response_model=WorkspaceSchema)
def create_workspace(workspace: WorkspaceCreate, db: Session = Depends(get_db)):
    db_ws = Workspace(name=workspace.name, description=workspace.description)
    db.add(db_ws)
    db.commit()
    db.refresh(db_ws)
    return db_ws

@router.get("/", response_model=list[WorkspaceSchema])
def list_workspaces(db: Session = Depends(get_db)):
    return db.query(Workspace).all()
