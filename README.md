# 🧠 **AI Co-Workspace**

**Claude-style AI co-workspace built for engineers.**
Persistent memory, artifact intelligence, transparent RAG, and multi-model LLM orchestration — designed for real project workflows, not just chat.

---

## ✨ **Overview**

AI Co-Workspace is an **open-source, workspace-centric AI platform** where conversations evolve into artifacts, artifacts become memory, and memory actively informs future reasoning.

Unlike traditional AI chat tools, this system treats **context as infrastructure** — observable, editable, and extensible.

Think **Claude Workspaces**, but:

* Open-source
* Multi-model
* Local-first
* RAG-transparent
* Engineer-controlled

---

## 🎯 **Why This Project Exists**

Modern LLM tools are powerful, but they:

* Forget long-running projects
* Hide how memory and context are selected
* Lock users into a single model
* Treat artifacts as disposable outputs
* Offer no observability or control

**AI Co-Workspace explores what an AI system looks like when memory, artifacts, and context are first-class, inspectable systems.**

---

## 🚀 **Core Capabilities**

### 🗂️ Workspace-First Design

Each workspace is fully isolated and owns:

* Chats
* Artifacts
* Files
* Memory
* Context rules

No cross-project contamination. No global memory leaks.

---

### 💬 **Intelligent Chat System**

* Workspace-scoped chat sessions
* Message history with summarization
* Streaming-ready API design
* Built for long-running collaboration

---

### 🧠 **Persistent Memory (RAG-Powered)**

Memory is not magic — it’s **explicit and inspectable**.

Memory sources:

* Chat summaries
* Artifacts (code, docs, configs)
* Uploaded files

Retrieval:

* Keyword + semantic search
* Vector DB backed (Chroma / Qdrant)
* Workspace-scoped context injection

---

### 📄 **Artifact Intelligence**

Artifacts are not just displayed — they are **understood**.

* Automatic artifact detection
* Artifact lifecycle: ```Detect → Create → Update → Persist```
* Artifacts feed memory and future reasoning
* Workspace-aware artifact management

---

### 🔌 **Multi-Model LLM Support**

Model-agnostic by design.

Supported:

* Ollama (local LLMs)
* OpenAI
* Extensible model registry

Switch models per workspace or task — no lock-in.

---

### 📊 **Observability (Planned)**

Designed for engineers who care about internals:

* Context inspection
* Retrieved memory visibility
* Token usage tracking
* Cost awareness

---

## 🆚 **What This Has That Claude Workspaces Don’t**

| Capability             | Claude | AI Co-Workspace |
| ---------------------- | ------ | --------------- |
| Editable memory        | ❌     | ✅             |
| Transparent RAG        | ❌     | ✅             |
| Artifact lifecycle     | ❌     | ✅             |
| Multi-model support    | ❌     | ✅             |
| Local LLMs             | ❌     | ✅             |
| Workspace export       | ❌     | ✅             |
| Extensible APIs        | ❌     | ✅             |

> Claude is a closed product.
> AI Co-Workspace is an **open platform**.

---

## 🏗️ **Architecture Flow**

```
User Prompt
   ↓
Workspace Context Builder
   ↓
Memory Retrieval (RAG)
   ↓
Prompt Builder
   ↓
LLM (Ollama / OpenAI)
   ↓
Response
   ↓
Artifact Detection
   ↓
Memory Update
```

---

## 📁 **Repository Structure**

