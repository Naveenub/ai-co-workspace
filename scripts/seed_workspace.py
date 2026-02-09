from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.db.models.workspace import Workspace

def seed():
    db: Session = SessionLocal()
    ws1 = Workspace(name="Dev Workspace", description="Testing AI co-workspace")
    ws2 = Workspace(name="Research Workspace", description="RAG experiments")
    db.add_all([ws1, ws2])
    db.commit()
    db.close()

if __name__ == "__main__":
    seed()
