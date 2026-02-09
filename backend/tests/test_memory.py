from app.services.memory.memory_manager import MemoryManager

def test_memory_add_query():
    mem = MemoryManager()
    mem.add("Test memory")
    results = mem.query("Test")
    assert isinstance(results, list)
