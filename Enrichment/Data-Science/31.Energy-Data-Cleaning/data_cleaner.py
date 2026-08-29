import pandas as pd
import numpy as np
import streamlit as st

def sum_multivalue_volumes(val):
    if pd.isna(val):
        return np.nan
    try:
        return sum(float(x.strip()) for x in str(val).split(",") if x.strip())
    except ValueError:
        return np.nan

@st.cache_data(show_spinner=False)
def clean_energy_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Applies the full sequence of data cleaning techniques on the raw DataFrame.
    """
    # Create a copy so we don't modify the cached raw dataframe
    clean_df = df.copy()

    # Step 2: String Trimming and Normalization
    if "Brand" in clean_df.columns:
        clean_df["Brand"] = clean_df["Brand"].astype(str).str.strip().str.upper()
        # The ingestion step (na_values) already replaces "NAN" if it matches, 
        # but just in case pandas astype(str) casts true np.nan to "NAN":
        clean_df["Brand"] = clean_df["Brand"].replace({"NAN": np.nan, "NAN ": np.nan})

    # Step 3: Parsing Multi-Value Numeric Columns
    for col in ["CompartGrVol", "CompartNetVol"]:
        if col in clean_df.columns:
            clean_df[f"{col}_Parsed"] = clean_df[col].apply(sum_multivalue_volumes)

    # Step 4: Safe Type Coercion for Analytical Columns
    numeric_cols = [
        "Labelled energy consumption (kWh/year)",
        "Height",
        "Width",
        "Depth",
        "Tot Vol",
        "Star2009",
        "SRI2009",
    ]
    for col in numeric_cols:
        if col in clean_df.columns:
            clean_df[col] = pd.to_numeric(clean_df[col], errors="coerce").astype(np.float64)

    # Step 5: Advanced NumPy Conditional Logic and Feature Engineering
    
    # 5.1 Calculate estimated annual running cost
    ELECTRICITY_RATE_PER_KWH = 0.30
    if "Labelled energy consumption (kWh/year)" in clean_df.columns:
        clean_df["Annual_Running_Cost_AUD"] = (
            clean_df["Labelled energy consumption (kWh/year)"] * ELECTRICITY_RATE_PER_KWH
        )
    
    # 5.2 Categorization using np.select
    if "Star2009" in clean_df.columns:
        conditions = [
            clean_df["Star2009"] >= 4.0,
            (clean_df["Star2009"] >= 2.5) & (clean_df["Star2009"] < 4.0),
            clean_df["Star2009"] < 2.5,
        ]
        choices = ["High Efficiency", "Moderate Efficiency", "Low Efficiency"]
        clean_df["Efficiency_Tier"] = np.select(conditions, choices, default="Unrated")
        # Ensure np.nan in Star2009 are also 'Unrated'
        clean_df.loc[clean_df["Star2009"].isna(), "Efficiency_Tier"] = "Unrated"

    # 5.3 Validity Flag using np.where
    if all(col in clean_df.columns for col in ["Height", "Width", "Depth"]):
        clean_df["Valid_Dimensions"] = np.where(
            (clean_df["Height"] > 300) & (clean_df["Width"] > 200) & (clean_df["Depth"] > 200),
            True,
            False,
        )

    return clean_df
