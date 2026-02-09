from app.services.memory.semantic_retriever import semantic_search

def test_semantic_search():
    results = semantic_search("query")
    assert len(results) == 5
