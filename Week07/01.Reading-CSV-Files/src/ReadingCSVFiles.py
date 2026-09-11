#!/usr/bin/env python
# coding: utf-8

# # Reading a CSV File
#
# <a href="https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week07/01.Reading-CSV-Files/notebooks/01-reading-csv-files.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
#
# ## Overview
# This notebook and script cover how to import tabular data stored in Comma-Separated Values (`.csv`) format into a Pandas DataFrame using `pd.read_csv()`.
#
# CSV is the most common plain-text format used for exchanging data in business and data science. In this topic, we use Australian weather observations recorded across Sydney, Melbourne, Brisbane, Perth, and Adelaide.

# ## Setup: Locate Sample Dataset
# We locate the `sample_weather.csv` file, ensuring the script runs smoothly whether executed from the project root or the notebooks folder.

# In[1]:


import os
from pathlib import Path
import pandas as pd

# Determine the dataset path reliably
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
    # Create fallback dataset if file is not found
    csv_file = Path("sample_weather.csv")
    df_fallback = pd.DataFrame({
        "Date": pd.date_range(start="2026-01-01", periods=10, freq="D").strftime("%Y-%m-%d"),
        "City": ["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide"] * 2,
        "Temperature": [28.5, 22.1, 31.0, 35.5, 25.0, 27.0, None, 30.5, 34.0, 26.5],
        "Rainfall": [0.0, 5.2, 0.0, 0.0, 1.5, 0.0, 10.5, 0.0, 0.0, 2.0],
    })
    df_fallback.to_csv(csv_file, index=False)

print(f"Using CSV file: {csv_file}")


# ## Code Snippets: Demonstrating pd.read_csv() Parameters
#
# ### 1. Basic CSV Ingestion
# By default, `pd.read_csv()` assumes the first row contains column headers and fields are separated by commas.

# In[2]:


# 1. Basic reading
df_basic = pd.read_csv(csv_file)
print("--- 1. Basic Ingestion (First 5 Rows) ---")
print(df_basic.head())
print("\nColumn Data Types:")
print(df_basic.dtypes)


# ### 2. Parsing Dates
# Notice in snippet 1 that `Date` was loaded as an `object` (string). With `parse_dates`, Pandas converts it directly into a datetime object (`datetime64[ns]`), unlocking time-series capabilities.

# In[3]:


# 2. Parsing dates
df_dates = pd.read_csv(csv_file, parse_dates=["Date"])
print("--- 2. Date Column Parsed to Datetime ---")
print(df_dates.dtypes)
print(f"\nFirst record Date type: {type(df_dates['Date'].iloc[0])}")


# ### 3. Setting an Index Column
# You can designate a specific column (e.g. `Date`) as the DataFrame index during ingestion using `index_col`.

# In[4]:


# 3. Setting index_col
df_indexed = pd.read_csv(csv_file, parse_dates=["Date"], index_col="Date")
print("--- 3. Indexed by Date ---")
print(df_indexed.head(3))
print("\nDataFrame Index:")
print(df_indexed.index)


# ### 4. Memory Optimisation: usecols and nrows
# When dealing with huge datasets with dozens of columns and millions of rows, use `usecols` to load only what you need and `nrows` to inspect a preview.

# In[5]:


# 4. Selecting specific columns and previewing first 4 rows
df_subset = pd.read_csv(csv_file, usecols=["City", "Temperature"], nrows=4)
print("--- 4. Subset of Columns and Rows ---")
print(df_subset)


# ## Enrichment
# ### The Trap of Compression
# Saving tiny CSV files in compressed format (`.gz`) can actually increase file size due to metadata overhead! Compression is meant for files larger than a few megabytes.
#
# ### Handling Encoding (`encoding='utf-8'` vs `'latin-1'`)
# If you see symbols like `` instead of accented characters or symbols, specify the encoding explicitly:
# ```python
# df = pd.read_csv('australian_census.csv', encoding='utf-8')
# ```
#
# ### Reading CSVs from a URL
# `pd.read_csv()` can also fetch CSV files directly over HTTP/HTTPS:
# ```python
# url = "https://raw.githubusercontent.com/vuhung16au/ACU-ITEC102/main/Week07/01.Reading-CSV-Files/notebooks/sample_weather.csv"
# # df_web = pd.read_csv(url)
# ```

# ## Takeaways
# - `pd.read_csv()` is the primary function to load CSV files into Pandas DataFrames.
# - Use `parse_dates=['Date']` to automatically parse temporal columns into `datetime64`.
# - Use `index_col='col_name'` to set an index column upon reading.
# - Use `usecols` to select specific columns and `nrows` to limit row count for memory efficiency.
# - Check `df.dtypes` immediately after loading to confirm data types are correct.

# ## Conclusion
# Reading CSV files correctly with appropriate parameters ensures your data pipeline starts with clean, correctly typed DataFrames, avoiding errors in later analysis steps.

# ## Exercises
#
# **Exercise 1:** Load only the `Date` and `Rainfall` columns from `sample_weather.csv`, ensuring `Date` is parsed as a datetime.
#
# **Exercise 2:** Load the first 3 rows of `sample_weather.csv` and print the total memory used.
#
# **Exercise 3:** Load the file setting `Date` as the index, then select the temperature on `'2026-01-04'`.

# In[6]:


# --- Solutions ---

print("\n=== Exercise Solutions ===")

# Exercise 1 Solution:
ex1_df = pd.read_csv(csv_file, usecols=["Date", "Rainfall"], parse_dates=["Date"])
print("\nExercise 1 Result:")
print(ex1_df.head(3))

# Exercise 2 Solution:
ex2_df = pd.read_csv(csv_file, nrows=3)
print("\nExercise 2 Result (Memory Usage in bytes):")
print(ex2_df.memory_usage(deep=True))

# Exercise 3 Solution:
ex3_df = pd.read_csv(csv_file, parse_dates=["Date"], index_col="Date")
print("\nExercise 3 Result (Temperature on 2026-01-04):")
temp_04 = ex3_df.loc["2026-01-04", "Temperature"]
print(f"Perth Temperature on 2026-01-04: {temp_04}°C")
