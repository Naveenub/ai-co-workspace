from pydantic import BaseModel

class MemoryCreate(BaseModel):
    workspace_id: int
    content: str
    embedding: str

class MemoryOut(MemoryCreate):
    id: int

    class Config:
        orm_mode = True
