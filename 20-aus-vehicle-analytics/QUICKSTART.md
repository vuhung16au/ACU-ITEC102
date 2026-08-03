# Quick Start

Follow these steps to set up and run the Aus-Vehicles Dashboard locally.

## Prerequisites
- Make sure you have `uv` and `make` installed on your machine.

## 1. Install Dependencies
Run the following command to sync the project dependencies:
```bash
make build
```

## 2. Fetch and Process Data
Download the data from the CKAN API and process it for the dashboard:
```bash
make data
```
This single command fetches the raw data (saving to `data/raw/vehicle_data.csv`) and processes it (saving to `data/processed/vehicle_data_clean.parquet`).

*(Alternatively, you can run `make fetch` and `make process` separately).*

## 3. Run the Dashboard
Launch the Streamlit app:
```bash
make run
```

## Cleaning Up
To reset your environment and delete downloaded data, run:
```bash
make clean
```
