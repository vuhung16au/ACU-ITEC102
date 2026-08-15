from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import os

app = FastAPI(title="NoSQL Public Toilet API")

MONGO_URI = os.environ.get("MONGO_URI", "mongodb://root:rootpassword@localhost:27017")
client = MongoClient(MONGO_URI)
db = client.nosql_db
collection = db.toilets

class ToiletFeature(BaseModel):
    type: str
    geometry: Dict[str, Any]
    properties: Dict[str, Any]

@app.get("/")
def read_root():
    return {"message": "Welcome to the NoSQL Public Toilet API. Access /docs for endpoints."}

@app.get("/toilets", response_model=List[ToiletFeature])
def get_toilets(limit: int = 10, skip: int = 0):
    toilets = list(collection.find({}, {"_id": 0}).skip(skip).limit(limit))
    return toilets

@app.get("/toilets/accessible", response_model=List[ToiletFeature])
def get_accessible_toilets():
    query = {"properties.features.accessible": True}
    toilets = list(collection.find(query, {"_id": 0}))
    return toilets

@app.post("/toilets", response_model=Dict[str, str])
def add_toilet(toilet: ToiletFeature):
    result = collection.insert_one(toilet.model_dump())
    if result.inserted_id:
        return {"status": "success", "message": "Toilet added successfully."}
    raise HTTPException(status_code=500, detail="Failed to add toilet.")
