import pandas as pd
from ckanapi import RemoteCKAN

def fetch_all_records(resource_id):
    ckan = RemoteCKAN("https://data.gov.au/data")
    all_records = []
    limit = 10000
    offset = 0
    
    print(f"Fetching data for resource {resource_id}...")
    while True:
        print(f"Fetching from offset {offset}...")
        response = ckan.action.datastore_search(
            resource_id=resource_id,
            limit=limit,
            offset=offset
        )
        records = response.get("records", [])
        if not records:
            break
            
        all_records.extend(records)
        offset += limit
        
    print(f"Total records fetched: {len(all_records)}")
    return pd.DataFrame(all_records)

if __name__ == "__main__":
    resource_id = "dd3847ae-9c18-4750-9d35-3c5b7d03c49a"
    df = fetch_all_records(resource_id)
    import os
    os.makedirs("data/raw", exist_ok=True)
    df.to_csv("data/raw/vehicle_data.csv", index=False)
    print("Saved raw data to data/raw/vehicle_data.csv")
