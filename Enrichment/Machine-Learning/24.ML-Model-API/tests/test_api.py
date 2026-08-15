from fastapi.testclient import TestClient
from app.main import app

def test_read_root():
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200
        assert "Welcome" in response.json()["message"]

def test_predict_endpoint():
    # Model should have been trained on startup, so predicting should work
    payload = {
        "Make": "Toyota",
        "Engine_Size_L": 2.5,
        "Fuel_Type": "Hybrid",
        "Fuel_Consumption_L_100km": 5.2
    }
    with TestClient(app) as client:
        response = client.post("/predict", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert "CO2_Emissions_g_km" in data
        assert isinstance(data["CO2_Emissions_g_km"], float)
