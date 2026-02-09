from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import workspaces, chats, messages, artifacts, rag, health
from app.db.base import Base
from app.db.session import engine

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Co-Workspace")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(workspaces.router, prefix="/api/v1/workspaces")
app.include_router(chats.router, prefix="/api/v1/chats")
app.include_router(messages.router, prefix="/api/v1/messages")
app.include_router(artifacts.router, prefix="/api/v1/artifacts")
app.include_router(rag.router, prefix="/api/v1/rag")
app.include_router(health.router, prefix="/api/v1/health")

@app.get("/")
def root():
    return {"message": "AI Co-Workspace Backend Running"}
