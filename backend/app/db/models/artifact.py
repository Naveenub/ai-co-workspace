from sqlalchemy import Column, Integer, String, ForeignKey, Text
from app.db.base import Base

class Artifact(Base):
    __tablename__ = "artifacts"

    id = Column(Integer, primary_key=True, index=True)
    workspace_id = Column(Integer, ForeignKey("workspaces.id"))
    title = Column(String)
    content = Column(Text)
    type = Column(String, default="text")
