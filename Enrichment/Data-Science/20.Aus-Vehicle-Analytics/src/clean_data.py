import pandas as pd
import numpy as np

def clean_data(input_path, output_path):
    print(f"Loading raw data from {input_path}...")
    df = pd.read_csv(input_path)
    
    print("Cleaning data...")
    # Clean year_of_manufacture: Convert to numeric, errors='coerce' to turn 'UNKNOWN' to NaN
    df['year_of_manufacture'] = pd.to_numeric(df['year_of_manufacture'], errors='coerce')
    
    # Clean no_vehicles: Convert to numeric
    df['no_vehicles'] = pd.to_numeric(df['no_vehicles'], errors='coerce').fillna(0).astype(int)
    
    # Basic cleaning for strings
    string_cols = ['vehicle_type', 'motive_power', 'make', 'model']
    for col in string_cols:
        df[col] = df[col].astype(str).str.strip().str.upper()
    
    print(f"Saving cleaned data to {output_path}...")
    import os
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_parquet(output_path, index=False)
    print("Done!")

if __name__ == "__main__":
    clean_data("data/raw/vehicle_data.csv", "data/processed/vehicle_data_clean.parquet")
