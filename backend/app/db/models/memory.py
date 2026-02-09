from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.sql import func
from app.db.base import Base

class Memory(Base):
    __tablename__ = "memory"

    id = Column(Integer, primary_key=True, index=True)
    workspace_id = Column(Integer, ForeignKey("workspaces.id"))
    content = Column(Text)
    embedding = Column(Text)  # store vector embedding as JSON
    created_at = Column(DateTime(timezone=True), server_default=func.now())
