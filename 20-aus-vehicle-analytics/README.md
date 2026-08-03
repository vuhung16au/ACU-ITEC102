# Aus-Vehicles

A Python data analysis and visualization project exploring Australian road vehicle registrations.

## Overview
This project connects to the `data.gov.au` CKAN API to download vehicle registration data. It cleans and processes this data using `pandas`, and serves an interactive web dashboard built with `streamlit` and `plotly`.

## Features
- **Motive Power Evolution**: Tracks the adoption of Electric and Hybrid vehicles versus Petrol.
- **Top Manufacturers**: Visualizes the top 10 most popular vehicle makes in the dataset.
- **Vehicle Distribution**: Analyzes vehicle types against motive power in a stacked bar chart.
- **Registration Trends**: Displays the overall time-series growth of vehicle registrations over the years.

## Folder Structure
- `data/raw/`: Raw downloaded CSV data.
- `data/processed/`: Cleaned Parquet files.
- `src/fetch_data.py`: Script to download data via CKAN API.
- `src/clean_data.py`: Script to parse text fields to numerics and handle missing values.
- `src/app.py`: Streamlit dashboard.

Please refer to `QUICKSTART.md` for detailed instructions. In short, you can use the provided Makefile:
- `make build`: Install dependencies
- `make data`: Fetch and process the vehicle data
- `make run`: Launch the interactive dashboard
- `make clean`: Clean up the environment and downloaded data
