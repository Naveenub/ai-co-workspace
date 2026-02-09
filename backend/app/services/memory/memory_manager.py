from app.services.memory.retriever import retrieve

class MemoryManager:
    def __init__(self):
        self.memories = []

    def add(self, memory: str):
        self.memories.append(memory)

    def query(self, query: str):
        return retrieve(1, query)
