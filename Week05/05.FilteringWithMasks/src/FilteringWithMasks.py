# Filtering Data using NumPy Masks (Boolean Arrays)

# Import the NumPy library
import numpy as np

# Create a NumPy array of ages
ages = np.array([15, 22, 14, 30, 18, 12])

# Create a boolean mask for ages greater than or equal to 18
adult_mask = ages >= 18

# Filter the ages array using the boolean mask to get only adult ages
adults = ages[adult_mask]

# Print the filtered adult ages
print(f"Adult ages only: {adults}")

# Expected Output: Adult ages only: [22 30 18]

# Advanced Filtering: Using Multiple Conditions

## Filter ages between 15 and 25 using a combined boolean mask
teen_mask = (ages >= 15) & (ages <= 25)
teens = ages[teen_mask]
print(f"Teen ages only: {teens}")

## Expected Output: Teen ages only: [15 22 18]

## Use OR condition to filter ages less than 15 or greater than 25
outlier_mask = (ages < 15) | (ages > 25)
outliers = ages[outlier_mask]
print(f"Outlier ages only: {outliers}")

## Expected Output: Outlier ages only: [14 30]

# Handling Missing Data (NaNs)

# Standard comparison operators (==, >, <) fail or act unpredictably with NaN
telemetry_data = np.array([1.2, 2.5, np.nan, 4.1, np.nan, 3.3])
print(f"Telemetry data: {telemetry_data}")

# Use np.isnan() to create a mask for NaN values
nan_mask = np.isnan(telemetry_data)
print(f"NaN mask: {nan_mask}")


# Filter out NaN values
clean_data = telemetry_data[~nan_mask]
print(f"Clean data: {clean_data}")
