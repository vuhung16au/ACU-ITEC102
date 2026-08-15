# Quickstart: Real-time Dashboard

Follow these instructions to run the Streamlit dashboard.

## Prerequisites
- Docker and Docker Compose installed.
- (Optional) `uv` installed to run Python tests locally.

## Running the Dashboard

To start the Streamlit application in a Docker container, run:

```bash
make up
```

This will build the Docker image and start the container. The application will be accessible at:
[http://localhost:8501](http://localhost:8501)

You can interact with the sidebar dropdowns to filter the flight data by origin and destination airports. The metrics and charts will update instantly thanks to DuckDB's fast execution.

## Running Tests

To verify the DuckDB data connection locally:

```bash
make test
```

## Stopping the Application

To stop the containers, run:

```bash
make down
```
