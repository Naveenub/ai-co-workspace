# Memory System

The AI Co-Workspace memory system stores chat history, summaries, and semantic embeddings for RAG.

## Components

1. **Summarizer**  
   - Converts chat threads into concise summaries  
   - Reduces context size for LLM calls  

2. **Retriever**  
   - Fetches relevant past messages or artifacts  
   - Supports lightweight recall  

3. **Semantic Retriever (RAG core)**  
   - Uses embeddings and vector search (Chroma / Qdrant)  
   - Provides top-K relevant context for queries  

4. **Memory Manager**  
   - Orchestrates storing, retrieving, and updating memory  
   - Interfaces with database and vector stores

## Flow

[New Chat] 
│
▼ 
[Summarizer] 
│
▼ 
[Memory Manager]
│
▼
[Retriever / Semantic Retriever] 
│
▼ 
[LLM Prompt]
