from pydantic import BaseModel

class MessageCreate(BaseModel):
    chat_id: int
    content: str
    role: str

class MessageOut(MessageCreate):
    id: int
    created_at: str

    class Config:
        orm_mode = True
