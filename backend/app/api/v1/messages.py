from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.models.message import Message
from app.schemas.message import MessageCreate, MessageOut
from app.api.deps import get_db

router = APIRouter()

@router.post("/", response_model=MessageOut)
def create_message(message: MessageCreate, db: Session = Depends(get_db)):
    db_message = Message(chat_id=message.chat_id, content=message.content, role=message.role)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

@router.get("/", response_model=List[MessageOut])
def list_messages(db: Session = Depends(get_db)):
    return db.query(Message).all()
