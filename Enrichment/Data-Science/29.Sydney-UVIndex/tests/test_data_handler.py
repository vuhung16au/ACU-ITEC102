import pytest
import pandas as pd
from data_handler import fetch_and_process_data

def test_fetch_and_process_data_offline():
    # Test offline data loading
    df = fetch_and_process_data(source="offline")
    
    # Check if dataframe is not empty
    assert not df.empty
    
    # Check if index is DatetimeIndex
    assert isinstance(df.index, pd.DatetimeIndex)
    
    # Check expected columns exist
    expected_columns = ['UV_Index', 'Lat', 'Lon']
    for col in expected_columns:
        assert col in df.columns
        
    # Check data types
    assert pd.api.types.is_numeric_dtype(df['UV_Index'])
    assert pd.api.types.is_numeric_dtype(df['Lat'])
    assert pd.api.types.is_numeric_dtype(df['Lon'])
