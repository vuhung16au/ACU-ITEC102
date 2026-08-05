import pytest
from src.main import generate_synthetic_data, analyze_data

def test_data_generation():
    df = generate_synthetic_data(1000)
    assert len(df) == 1000
    assert "state" in df.columns
    assert "fuel_type" in df.columns

def test_analysis():
    df = generate_synthetic_data(100)
    summary = analyze_data(df)
    assert len(summary) > 0
    assert "age_years" in summary.columns
