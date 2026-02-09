# Retrieval-Augmented Generation (RAG) Design

RAG enhances LLM answers with external context from vector stores.

## Flow

[User Query] 
│
▼ 
[API v1 RAG Endpoint] 
│
▼ 
[Semantic Retriever]
│
▼
[Vector Store: Chroma / Qdrant] 
│
▼ 
Top-K Relevant Context
│
▼
[Prompt Builder] 
│
▼ 
LLM (Ollama/OpenAI)
│
▼
[Final Answer]


## Key Components

1. **RAG Endpoint (`/api/v1/rag`)**  
   - Receives query and workspace ID  
   - Returns `context` + `answer`  

2. **Semantic Retriever**  
   - Converts query to embedding  
   - Searches vector store for relevant documents  

3. **Vector Stores**  
   - Chroma: lightweight local vector store  
   - Qdrant: high-performance vector search engine  

4. **Prompt Builder**  
   - Combines retrieved context and system rules  
   - Generates final LLM prompt

## Example

json
```
POST /api/v1/rag/
{
  "workspace_id": 1,
  "query": "Explain co-workspace architecture"
}

Response:
{
  "context": "Retrieved context for workspace 1...",
  "answer": "The AI Co-Workspace is built on FastAPI..."
}
```
