# Quickstart: ML Model API

Follow these instructions to run and test the API.

## Prerequisites
- Docker and Docker Compose installed.
- (Optional) `uv` installed for local testing.

## Running the Application

To start the API in a Docker container, run:

```bash
make up
```

This will build the Docker image and start the container on port `8000`. Wait a few moments for the model to train upon the first startup.

## Interacting with the API

You can access the auto-generated API documentation (Swagger UI) by navigating to:
[http://localhost:8000/docs](http://localhost:8000/docs)

From there, you can test the `/predict` endpoint interactively.

Alternatively, test it via `curl`:
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
```

## Running Tests

If you have `uv` and Python installed, you can run the unit tests locally:

```bash
make test
```

## Stopping the Application

To stop the containers, run:

```bash
make down
```
