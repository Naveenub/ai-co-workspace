from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Memory(Base):
    __tablename__ = "memorys"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String, default="")
