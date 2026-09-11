#!/usr/bin/env python
# coding: utf-8

# # Exploring and Summarising Data
#
# <a href="https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week07/02.Exploring-and-Summarising-Data/notebooks/02-exploring-and-summarising-data.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
#
# ## Overview
# Once data is loaded into a Pandas DataFrame, the immediate next step is **exploratory data analysis (EDA)**.
# In this module, you will learn how to inspect the dimensions, preview rows, check data types and missing values, and calculate key descriptive statistics on Australian weather observations.

# ## Setup: Locate Sample Dataset
# We locate the `sample_weather.csv` dataset.

# In[1]:


import os
from pathlib import Path
import pandas as pd

# Determine dataset path reliably
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
        "Temperature": [28.5, 22.1, 31.0, 35.5, 25.0, 27.0, None, 30.5, 34.0, 26.5],
        "Rainfall": [0.0, 5.2, 0.0, 0.0, 1.5, 0.0, 10.5, 0.0, 0.0, 2.0],
    })
    df_fallback.to_csv(csv_file, index=False)

df = pd.read_csv(csv_file, parse_dates=["Date"])
print(f"Loaded {len(df)} rows from {csv_file}\n")


# ## Code Snippets: Exploring and Summarising Data
#
# ### 1. Structural Inspection: head(), tail(), shape, columns
# Use `.head()` and `.tail()` to view the beginning and end of the dataset, and `.shape` to check its dimensions (rows, columns).

# In[2]:


print("--- 1. First 3 Rows (.head(3)) ---")
print(df.head(3))

print("\n--- Last 2 Rows (.tail(2)) ---")
print(df.tail(2))

print(f"\nDataFrame Dimensions (.shape): {df.shape} (rows, columns)")
print(f"Column Names (.columns): {list(df.columns)}")


# ### 2. Systemic Metadata: info() and dtypes
# `.info()` provides a comprehensive summary of column names, non-null counts, data types, and RAM usage.

# In[3]:


print("\n--- 2. Dataset Information (.info()) ---")
df.info()


# ### 3. Descriptive Statistics: describe()
# `.describe()` calculates count, mean, standard deviation, min, percentiles (25%, 50%, 75%), and max for numerical columns.

# In[4]:


print("\n--- 3. Numerical Summary Statistics (.describe()) ---")
print(df.describe())

print("\n--- Summary Including Categorical Columns (.describe(include='all')) ---")
print(df.describe(include="all"))


# ### 4. Targeted Aggregations & Frequency Counts
# Compute specific statistical aggregates or investigate frequency distributions of categorical columns.

# In[5]:


print("\n--- 4. Targeted Aggregations ---")
print(f"Mean Temperature: {df['Temperature'].mean():.2f}°C")
print(f"Median Temperature: {df['Temperature'].median():.2f}°C")
print(f"Total Recorded Rainfall: {df['Rainfall'].sum():.1f} mm")

print("\n--- Observation Counts per City (.value_counts()) ---")
print(df["City"].value_counts())

print(f"\nUnique Cities ({df['City'].nunique()}): {df['City'].unique()}")


# ## Enrichment
# ### Finding Extremes with idxmax() and idxmin()
# Rather than just finding the maximum number, `.idxmax()` returns the index position of the highest value, allowing you to fetch the entire record!

# In[6]:


hottest_row_idx = df["Temperature"].idxmax()
hottest_record = df.loc[hottest_row_idx]
print("\n--- Enrichment: Hottest Day Record ---")
print(f"Hottest City: {hottest_record['City']}")
print(f"Date: {hottest_record['Date'].strftime('%Y-%m-%d')}")
print(f"Temperature: {hottest_record['Temperature']}°C")

print("\n--- Enrichment: Average Temperature by City (groupby) ---")
print(df.groupby("City")["Temperature"].mean())


# ## Takeaways
# - Always start data exploration with `df.info()` to check data types and identify missing values.
# - Use `df.describe()` to quickly gauge the spread, mean, and range of numerical features.
# - Use `.value_counts()` to inspect the representation and balance of categories.
# - Combine `.idxmax()` with `.loc[]` to look up complete records associated with minimum or maximum values.

# ## Conclusion
# Exploring and summarising data gives you vital visibility into data quality, outliers, and distributions before performing complex analytics or machine learning.

# ## Exercises
#
# **Exercise 1:** Compute the average (mean) and maximum rainfall across all records.
#
# **Exercise 2:** Identify the date and city where the heaviest rainfall occurred using `.idxmax()`.
#
# **Exercise 3:** Check how many missing values exist in the `Temperature` column using `.isna().sum()`.

# In[7]:


# --- Solutions ---

print("\n=== Exercise Solutions ===")

# Exercise 1 Solution:
print(f"Exercise 1: Mean Rainfall = {df['Rainfall'].mean():.2f} mm, Max Rainfall = {df['Rainfall'].max():.1f} mm")

# Exercise 2 Solution:
wettest_idx = df["Rainfall"].idxmax()
wettest_day = df.loc[wettest_idx]
print(f"Exercise 2: Heaviest rain was in {wettest_day['City']} on {wettest_day['Date'].strftime('%Y-%m-%d')} ({wettest_day['Rainfall']} mm)")

# Exercise 3 Solution:
missing_temps = df["Temperature"].isna().sum()
print(f"Exercise 3: Missing Temperature records = {missing_temps}")
