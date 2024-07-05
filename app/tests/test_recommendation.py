from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_recommendations():
    response = client.get("/recommendations/")
    assert response.status_code == 200
    assert len(response.json()) <= 10