```
ai-co-workspace/
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
├── docker-compose.yml
├── Makefile
├── docs/
│   ├── architecture.md
│   ├── mvp-execution-flow.md
│   ├── memory-system.md
│   ├── rag-design.md              # 🆕 RAG explained clearly
│   ├── artifact-lifecycle.md
│   ├── api-contracts.md
│   └── screenshots/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── logging.py
│   │   │   ├── security.py
│   │   │   └── lifespan.py
│   │   ├── db/
│   │   │   ├── base.py
│   │   │   ├── session.py
│   │   │   └── models/
│   │   │       ├── workspace.py
│   │   │       ├── chat.py
│   │   │       ├── message.py
│   │   │       ├── artifact.py
│   │   │       └── memory.py
│   │   ├── schemas/
│   │   │   ├── workspace.py
│   │   │   ├── chat.py
│   │   │   ├── message.py
│   │   │   ├── artifact.py
│   │   │   └── memory.py
│   │   ├── api/
│   │   │   ├── deps.py
│   │   │   └── v1/
│   │   │       ├── workspaces.py
│   │   │       ├── chats.py
│   │   │       ├── messages.py
│   │   │       ├── artifacts.py
│   │   │       ├── files.py
│   │   │       ├── rag.py            # 🆕 RAG query endpoint
│   │   │       └── health.py
│   │   ├── services/
│   │   │   ├── llm/                  # PHASE 2
│   │   │   │   ├── base.py
│   │   │   │   ├── ollama.py
│   │   │   │   ├── openai.py
│   │   │   │   └── model_registry.py
│   │   │   ├── prompt/               # PHASE 3
│   │   │   │   ├── builder.py
│   │   │   │   ├── context.py
│   │   │   │   └── system_rules.py
│   │   │   ├── memory/               # MEMORY LAYER
│   │   │   │   ├── summarizer.py      # chat → summary
│   │   │   │   ├── retriever.py       # lightweight recall
│   │   │   │   ├── semantic_retriever.py  # 🆕 RAG core
│   │   │   │   └── memory_manager.py
│   │   │   ├── artifacts/            # PHASE 4
│   │   │   │   ├── detector.py
│   │   │   │   ├── creator.py
│   │   │   │   ├── updater.py
│   │   │   │   └── artifact_service.py
│   │   │   ├── vector/               # 🆕 RAG INFRA
│   │   │   │   ├── embeddings.py     # text → vector
│   │   │   │   ├── chroma_store.py
│   │   │   │   ├── qdrant_store.py
│   │   │   │   └── vector_router.py
│   │   │   └── workspaces/
│   │   │       ├── context_builder.py
│   │   │       └── permissions.py
│   │   ├── tasks/
│   │   │   ├── summarization.py
│   │   │   ├── embedding.py           # 🆕 background embedding
│   │   │   └── memory_cleanup.py
│   │   └── utils/
│   │       ├── token_counter.py
│   │       ├── text.py
│   │       └── time.py
│   ├── tests/
│   │   ├── test_workspaces.py
│   │   ├── test_chats.py
│   │   ├── test_artifacts.py
│   │   ├── test_memory.py
│   │   └── test_rag.py                # 🆕 RAG tests
│   └── requirements.txt
├── frontend/
│   ├── public/
│   │   └── index.html
|   ├── src/
│   │   ├── App.tsx
│   │   ├── index.tsx
│   │   ├── components/
│   │   │   ├── WorkspaceSidebar.tsx
│   │   │   ├── ChatPanel.tsx
│   │   │   ├── ArtifactEditor.tsx
│   │   │   ├── MarkdownViewer.tsx
│   │   │   └── MessageBubble.tsx
│   │   └── styles/
│   │       └── globals.css
│   ├── package.json
│   ├── tsconfig.json
│   └── tailwind.config.js
├── vectorstore/
│   ├── chroma/
│   │   ├── __init__.py
│   │   └── client.py        # pickle-based local store for testing
│   └── qdrant/
│       ├── __init__.py
│       └── client.py        # placeholder for live Qdrant integration
infra/
├── docker/
│   ├── backend.Dockerfile
│   ├── frontend.Dockerfile
│   └── ollama.Dockerfile
├── kubernetes/
│   ├── backend.yaml
│   ├── frontend.yaml
│   └── qdrant.yaml
└── terraform/
│       ├── aws/
│       │   ├── main.tf
│       │   ├── variables.tf
│       │   ├── outputs.tf
│       │   └── provider.tf
│       └── modules/
│           ├── network.tf
│           ├── db.tf
│           └── storage.tf
└── scripts/
    ├── seed_workspace.py
    ├── migrate_db.py
    └── dev.sh
```

---

## 🏗️ **ASCII Architecture Diagram**

