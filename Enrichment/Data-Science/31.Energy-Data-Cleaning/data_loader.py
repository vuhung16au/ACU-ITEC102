import pandas as pd
import requests
import io
import os
import streamlit as st

DATA_URL = "https://data.gov.au/data/dataset/559708e5-480e-4f94-8429-c49571e82761/resource/0eabca18-49bb-4a9e-8019-28d5d56501c4/download/rf_2026_08_18.csv"
LOCAL_PATH = os.path.join(os.path.dirname(__file__), "data", "sample_energy_data.csv")

@st.cache_data(show_spinner=False)
def load_raw_data(source_type: str) -> pd.DataFrame:
    """
    Fetches raw energy rating data from data.gov.au or local mock file.
    Includes Sentinel Null Replacement at ingestion time.
    """
    # Step 1: Ingestion & Sentinel Null Standardization
    na_sentinels = ["N/A", "-", "None", "", "Not Tested", "NAN", "nan"]
    
    if source_type == "Online":
        try:
            response = requests.get(DATA_URL, timeout=15)
            response.raise_for_status()
            df = pd.read_csv(io.StringIO(response.text), na_values=na_sentinels, low_memory=False)
        except Exception as e:
            st.error(f"Network error fetching online data: {e}. Falling back to Local data.")
            return load_raw_data("Local")
    else:
        df = pd.read_csv(LOCAL_PATH, na_values=na_sentinels, low_memory=False)
        
    return df
