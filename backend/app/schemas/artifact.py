from pydantic import BaseModel

class ArtifactCreate(BaseModel):
    workspace_id: int
    title: str
    content: str
    type: str = "text"

class ArtifactOut(ArtifactCreate):
    id: int

    class Config:
        orm_mode = True
