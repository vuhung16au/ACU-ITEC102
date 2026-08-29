import pandas as pd
import numpy as np
import streamlit as st

@st.cache_data(show_spinner=False)
def generate_brand_comparison(df: pd.DataFrame) -> pd.DataFrame:
    """
    Computes average star rating and annual energy consumption per manufacturer.
    """
    if "Brand" not in df.columns:
        return pd.DataFrame()
        
    cols_to_agg = {}
    if "Star2009" in df.columns:
        cols_to_agg["Star2009"] = "mean"
    if "Labelled energy consumption (kWh/year)" in df.columns:
        cols_to_agg["Labelled energy consumption (kWh/year)"] = "mean"
        
    if not cols_to_agg:
        return pd.DataFrame()

    comparison = df.groupby("Brand").agg(cols_to_agg).reset_index()
    # Sort by Star2009 descending if available
    if "Star2009" in comparison.columns:
        comparison = comparison.sort_values(by="Star2009", ascending=False)
        
    return comparison

@st.cache_data(show_spinner=False)
def generate_efficiency_distribution(df: pd.DataFrame) -> pd.DataFrame:
    """
    Computes value counts across Efficiency_Tier.
    """
    if "Efficiency_Tier" not in df.columns:
        return pd.DataFrame()
        
    dist = df["Efficiency_Tier"].value_counts().reset_index()
    dist.columns = ["Efficiency_Tier", "Count"]
    return dist

@st.cache_data(show_spinner=False)
def generate_correlation_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """
    Computes correlation between appliance volume and energy consumption.
    """
    cols = ["Tot Vol", "Labelled energy consumption (kWh/year)", "Star2009", "Annual_Running_Cost_AUD"]
    available_cols = [c for c in cols if c in df.columns]
    
    if len(available_cols) < 2:
        return pd.DataFrame()
        
    return df[available_cols].corr()
