from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_location():
    response = client.post(
        "/locations/",        
        json={
        "name": "Museo de la Plata",
        "description": "Museo de la Plata.",
        "latitude": 4.602222928504023, 
        "longitude": -74.07197673184034,
        "category_id": 3
        }
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Test Location"