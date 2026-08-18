import pytest
import pandas as pd
from app import load_data

def test_load_data_local():
    # Test loading local data
    df = load_data(source_type="Local")
    
    # Check if dataframe is not empty
    assert not df.empty
    
    # Check if required columns exist
    expected_columns = ['Name', 'Latitude', 'Longitude', 'Category']
    for col in expected_columns:
        assert col in df.columns
        
    # Check data types of coordinates
    assert pd.api.types.is_numeric_dtype(df['Latitude'])
    assert pd.api.types.is_numeric_dtype(df['Longitude'])
    
    # Check no NaN values in coordinates
    assert not df['Latitude'].isna().any()
    assert not df['Longitude'].isna().any()
