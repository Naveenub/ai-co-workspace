## AI Co-Workspace Architecture

This document explains the architecture of the AI Co-Workspace MVP.

## Overview

[Frontend React/Next.js UI]
│
▼
[FastAPI Backend API Layer]
├─ Workspaces API
├─ Chats API
├─ Messages API
├─ Artifacts API
└─ RAG API
│
▼
[Services Layer]
├─ LLM (Ollama / OpenAI)
├─ Prompt Builder
├─ Memory Management
├─ Artifacts Handler
└─ Vector Store Router (Chroma / Qdrant)
│
▼
[Database / Vector Stores]
├─ SQLite / PostgreSQL
├─ Chroma Vector Store
└─ Qdrant Vector Store

## Layers

1. **Frontend:** Interactive UI with workspace sidebar, chat panel, and artifact editor.  
2. **Backend API:** FastAPI endpoints for workspaces, chats, messages, artifacts, RAG queries, and health checks.  
3. **Services:**  
   - LLM integration (Ollama/OpenAI)  
   - Prompt building and system rules  
   - Memory retrieval and summarization  
   - Artifact lifecycle management  
   - Vector store routing for RAG  
4. **Database:**  
   - SQL database for structured data  
   - Vector stores for RAG semantic retrieval
