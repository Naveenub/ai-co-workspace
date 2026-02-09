from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.models.chat import Chat
from app.schemas.chat import ChatCreate, ChatOut
from app.api.deps import get_db

router = APIRouter()

@router.post("/", response_model=ChatOut)
def create_chat(chat: ChatCreate, db: Session = Depends(get_db)):
    db_chat = Chat(workspace_id=chat.workspace_id, title=chat.title)
    db.add(db_chat)
    db.commit()
    db.refresh(db_chat)
    return db_chat

@router.get("/", response_model=List[ChatOut])
def list_chats(db: Session = Depends(get_db)):
    return db.query(Chat).all()
