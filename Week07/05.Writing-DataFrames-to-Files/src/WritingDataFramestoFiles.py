#!/usr/bin/env python
# coding: utf-8

# # Writing DataFrames to Files
#
# <a href="https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week07/05.Writing-DataFrames-to-Files/notebooks/05-writing-dataframes-to-files.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
#
# ## Overview
# Once you have cleansed, transformed, or filtered data in Pandas, you need to export your results to disk so they can be consumed by dashboards, spreadsheets, stakeholders, or web APIs.
#
# In this module, you will learn how to write DataFrames to **CSV**, **JSON**, and **Excel** files, with a critical focus on the `index=False` parameter to prevent the notorious `Unnamed: 0` bug.

# ## Setup: Locate Sample Dataset
# We load `sample_weather.csv`.

# In[1]:


import json
import os
from pathlib import Path
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
        "Temperature": [28.5, 22.1, 31.0, 35.5, 25.0, 27.0, None, 30.5, 34.0, 26.5],
        "Rainfall": [0.0, 5.2, 0.0, 0.0, 1.5, 0.0, 10.5, 0.0, 0.0, 2.0],
    })
    df_fallback.to_csv(csv_file, index=False)

df = pd.read_csv(csv_file, parse_dates=["Date"])
print(f"Loaded {len(df)} records for export demonstrations.\n")


# ## Code Snippets: Exporting DataFrames
#
# ### 1. Exporting to CSV: The Crucial index=False Rule
# When exporting to CSV, Pandas by default saves the integer row index (0, 1, 2...). When reloaded, Pandas creates an unwanted `Unnamed: 0` column. **Always pass `index=False` unless your index contains meaningful row labels!**

# In[2]:


# Filter hot days for a specialized report
hot_days_df = df[df["Temperature"] >= 30.0].copy()

output_csv = "hot_weather_report.csv"
hot_days_df.to_csv(output_csv, index=False)
print(f"--- 1. Saved Hot Weather Report to '{output_csv}' ---")

# Verify by reading back
reloaded_csv = pd.read_csv(output_csv)
print("Reloaded CSV columns:", list(reloaded_csv.columns))
print(reloaded_csv.head(3))


# ### 2. Exporting to JSON: Web & API Integration
# JSON is the standard format for web applications. Use `orient='records'` to generate a clean array of JSON objects.

# In[3]:


output_json = "hot_weather_report.json"
hot_days_df.to_json(output_json, orient="records", date_format="iso", indent=2)
print(f"\n--- 2. Saved JSON Report to '{output_json}' ---")

# Preview first few lines of generated JSON
with open(output_json, "r", encoding="utf-8") as f:
    json_preview = f.read()[:200]
print(f"JSON Preview:\n{json_preview}...\n")


# ### 3. Exporting Aggregated Summaries
# Often, you export statistical summaries rather than raw rows.

# In[4]:


city_summary = df.groupby("City", as_index=False).agg(
    Avg_Temperature=("Temperature", "mean"),
    Total_Rainfall=("Rainfall", "sum"),
)
summary_csv = "city_weather_summary.csv"
city_summary.to_csv(summary_csv, index=False, float_format="%.2f")

print(f"--- 3. Saved Summary Metrics to '{summary_csv}' ---")
print(pd.read_csv(summary_csv))


# ### 4. Exporting to Excel (Optional openpyxl)
# You can export DataFrames into styled Microsoft Excel worksheets using `to_excel()`.

# In[5]:


output_excel = "weather_export.xlsx"
try:
    city_summary.to_excel(output_excel, sheet_name="CityStats", index=False)
    print(f"\n--- 4. Saved Excel Workbook to '{output_excel}' ---")
except ImportError:
    print("\n--- 4. Excel Export Skipped ---")
    print("openpyxl required for .xlsx export. Install via: uv add openpyxl")


# ## Enrichment
# ### Exporting Gzipped CSVs on the Fly
# Pandas can compress files transparently simply by providing the `.gz` extension:
# ```python
# df.to_csv('large_dataset.csv.gz', compression='gzip', index=False)
# ```
#
# ### Markdown Tables for Documentation
# For generating markdown tables directly inside reports or GitHub READMEs:
# ```python
# print(city_summary.to_markdown(index=False))
# ```

# ## Takeaways
# - Always include `index=False` when calling `to_csv()` unless your index is a named, meaningful key.
# - Use `df.to_json(..., orient='records', indent=2)` when delivering data to web services.
# - Use `float_format='%.2f'` in `to_csv()` to round floating-point numbers consistently.
# - Always test-read exported files to confirm columns and data formats survived the round-trip.

# ## Conclusion
# Writing data safely and consistently ensures your data pipelines integrate cleanly with downstream systems, colleagues, and external clients.

# ## Exercises
#
# **Exercise 1:** Filter records for Sydney only and export them to `sydney_weather.csv` with `index=False`.
#
# **Exercise 2:** Export `city_summary` to a JSON file named `city_summary.json` with `orient='records'`.
#
# **Exercise 3:** Reload `sydney_weather.csv` and assert that no column starts with `"Unnamed"`.

# In[6]:


# --- Solutions ---

print("\n=== Exercise Solutions ===")

# Exercise 1 Solution:
sydney_df = df[df["City"] == "Sydney"]
sydney_df.to_csv("sydney_weather.csv", index=False)
print(f"Exercise 1: Exported {len(sydney_df)} Sydney records to 'sydney_weather.csv'")

# Exercise 2 Solution:
city_summary.to_json("city_summary.json", orient="records", indent=2)
print("Exercise 2: Exported city summary to 'city_summary.json'")

# Exercise 3 Solution:
check_df = pd.read_csv("sydney_weather.csv")
has_unnamed = any("Unnamed" in col for col in check_df.columns)
print(f"Exercise 3: Reloaded successfully! Contains unwanted 'Unnamed' column? {has_unnamed}")

# Clean up temporary exercise files
for tmp_file in ["hot_weather_report.csv", "hot_weather_report.json", "city_weather_summary.csv", "sydney_weather.csv", "city_summary.json"]:
    if os.path.exists(tmp_file):
        os.remove(tmp_file)
if os.path.exists("weather_export.xlsx"):
    os.remove("weather_export.xlsx")
print("\nCleaned up exercise demonstration output files.")
