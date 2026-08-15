import pandas as pd
from etl import transform

def test_transform_cleaning():
    mock_data = pd.DataFrame([
        {"name": " Valid Name ", "address": "  Some St  ", "capacity": -5, "lat": -33.0, "lng": 150.0},
        {"name": "Missing Coord", "address": "123 St", "capacity": 2, "lat": None, "lng": None}
    ])
    
    cleaned_df = transform(mock_data)
    
    # Missing coords should be dropped
    assert len(cleaned_df) == 1
    
    # Whitespace should be stripped
    assert cleaned_df.iloc[0]['name'] == "Valid Name"
    assert cleaned_df.iloc[0]['address'] == "Some St"
    
    # Invalid capacity should be zeroed
    assert cleaned_df.iloc[0]['capacity'] == 0
