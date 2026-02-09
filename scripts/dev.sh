#!/bin/bash
# 🛠️ Development startup script

echo "Starting AI Co-Workspace development environment..."

# Start backend
echo "Starting backend..."
uvicorn backend.app.main:app --reload &

# Start frontend
echo "Starting frontend..."
cd frontend && npm run dev &

wait
