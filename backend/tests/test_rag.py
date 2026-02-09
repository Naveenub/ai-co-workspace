from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_rag_query():
    response = client.post("/api/v1/rag/", json={"workspace_id":1,"query":"Hello AI"})
    assert response.status_code == 200
    data = response.json()
    assert "context" in data and "answer" in data
