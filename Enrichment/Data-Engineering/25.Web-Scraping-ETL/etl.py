import os
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values
import argparse

DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_NAME = os.environ.get("DB_NAME", "etl_db")
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASS = os.environ.get("DB_PASSWORD", "postgres")

def extract(file_path: str) -> pd.DataFrame:
    print(f"Extracting data from {file_path}...")
    df = pd.read_csv(file_path)
    return df

def transform(df: pd.DataFrame) -> pd.DataFrame:
    print("Transforming data...")
    # 1. Clean whitespace from strings
    df['name'] = df['name'].str.strip()
    df['address'] = df['address'].str.strip()
    
    # 2. Filter out missing coordinates
    initial_count = len(df)
    df = df.dropna(subset=['lat', 'lng'])
    print(f"  Dropped {initial_count - len(df)} rows due to missing coordinates.")
    
    # 3. Clean invalid capacity
    df['capacity'] = df['capacity'].fillna(0).astype(int)
    df.loc[df['capacity'] < 0, 'capacity'] = 0
    
    return df

def load(df: pd.DataFrame):
    print("Loading data into PostgreSQL...")
    conn = psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    cursor = conn.cursor()
    
    # Convert dataframe to list of tuples
    records = df[['name', 'address', 'operator', 'capacity', 'lat', 'lng']].values.tolist()
    
    insert_query = """
    INSERT INTO charging_stations (name, address, operator, capacity, lat, lng)
    VALUES %s
    """
    execute_values(cursor, insert_query, records)
    
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Successfully loaded {len(records)} records into the database.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', default='data/mock_charging_stations.csv', help='Path to the input CSV file')
    args = parser.parse_args()
    
    raw_data = extract(args.file)
    clean_data = transform(raw_data)
    load(clean_data)
