from app.db.session import SessionLocal
from app.db.models.workspace import Workspace

def seed():
    db = SessionLocal()
    ws = Workspace(name="Default Workspace")
    db.add(ws)
    db.commit()
    db.close()
    print("Seeded default workspace.")

if __name__ == "__main__":
    seed()
