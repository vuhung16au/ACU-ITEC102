# Quickstart: NoSQL Data Store

Follow these instructions to run the FastAPI application, MongoDB instance, and Mongo Express UI.

## Prerequisites
- Docker and Docker Compose installed.
- (Optional) `uv` installed to run Python tests locally.

## Running the Application

To start MongoDB, Mongo Express, and the FastAPI application, run:

```bash
make up
```

This will spin up three containers:
1. **MongoDB**: The core database running on port `27017`.
2. **Mongo Express**: A web-based administrative UI for MongoDB.
3. **FastAPI**: The REST API.

## Interacting with the Services

1. **FastAPI Swagger UI**:
   - Open your browser to [http://localhost:8002/docs](http://localhost:8002/docs)
   - You can test the endpoints (`/toilets`, `/toilets/accessible`, etc.) directly from this UI.

2. **Mongo Express**:
   - Open your browser to [http://localhost:8081](http://localhost:8081)
   - **Login**:
     - Username: `admin`
     - Password: `adminpassword`
   - You can browse the `nosql_db` database and the `toilets` collection to see the raw JSON documents.

## Running Tests

To verify the FastAPI logic locally without relying on the database:

```bash
make test
```

## Stopping the Application

To stop all containers, run:

```bash
make down
```
