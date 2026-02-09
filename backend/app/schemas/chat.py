from pydantic import BaseModel

class ChatCreate(BaseModel):
    workspace_id: int
    title: str

class ChatOut(ChatCreate):
    id: int

    class Config:
        orm_mode = True
