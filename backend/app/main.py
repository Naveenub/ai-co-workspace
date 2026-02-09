from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import workspaces, chats, messages, artifacts, rag, health

app = FastAPI(title="AI Co-Workspace", version="1.0.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(workspaces.router, prefix="/api/v1/workspaces", tags=["Workspaces"])
app.include_router(chats.router, prefix="/api/v1/chats", tags=["Chats"])
app.include_router(messages.router, prefix="/api/v1/messages", tags=["Messages"])
app.include_router(artifacts.router, prefix="/api/v1/artifacts", tags=["Artifacts"])
app.include_router(rag.router, prefix="/api/v1/rag", tags=["RAG"])
app.include_router(health.router, prefix="/api/v1/health", tags=["Health"])
