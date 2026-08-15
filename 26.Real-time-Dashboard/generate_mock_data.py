import pandas as pd
import numpy as np

np.random.seed(42)

# Generate 5 years of daily flight data
dates = pd.date_range(start='2019-01-01', end='2023-12-31', freq='D')
routes = [
    ('SYD', 'MEL'), ('MEL', 'SYD'),
    ('SYD', 'BNE'), ('BNE', 'SYD'),
    ('MEL', 'BNE'), ('BNE', 'MEL'),
    ('SYD', 'PER'), ('PER', 'SYD'),
    ('MEL', 'PER'), ('PER', 'MEL'),
    ('SYD', 'ADL'), ('ADL', 'SYD'),
    ('MEL', 'ADL'), ('ADL', 'MEL'),
]

data = []
for date in dates:
    for route in routes:
        # Simulate base passengers, lower on weekends
        base_passengers = np.random.randint(500, 3000)
        if date.weekday() >= 5:
            base_passengers = int(base_passengers * 0.7)
            
        # 2020/2021 COVID impact
        if date.year in [2020, 2021]:
            base_passengers = int(base_passengers * 0.2)
            
        flights = max(1, int(base_passengers / 150) + np.random.randint(0, 3))
        seats = flights * 180
        passengers = min(seats, base_passengers)
        
        data.append({
            'date': date,
            'origin': route[0],
            'destination': route[1],
            'flights': flights,
            'seats': seats,
            'passengers': passengers
        })

df = pd.DataFrame(data)
df.to_parquet('data/mock_flights.parquet', index=False)
print("Mock data generated at data/mock_flights.parquet")