```
                     Frontend UI
                 (Next.js Workspace)
                  ┌───────────────┐
                  │ Chat Panel    │
                  │ Artifact View │
                  │ Sidebar       │
                  └───────┬───────┘
                          │ REST / WebSocket
                          ▼
             ┌─────────────────────────┐
             │      Backend API        │
             │       (FastAPI)         │
             │ ┌───────────┐ ┌───────┐ │
             │ │ Chat API  │ │ RAG   │ │
             │ │ Artifact  │ │ API   │ │
             │ │ Workspace │ │ Files │ │
             │ └───────────┘ └───────┘ │
             └───────────┬─────────────┘
                         │
                         ▼
               ┌────────────────────┐
               │   Services Layer   │
               │ ┌────────────────┐ │
               │ │ Prompt Builder │ │
               │ │ Context Mgmt   │ │
               │ │ Memory Engine  │ │
               │ │ Artifact Eng   │ │
               │ │ Vector Router  │ │
               │ └────────────────┘ │
               └─────────┬──────────┘
                         │
                         ▼
            ┌─────────────────────────┐
            │ Memory & Vector Stores  │
            │ ┌───────────┐ ┌────────┐│
            │ │ SQL Memory│ │ Chroma ││
            │ │ Summaries │ │ Qdrant ││
            │ │ Artifacts │ │ Embeds ││
            │ └───────────┘ └────────┘│
            └────────────┬────────────┘
                         │
                         ▼
        ┌─────────────────────────────────┐
        │      LLM Providers              │
        │ ┌─────────────┐ ┌─────────────┐ │
        │ │    Ollama   │ │    OpenAI   │ │
        │ │    Local    │ │    Cloud    │ │
        │ │ Multi-Model │ │ Multi-Model │ |
        │ └─────────────┘ └─────────────┘ │
        └────────────────┬────────────────┘
                         │
                         ▼
            ┌─────────────────────────┐
            │ Artifact Detection &    │
            │ Memory Update           │
            │ - Auto-create / update  │
            │ - Feed memory & RAG     │
            └────────────┬────────────┘
                         │
                         ▼
               ┌────────────────────┐
               │ Background Tasks   │
               │ - Summarization    │
               │ - Embedding        │
               │ - Memory Cleanup   │
               └────────────────────┘
```

## 🛠️ **Tech Stack**

### **Backend**

* FastAPI
* SQLAlchemy
* Async service architecture
* Modular domain design

### **LLMs**

* Ollama (local-first)
* OpenAI
* Model registry abstraction

### **Memory & RAG**

* Chroma / Qdrant
* Embedding abstraction
* Semantic + keyword retrieval

### **Frontend**

* Next.js
* TailwindCSS
* Workspace-centric UI

### **Infrastructure**

* Docker & Docker Compose
* Kubernetes manifests
* Terraform modules

---

## 🧪 **What This Project Is NOT**

* ❌ Not an LLM training platform
* ❌ Not a fine-tuning pipeline
* ❌ Not a Claude UI clone
* ❌ Not tied to one vendor or cloud

This project focuses on **LLM orchestration, memory systems, and workspace intelligence**.

---

## 🗺️ **MVP Execution Phases**

1️⃣ Backend workspace & chat APIs
2️⃣ Ollama LLM integration
3️⃣ Prompt builder + memory retrieval
4️⃣ Artifact detection & lifecycle
5️⃣ Frontend workspace UI
6️⃣ Vector DB & semantic memory
7️⃣ Polishing, observability & docs

---

## 📦 **Data Ownership & Portability**

* Workspace export (JSON / Markdown)
* Local-first execution
* No vendor lock-in
* Your data, your models, your control

---

## 🤝 **Who This Is For**

* Cloud & DevOps engineers
* AI platform builders
* RAG system designers
* Open-source contributors
* Teams building serious, long-running AI projects

---

## 📜 **License**

MIT License

---

## 🧭 **Roadmap Highlights**

* Memory pinning & importance scoring
* Artifact versioning & diffs
* Context inspection UI
* Plugin & webhook system
* CI/CD & GitHub integrations

---

## ⭐ **Final Note**

This project isn’t about replacing Claude.

It answers a different question:

> **“What does an AI workspace look like when engineers control memory, context, and models?”**
