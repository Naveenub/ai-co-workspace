# MVP Execution Flow

This file explains the recommended order for executing MVP phases.

## Phases

1️⃣ **Backend workspace + chat APIs**  
- Initialize FastAPI backend  
- Define database models, schemas, and routers  

2️⃣ **Ollama LLM integration**  
- Add stub LLM service  
- Support both Ollama and OpenAI  

3️⃣ **Prompt builder + memory retrieval**  
- Context builder for workspaces  
- Memory manager for chat summaries and lightweight recall  

4️⃣ **Artifact detection**  
- Artifact creation, updating, and retrieval  
- Artifact service with lifecycle support  

5️⃣ **Frontend workspace UI**  
- Workspace sidebar  
- Chat panel  
- Artifact editor  

6️⃣ **Vector DB memory (RAG)**  
- Chroma and Qdrant integration  
- Semantic retrieval for query context  

7️⃣ **Polishing + documentation**  
- Complete README, architecture diagrams, and API docs  
- Add tests, Docker, and scripts
