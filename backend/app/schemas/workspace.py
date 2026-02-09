from pydantic import BaseModel

class WorkspaceCreate(BaseModel):
    name: str
    description: str = ""

class WorkspaceOut(WorkspaceCreate):
    id: int

    class Config:
        orm_mode = True
