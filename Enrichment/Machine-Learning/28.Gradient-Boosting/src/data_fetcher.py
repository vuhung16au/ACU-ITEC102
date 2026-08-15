import pandas as pd
import numpy as np
import requests

def get_housing_data():
    """
    Fetches Melbourne housing data (Regression).
    """
    try:
        url = "https://data.melbourne.vic.gov.au/api/v2/catalog/datasets/house-prices-by-small-area-sale-year/exports/csv"
        # The Melbourne housing data uses semicolon as separator
        df = pd.read_csv(url, sep=';', nrows=10000) 
        
        # Clean data
        df = df.dropna(subset=['median_price', 'sale_year', 'transaction_count'])
        
        # Encode categorical features
        df = pd.get_dummies(df, columns=['small_area', 'type'], drop_first=True)
        
        # Rename target column to 'price'
        df = df.rename(columns={'median_price': 'price'})
        return df
    except Exception as e:
        print(f"Could not fetch real housing data from data.gov.au. Using synthetic mock data. ({e})")
        return _generate_mock_housing_data()

def get_crash_data():
    """
    Fetches ACT Crash Data (Classification).
    Target: Predict if crash resulted in an injury (1) or just property damage (0).
    """
    try:
        url = "https://www.data.act.gov.au/api/v3/views/6jn4-m8rx/export.csv?accessType=DOWNLOAD"
        df = pd.read_csv(url, nrows=10000) 
        
        # Clean data
        df = df.dropna(subset=['LATITUDE', 'LONGITUDE', 'CRASH_SEVERITY'])
        
        # Target: 1 if Injury or Fatal, 0 if Property Damage Only
        df['is_injury'] = df['CRASH_SEVERITY'].apply(lambda x: 0 if 'property damage' in str(x).lower() else 1)
        
        # Features: extract hour from CRASH_TIME
        df['CRASH_TIME'] = pd.to_datetime(df['CRASH_TIME'], format='%H:%M', errors='coerce').dt.hour
        df['CRASH_TIME'] = df['CRASH_TIME'].fillna(12) # fill missing with noon
        
        # One-hot encode some conditions
        df = pd.get_dummies(df, columns=['LIGHTING_CONDITION', 'ROAD_CONDITION', 'WEATHER_CONDITION'], drop_first=True)
        
        # Drop columns not suitable for modeling directly
        cols_to_drop = ['CRASH_ID', 'CRASH_DATE', 'SUBURB_LOCATION', 'INTERSECTION', 'MIDBLOCK', 'CRASH_DIRECTION', 'CRASH_TYPE', 'CRASH_SEVERITY', 'Location']
        df = df.drop(columns=[c for c in cols_to_drop if c in df.columns])
        
        return df
    except Exception as e:
        print(f"Could not fetch real crash data from data.gov.au. Using synthetic mock data. ({e})")
        return _generate_mock_crash_data()


def _generate_mock_housing_data(n_samples=5000):
    np.random.seed(42)
    bedrooms = np.random.randint(1, 6, n_samples)
    bathrooms = np.minimum(np.random.randint(1, 4, n_samples), bedrooms + 1)
    distance_to_cbd = np.random.uniform(1.0, 50.0, n_samples)
    land_size = np.random.uniform(200, 1500, n_samples)
    
    base_price = 500000 
    price = (
        base_price + 
        (bedrooms * 150000) + 
        (bathrooms * 100000) - 
        (distance_to_cbd * 12000) + 
        (land_size * 500) +
        np.random.normal(0, 50000, n_samples)
    )
    
    return pd.DataFrame({
        'bedrooms': bedrooms,
        'bathrooms': bathrooms,
        'distance_to_cbd_km': distance_to_cbd,
        'land_size_sqm': land_size,
        'price': price
    })

def _generate_mock_crash_data(n_samples=5000):
    np.random.seed(42)
    latitude = np.random.uniform(-35.5, -35.1, n_samples)
    longitude = np.random.uniform(148.9, 149.3, n_samples)
    crash_time = np.random.randint(0, 24, n_samples)
    
    # Calculate probability of injury
    score = (crash_time / 24) * 2 - 1 + np.random.normal(0, 1, n_samples)
    prob_injury = 1 / (1 + np.exp(-score))
    is_injury = np.random.binomial(1, prob_injury)
    
    return pd.DataFrame({
        'LATITUDE': latitude,
        'LONGITUDE': longitude,
        'CRASH_TIME': crash_time,
        'is_injury': is_injury
    })

if __name__ == "__main__":
    df_houses = get_housing_data()
    print(f"Housing Data Sample:\n{df_houses.head()}\n")
    
    df_crash = get_crash_data()
    print(f"Crash Data Sample:\n{df_crash.head()}\n")
