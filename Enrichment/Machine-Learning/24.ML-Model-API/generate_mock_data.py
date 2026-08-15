import pandas as pd
import numpy as np

np.random.seed(42)
makes = ['Toyota', 'Ford', 'Holden', 'Mazda', 'Hyundai', 'Kia', 'Mitsubishi', 'Nissan']
n_samples = 200

data = {
    'Make': np.random.choice(makes, n_samples),
    'Engine_Size_L': np.round(np.random.uniform(1.2, 5.0, n_samples), 1),
    'Fuel_Type': np.random.choice(['Petrol', 'Diesel', 'Hybrid'], n_samples, p=[0.7, 0.2, 0.1])
}

df = pd.DataFrame(data)

# Simulate Fuel Consumption based on Engine Size and Fuel Type
df['Fuel_Consumption_L_100km'] = df['Engine_Size_L'] * 2.5 + np.random.normal(0, 1, n_samples)
df.loc[df['Fuel_Type'] == 'Hybrid', 'Fuel_Consumption_L_100km'] *= 0.6
df.loc[df['Fuel_Type'] == 'Diesel', 'Fuel_Consumption_L_100km'] *= 0.8
df['Fuel_Consumption_L_100km'] = np.round(df['Fuel_Consumption_L_100km'], 1)

# Simulate CO2 Emissions (roughly proportional to fuel consumption)
df['CO2_Emissions_g_km'] = df['Fuel_Consumption_L_100km'] * 23.2 + np.random.normal(0, 10, n_samples)
df['CO2_Emissions_g_km'] = np.round(df['CO2_Emissions_g_km']).astype(int)

df.to_csv('data/mock_vehicles.csv', index=False)
print("Mock data generated at data/mock_vehicles.csv")
