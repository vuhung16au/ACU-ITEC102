import pandas as pd
import numpy as np

np.random.seed(42)

stations = [
    {"name": "Sydney City Evie", "address": "123 George St, Sydney NSW 2000", "operator": "Evie", "capacity": 4, "lat": -33.8688, "lng": 151.2093},
    {"name": "Melbourne Central Chargefox", "address": "300 Lonsdale St, Melbourne VIC 3000", "operator": "Chargefox", "capacity": 6, "lat": -37.8115, "lng": 144.9632},
    {"name": "Brisbane Airport Tesla", "address": "Airport Dr, Brisbane Airport QLD 4008", "operator": "Tesla", "capacity": 8, "lat": -27.3888, "lng": 153.1189},
    {"name": "Perth CBD Ampol", "address": "150 St Georges Tce, Perth WA 6000", "operator": "Ampol", "capacity": 2, "lat": -31.9546, "lng": 115.8573},
    {"name": "Adelaide Jolt", "address": "Victoria Square, Adelaide SA 5000", "operator": "Jolt", "capacity": 2, "lat": -34.9285, "lng": 138.6007},
    # Intentionally missing/dirty data for ETL cleaning
    {"name": "Hobart Missing Coord", "address": "Salamanca Pl, Hobart TAS 7000", "operator": "Chargefox", "capacity": 2, "lat": None, "lng": None},
    {"name": "Darwin Fast", "address": "1 Mitchell St, Darwin NT 0800", "operator": "Evie", "capacity": 1, "lat": -12.4634, "lng": 130.8456},
    {"name": "Canberra Tesla Supercharger", "address": "Majura Park, Canberra ACT 2609", "operator": "Tesla", "capacity": 6, "lat": -35.3060, "lng": 149.1915},
    {"name": "Dirty Address Station", "address": "   404 Unknown St , Nowhere NSW 2999   ", "operator": "Jolt", "capacity": 4, "lat": -33.1, "lng": 150.1},
    {"name": "Invalid Capacity", "address": "100 Fake Rd, Sydney NSW 2000", "operator": "Evie", "capacity": -1, "lat": -33.8, "lng": 151.2},
]

df = pd.DataFrame(stations)
df.to_csv('data/mock_charging_stations.csv', index=False)
print("Mock data generated at data/mock_charging_stations.csv")
