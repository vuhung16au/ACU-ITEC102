# Geospatial Data Visualizer

This project is a single-page Streamlit web application that fetches, cleans, and visualizes geospatial data on an interactive map. The educational objective is to demonstrate how to use `pandas` for data manipulation and `plotly.express.scatter_mapbox` for interactive map visualizations without requiring an API key.

## Learning Objectives
- Understanding data fetching and cleaning with `pandas`.
- Creating interactive map visualizations using `plotly.express`.
- Building single-page applications with `streamlit`.
- Handling data source toggling (Online vs Local Fallback).

## Features
- **Data Handler**: Fetches data from data.gov.au (Australian National Public Toilet Map) or a local CSV file, cleans coordinates, and coerces data types.
- **Plotly Map Engine**: Generates an interactive map using `carto-positron` mapbox style.
- **Streamlit UI**: Offers sidebar controls for data source and category filtering, a main map visualization, and a raw data expander.

See [QUICKSTART.md](QUICKSTART.md) for instructions on how to run this project.
Screenshots and screencasts can be found in the `images` directory.
