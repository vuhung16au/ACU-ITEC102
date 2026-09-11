#!/usr/bin/env python
# coding: utf-8

# # Handling Missing Values Before Exporting
#
# <a href="https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week07/06.Handling-Missing-Values-Before-Exporting/notebooks/06-handling-missing-values-before-exporting.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
#
# ## Overview
# In real-world data collection, sensor malfunctions, user dropouts, and communication timeouts result in **missing values** (`NaN` or `None`).
# Exporting datasets with unhandled missing values can crash downstream databases, break machine learning pipelines, or skew business reports.
#
# In this module, you will learn how to detect, inspect, drop, and impute (fill) missing values in Pandas, followed by validation checks before exporting clean data.

# ## Setup: Locate Sample Dataset
# We load `sample_weather.csv` (which intentionally includes missing sensor data).

# In[1]:


import os
from pathlib import Path
import numpy as np
import pandas as pd

current_dir = Path(__file__).resolve().parent if "__file__" in globals() else Path.cwd()
possible_paths = [
    current_dir / "sample_weather.csv",
    current_dir / "notebooks" / "sample_weather.csv",
    current_dir.parent / "notebooks" / "sample_weather.csv",
    Path("sample_weather.csv"),
    Path("notebooks/sample_weather.csv"),
]

csv_file = None
for p in possible_paths:
    if p.exists():
        csv_file = p
        break

if csv_file is None:
    csv_file = Path("sample_weather.csv")
    df_fallback = pd.DataFrame({
        "Date": pd.date_range(start="2026-01-01", periods=10, freq="D").strftime("%Y-%m-%d"),
        "City": ["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide"] * 2,
        "Temperature": [28.5, 22.1, 31.0, 35.5, 25.0, 27.0, np.nan, 30.5, 34.0, 26.5],
        "Rainfall": [0.0, 5.2, 0.0, 0.0, 1.5, 0.0, 10.5, 0.0, 0.0, 2.0],
    })
    df_fallback.to_csv(csv_file, index=False)

df = pd.read_csv(csv_file, parse_dates=["Date"])
print(f"Loaded {len(df)} records from {csv_file}\n")


# ## Code Snippets: Handling Missing Values
#
# ### 1. Detecting Missing Values
# Use `.isna()` (or `.isnull()`) combined with `.sum()` to identify missing entries per column.

# In[2]:


print("--- 1. Missing Value Audit ---")
missing_counts = df.isna().sum()
print("Count of missing values per column:")
print(missing_counts)

print("\nPercentage of missing values per column:")
print((df.isna().mean() * 100).round(2).astype(str) + "%")

# Isolate rows with any missing value
rows_with_na = df[df.isna().any(axis=1)]
print("\nRows containing at least one missing value:")
print(rows_with_na)


# ### 2. Strategy A: Dropping Missing Values (.dropna())
# When missing records represent corrupted or unrecoverable entries, use `.dropna()`.

# In[3]:


# Drop rows containing any nulls
df_dropped = df.dropna()
print(f"\n--- 2. Dropping Rows with Nulls ---")
print(f"Original row count: {len(df)}")
print(f"Row count after .dropna(): {len(df_dropped)}")

# Drop only if a specific critical column is missing
df_dropped_temp = df.dropna(subset=["Temperature"])
print(f"Row count after dropping missing Temperature: {len(df_dropped_temp)}")


# ### 3. Strategy B: Imputing / Filling Missing Values (.fillna())
# In many domains, dropping rows loses valuable surrounding data. Instead, we impute (fill) missing values with meaningful estimates:
# - **Constant Fill**: e.g., replacing missing rainfall with `0.0`
# - **Statistical Fill**: replacing missing temperature with the column mean or median

# In[4]:


# Create a working copy for imputation
df_imputed = df.copy()

# Compute mean temperature across the dataset
mean_temp = df_imputed["Temperature"].mean()
print(f"\n--- 3. Imputing Missing Temperature ---")
print(f"Computed Mean Temperature: {mean_temp:.2f}°C")

# Impute missing values
df_imputed["Temperature"] = df_imputed["Temperature"].fillna(mean_temp)

print("Missing values after imputation:")
print(df_imputed.isna().sum())


# ### 4. Validation and Exporting
# **Best Practice**: Before writing to disk, assert that zero missing values remain.

# In[5]:


# Verify no nulls exist anywhere in the DataFrame
total_missing = df_imputed.isna().sum().sum()
assert total_missing == 0, f"Error: {total_missing} missing values still remain!"
print("\n--- 4. Data Validation: PASSED (0 missing values remaining) ---")

output_file = "cleaned_weather_export.csv"
df_imputed.to_csv(output_file, index=False, float_format="%.2f")
print(f"Successfully exported clean, validated dataset to '{output_file}'")

# Preview the exported file
print("\nExported file preview:")
print(pd.read_csv(output_file).head(8))


# ## Enrichment
# ### Group-Specific Imputation
# Rather than filling with the nationwide average, fill missing temperature with the average temperature of that specific city!
# ```python
# df['Temperature'] = df.groupby('City')['Temperature'].transform(
#     lambda group: group.fillna(group.mean())
# )
# ```
#
# ### Forward and Backward Filling (Time-Series)
# In chronological weather or sensor logs, `.ffill()` propagates the last known valid reading forward:
# ```python
# df['Temperature'] = df['Temperature'].ffill()
# ```

# ## Takeaways
# - Always audit missing values using `df.isna().sum()` immediately after ingestion.
# - Choose between dropping (`.dropna()`) and imputing (`.fillna()`) based on domain requirements.
# - When imputing, choose sensible defaults (e.g. `0.0` for rainfall, column mean/median for temperature).
# - Validate data hygiene with assertions (`assert df.isna().sum().sum() == 0`) before exporting.
# - Always export with `index=False`.

# ## Conclusion
# Handling missing values proactively prevents subtle calculation biases and ensures data products are reliable and production-ready.

# ## Exercises
#
# **Exercise 1:** Count the number of non-null values in the dataset using `.notna().sum()`.
#
# **Exercise 2:** Create a copy of `df` and fill missing temperature using the **median** temperature.
#
# **Exercise 3:** Use forward fill (`.ffill()`) on a copy of `df` and confirm that row index 6 now inherits the temperature of row 5.

# In[6]:


# --- Solutions ---

print("\n=== Exercise Solutions ===")

# Exercise 1 Solution:
print("Exercise 1: Non-null counts per column:")
print(df.notna().sum())

# Exercise 2 Solution:
df_median = df.copy()
median_temp = df_median["Temperature"].median()
df_median["Temperature"] = df_median["Temperature"].fillna(median_temp)
print(f"\nExercise 2: Filled missing temperature with median ({median_temp:.1f}°C). Missing count = {df_median['Temperature'].isna().sum()}")

# Exercise 3 Solution:
df_ffill = df.copy()
df_ffill["Temperature"] = df_ffill["Temperature"].ffill()
print(f"\nExercise 3: Row 6 temperature after ffill (inherited from Row 5 Sydney 27.0°C): {df_ffill.loc[6, 'Temperature']}°C")

# Clean up temporary output file
if os.path.exists("cleaned_weather_export.csv"):
    os.remove("cleaned_weather_export.csv")
