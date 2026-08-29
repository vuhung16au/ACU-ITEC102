import pytest
import pandas as pd
import numpy as np
from data_loader import load_raw_data
from data_cleaner import clean_energy_data

def test_clean_energy_data():
    raw_df = load_raw_data(source_type="Local")
    assert not raw_df.empty, "Failed to load raw mock data"
    
    clean_df = clean_energy_data(raw_df)
    
    # 1. Null Integrity: The N/A and - should be parsed as True under .isna()
    assert clean_df["Labelled energy consumption (kWh/year)"].isna().sum() > 0, "Failed to capture nulls in consumption"
    
    # 2. Type Safety
    assert clean_df["Labelled energy consumption (kWh/year)"].dtype == np.float64
    assert clean_df["Height"].dtype == np.float64
    assert clean_df["Star2009"].dtype == np.float64
    
    # 3. Brand Consistency
    # We started with "FISHER & PAYKEL ", "Fisher & Paykel", " SAMSUNG", "SAMSUNG", "WHIRLPOOL", "Whirlpool ", "LG"
    # Should reduce down to unique uppercase trimmed versions
    unique_brands = clean_df["Brand"].dropna().unique()
    assert "FISHER & PAYKEL" in unique_brands
    assert "SAMSUNG" in unique_brands
    assert "WHIRLPOOL" in unique_brands
    assert "LG" in unique_brands
    assert len(unique_brands) == 4, f"Brand cleanup failed, found {unique_brands}"
    
    # 4. Parsing Multi-Value Numeric Columns
    # "243.0,97.0" -> 340.0
    assert "CompartGrVol_Parsed" in clean_df.columns
    # Check that at least some parsing happened
    assert clean_df["CompartGrVol_Parsed"].max() > 0
    
    # 5. Conditional Logic
    assert "Efficiency_Tier" in clean_df.columns
    assert "Annual_Running_Cost_AUD" in clean_df.columns
    assert "Valid_Dimensions" in clean_df.columns
    
    # Check LG row which had Height = -100
    lg_mask = clean_df["Brand"] == "LG"
    assert not clean_df.loc[lg_mask, "Valid_Dimensions"].iloc[0]
