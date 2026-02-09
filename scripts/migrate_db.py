from app.db.base import Base
from app.db.session import engine

def migrate():
    Base.metadata.create_all(bind=engine)
    print("Database migrated successfully.")

if __name__ == "__main__":
    migrate()
