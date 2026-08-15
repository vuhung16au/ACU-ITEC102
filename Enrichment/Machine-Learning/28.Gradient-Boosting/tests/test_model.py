import pytest
import pandas as pd
import sys
import os

# Add src to path so we can import modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from data_fetcher import get_housing_data, get_crash_data

def test_housing_data_generation():
    df = get_housing_data()
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert 'price' in df.columns
    assert len(df) > 0

def test_crash_data_generation():
    df = get_crash_data()
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert 'is_injury' in df.columns
    assert 'LATITUDE' in df.columns
    assert len(df) > 0
    # ensure it's binary
    assert set(df['is_injury'].unique()).issubset({0, 1})
