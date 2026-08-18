import pandas as pd
import streamlit as st
import requests
import io
import os

LIVE_URL = "https://data.gov.au/data/dataset/c31a759c-a4d4-455f-87a7-98576be14f11/resource/d39c41e0-e36d-47f3-b382-2ba9b0950963/download/uv-sydney-2007.csv"

@st.cache_data
def fetch_and_process_data(source="offline"):
    """
    Fetches and processes UV Index data.
    `source` can be 'online' or 'offline'.
    """
    if source == "online":
        try:
            # We set a timeout so the app doesn't hang forever
            response = requests.get(LIVE_URL, timeout=10)
            response.raise_for_status()
            df = pd.read_csv(io.StringIO(response.text))
        except Exception as e:
            st.error(f"Failed to fetch live data: {e}. Falling back to offline mode.")
            return fetch_and_process_data(source="offline")
    else:
        # Load local mock dataset
        filepath = os.path.join(os.path.dirname(__file__), 'data', 'sample_uv.csv')
        df = pd.read_csv(filepath)

    # Data Cleaning
    df['Date-Time'] = pd.to_datetime(df['Date-Time'])
    
    # Ensure correctly typed
    for col in ['UV_Index', 'Lat', 'Lon']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # Set index
    df = df.set_index('Date-Time')
    
    # Sort the index to ensure chronological order
    df = df.sort_index()
    
    return df
