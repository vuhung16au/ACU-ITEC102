# Tech Stack

This project utilizes the following technologies for fetching, processing, and visualizing the data:

- **Streamlit**: A fast and easy way to build and share data applications. It is used as the core framework for creating the interactive web dashboard for vehicle analytics.
- **CKANAPI**: A Python package for accessing CKAN data portals. It is used to programmatically fetch the Road Vehicles Australia dataset from the `data.gov.au` open data portal.
- **Plotly**: A graphing library for making interactive, publication-quality graphs. It is used to create interactive charts and visualizations within the Streamlit app.
- **PyArrow**: A cross-language development platform for in-memory data. It is used in this project to efficiently read, process, and handle large tabular datasets (like Parquet files or large CSVs) quickly and with low memory overhead.
