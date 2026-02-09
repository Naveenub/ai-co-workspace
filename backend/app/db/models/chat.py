from sqlalchemy import Column, Integer, String
from app.db.base import Base

class chat(Base):
    __tablename__ = "chat"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String, default="")
