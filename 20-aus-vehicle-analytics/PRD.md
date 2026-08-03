# Product Requirements Document (PRD)

## Main Purpose
Implement a Python project to analyse and visualize road vehicle registration data from Australia.
- **Analyse** road vehicle data from Australia.
- **Visualize** vehicle registrations over time to find interesting trends and insights.
- **Think deeply** about the data and provide insights that can be useful for decision-making or further research.

## Features & Target Insights
The dashboard should present the following insights:
1. **Motive Power Evolution**: A line chart showing vehicle registrations over time by `motive_power` (tracking the adoption of Electric/Hybrid vs. Petrol).
2. **Top Manufacturers**: A bar chart displaying the top 10 most popular vehicle makes/models.
3. **Vehicle Distribution**: A heatmap or stacked bar chart showing the distribution of `vehicle_type` against `motive_power`.
4. **Registration Trends**: Time-series showing the overall vehicle registrations over the years to track industry growth.

## Tech Stack
- **Language**: Python
- **Package Management**: `uv` (to manage dependencies and virtual environments)
- **Data Source**: CKAN API (`ckanapi`) fetching from `data.gov.au`
- **Data Processing**: `pandas` (for cleaning and manipulation)
- **Visualization & UI**: `streamlit` (for an interactive web dashboard) and `plotly` (for dynamic charts)

## Data Processing & Caching Strategy
- **Fetching**: The dataset has over 102,000 records. Fetching dynamically via API on every load is inefficient. The project will include a script to fetch all pages (using `limit` and `offset`) and save them locally.
- **Caching**: Store the fetched data as a local CSV or Parquet file in the `data/raw/` folder.
- **Cleaning**: Ensure fields like `year_of_manufacture` and `no_vehicles` (which come back as text strings from the API) are properly cast to integers/numerics. Handle missing or `"UNKNOWN"` values appropriately before visualization.

## Recommended Folder Structure
```text
.
├── data/                  # Local data storage
│   ├── raw/               # Fetched raw data from data.gov.au
│   └── processed/         # Cleaned data ready for analysis
├── notebooks/             # Jupyter notebooks for exploratory data analysis (EDA)
├── src/                   # Python source code
│   ├── fetch_data.py      # Script to download and cache the dataset
│   ├── clean_data.py      # Script to clean and format types
│   └── app.py             # Streamlit web dashboard application
├── QUICKSTART.md          # Setup guide
├── README.md              # Project description
├── PRD.md                 # Product Requirements Document
└── pyproject.toml         # uv project configuration
```

## Sample Data & API Reference
**Resource ID:** `dd3847ae-9c18-4750-9d35-3c5b7d03c49a`

**Sample Python Fetch Script:**
```python
from ckanapi import RemoteCKAN

# Connect to data.gov.au publicly
ckan = RemoteCKAN("https://data.gov.au")

# Fetch records from the DataStore resource
response = ckan.action.datastore_search(
    resource_id="dd3847ae-9c18-4750-9d35-3c5b7d03c49a",
    limit=5
)

# Print matching records
for record in response.get("records", []):
    print(record)
```

**Schema details:**
`_id` (int), `vehicle_type` (text), `year_of_manufacture` (text), `motive_power` (text), `make` (text), `model` (text), `no_vehicles` (text)