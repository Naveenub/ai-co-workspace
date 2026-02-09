# 🧠 AI Co-Workspace

**Claude-style AI co-workspace built for engineers.**
Persistent memory, artifact intelligence, transparent RAG, and multi-model LLM orchestration — designed for real project workflows, not just chat.

---

## ✨ Overview

AI Co-Workspace is an **open-source, workspace-centric AI platform** where conversations evolve into artifacts, artifacts become memory, and memory actively informs future reasoning.

Unlike traditional AI chat tools, this system treats **context as infrastructure** — observable, editable, and extensible.

Think **Claude Workspaces**, but:

* Open-source
* Multi-model
* Local-first
* RAG-transparent
* Engineer-controlled

---

## 🎯 Why This Project Exists

Modern LLM tools are powerful, but they:

* Forget long-running projects
* Hide how memory and context are selected
* Lock users into a single model
* Treat artifacts as disposable outputs
* Offer no observability or control

**AI Co-Workspace explores what an AI system looks like when memory, artifacts, and context are first-class, inspectable systems.**

---

## 🚀 Core Capabilities

### 🗂️ Workspace-First Design

Each workspace is fully isolated and owns:

* Chats
* Artifacts
* Files
* Memory
* Context rules

No cross-project contamination. No global memory leaks.

---

### 💬 Intelligent Chat System

* Workspace-scoped chat sessions
* Message history with summarization
* Streaming-ready API design
* Built for long-running collaboration

---

### 🧠 Persistent Memory (RAG-Powered)

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

### 📄 Artifact Intelligence

Artifacts are not just displayed — they are **understood**.

* Automatic artifact detection
* Artifact lifecycle:

  * Detect → Create → Update → Persist
* Artifacts feed memory and future reasoning
* Workspace-aware artifact management

---

### 🔌 Multi-Model LLM Support

Model-agnostic by design.

Supported:

* Ollama (local LLMs)
* OpenAI
* Extensible model registry

Switch models per workspace or task — no lock-in.

---

### 📊 Observability (Planned)

Designed for engineers who care about internals:

* Context inspection
* Retrieved memory visibility
* Token usage tracking
* Cost awareness

---

## 🆚 What This Has That Claude Workspaces Don’t

| Capability          | Claude | AI Co-Workspace |
| ------------------- | ------ | --------------- |
| Editable memory     | ❌      | ✅               |
| Transparent RAG     | ❌      | ✅               |
| Artifact lifecycle  | ❌      | ✅               |
| Multi-model support | ❌      | ✅               |
| Local LLMs          | ❌      | ✅               |
| Workspace export    | ❌      | ✅               |
| Extensible APIs     | ❌      | ✅               |

> Claude is a closed product.
> AI Co-Workspace is an **open platform**.

---

## 🏗️ Architecture Flow

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

## 📁 Repository Structure

```
ai-co-workspace/
├── backend/            # FastAPI backend
│   ├── app/
│   │   ├── api/        # REST APIs
│   │   ├── services/   # LLM, memory, RAG, artifacts
│   │   ├── db/         # SQLAlchemy models
│   │   └── core/       # Config, security, lifecycle
│   └── tests/
│
├── frontend/           # Next.js workspace UI
│
├── vectorstore/        # Chroma / Qdrant persistence
│
├── infra/              # Docker, Kubernetes, Terraform
│
├── docs/               # Architecture & design docs
│
└── scripts/            # Dev utilities & migrations
```

See `/docs` for deep dives into architecture, memory systems, and artifact lifecycle.

---

## 🛠️ Tech Stack

### Backend

* FastAPI
* SQLAlchemy
* Async service architecture
* Modular domain design

### LLMs

* Ollama (local-first)
* OpenAI
* Model registry abstraction

### Memory & RAG

* Chroma / Qdrant
* Embedding abstraction
* Semantic + keyword retrieval

### Frontend

* Next.js
* TailwindCSS
* Workspace-centric UI

### Infrastructure

* Docker & Docker Compose
* Kubernetes manifests
* Terraform modules

---

## 🧪 What This Project Is NOT

* ❌ Not an LLM training platform
* ❌ Not a fine-tuning pipeline
* ❌ Not a Claude UI clone
* ❌ Not tied to one vendor or cloud

This project focuses on **LLM orchestration, memory systems, and workspace intelligence**.

---

## 🗺️ MVP Execution Phases

1️⃣ Backend workspace & chat APIs
2️⃣ Ollama LLM integration
3️⃣ Prompt builder + memory retrieval
4️⃣ Artifact detection & lifecycle
5️⃣ Frontend workspace UI
6️⃣ Vector DB & semantic memory
7️⃣ Polishing, observability & docs

---

## 📦 Data Ownership & Portability

* Workspace export (JSON / Markdown)
* Local-first execution
* No vendor lock-in
* Your data, your models, your control

---

## 🤝 Who This Is For

* Cloud & DevOps engineers
* AI platform builders
* RAG system designers
* Open-source contributors
* Teams building serious, long-running AI projects

---

## 📜 License

MIT License — build freely, fork openly, ship boldly.

---

## 🧭 Roadmap Highlights

* Memory pinning & importance scoring
* Artifact versioning & diffs
* Context inspection UI
* Plugin & webhook system
* CI/CD & GitHub integrations

---

## ⭐ Final Note

This project isn’t about replacing Claude.

It answers a different question:

> **“What does an AI workspace look like when engineers control memory, context, and models?”**

---
