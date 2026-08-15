from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.model import predict, train_model
import os

app = FastAPI(title="Green Vehicle CO2 Emissions API", description="API to predict CO2 emissions based on vehicle features.")

class VehicleFeatures(BaseModel):
    Make: str
    Engine_Size_L: float
    Fuel_Type: str
    Fuel_Consumption_L_100km: float

class PredictionResponse(BaseModel):
    CO2_Emissions_g_km: float

@app.on_event("startup")
def startup_event():
    # Train the model if it doesn't exist
    if not os.path.exists("data/model.joblib"):
        try:
            train_model()
        except Exception as e:
            print(f"Error during initial model training: {e}")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Green Vehicle CO2 Emissions API. Use /docs to see the available endpoints."}

@app.post("/predict", response_model=PredictionResponse)
def get_prediction(features: VehicleFeatures):
    try:
        prediction = predict(features.model_dump())
        return {"CO2_Emissions_g_km": prediction}
    except FileNotFoundError as e:
        raise HTTPException(status_code=503, detail="Model is currently training or unavailable.")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
