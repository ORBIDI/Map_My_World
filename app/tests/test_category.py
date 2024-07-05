from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_category():
    response = client.post(
        "/categories/",
        json={"name": "Test Category","description": "Test Category"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Test Category"