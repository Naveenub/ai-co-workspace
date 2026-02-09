.PHONY: help backend frontend build up down seed test

help:
	@echo "Usage:"
	@echo "  make backend       - Run backend server"
	@echo "  make frontend      - Run frontend server"
	@echo "  make build         - Build all docker images"
	@echo "  make up            - Start all containers"
	@echo "  make down          - Stop all containers"
	@echo "  make seed          - Seed database with sample workspaces"
	@echo "  make test          - Run backend tests"

backend:
	uvicorn backend.app.main:app --reload --port 8000

frontend:
	cd frontend && npm install && npm run dev

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

seed:
	python scripts/seed_workspace.py

test:
	pytest backend/tests/
