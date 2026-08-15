# Project 24: ML Model API

This project demonstrates how to serve a Machine Learning model using a RESTful API. We use Python with `scikit-learn` for the model training and `FastAPI` to expose the predictions as a web service.

## Screenshot(s) & Example Run 

```bash
curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "Make": "Toyota",
  "Engine_Size_L": 2.5,
  "Fuel_Type": "Hybrid",
  "Fuel_Consumption_L_100km": 5.0
}'
{"CO2_Emissions_g_km":114.24}%   
```

## Learning Objectives
1. Understand the basics of training a simple Machine Learning model (Random Forest Regressor).
2. Learn how to wrap an ML model in a REST API.
3. Understand how to handle incoming HTTP requests, process data, and return predictions.
4. Containerize a Python API with Docker.

## Data Source
- **Real Data**: The project is designed around the "Green Vehicle Guide" dataset from [data.gov.au](https://data.gov.au/dataset/ds-dga-05922d56-b333-4f51-8178-f71661cb1e92/details). It aims to predict CO2 Emissions based on vehicle features.
- **Fallback**: A synthetic dataset `data/mock_vehicles.csv` is provided if you cannot fetch the real data.

## See Also
- [QUICKSTART.md](QUICKSTART.md): Instructions on how to run and test the project.
- [docs/theory.md](docs/theory.md): Brief theoretical concepts.
- `images/`: Contains screenshots of the working project.
