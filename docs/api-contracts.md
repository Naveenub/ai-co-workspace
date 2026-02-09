# API Contracts

This document describes available API endpoints.

## Workspaces

- `POST /api/v1/workspaces/` → Create workspace  
- `GET /api/v1/workspaces/` → List workspaces  

## Chats

- `POST /api/v1/chats/` → Create chat  
- `GET /api/v1/chats/{workspace_id}` → List chats  

## Messages

- `POST /api/v1/messages/` → Send message  
- `GET /api/v1/messages/{chat_id}` → List messages  

## Artifacts

- `POST /api/v1/artifacts/` → Create artifact  
- `GET /api/v1/artifacts/{workspace_id}` → List artifacts  

## RAG

- `POST /api/v1/rag/` → Query RAG with semantic retrieval  
  json
  ```
  {
    "workspace_id": 1,
    "query": "Explain co-workspace architecture"
  }
```
