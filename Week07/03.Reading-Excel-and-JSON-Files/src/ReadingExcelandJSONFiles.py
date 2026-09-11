#!/usr/bin/env python
# coding: utf-8

# # Reading Excel and JSON Files
#
# <a href="https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week07/03.Reading-Excel-and-JSON-Files/notebooks/03-reading-excel-and-json-files.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
#
# ## Overview
# In real-world data science, not all data arrives as CSV files.
# - **Microsoft Excel (`.xlsx`)**: Common in corporate environments, often containing multiple formatted sheets, formulas, and headers.
# - **JSON (JavaScript Object Notation)**: The standard data format for web APIs, microservices, and NoSQL databases.
#
# In this module, you will learn how to read data from Excel workbooks (`energy_stats.xlsx`) and JSON files (`sydney_airbnb.json`) into Pandas DataFrames.

# ## Setup: Locate Dataset Files
# We locate `energy_stats.xlsx` and `sydney_airbnb.json` reliably.

# In[1]:


import json
import os
from pathlib import Path
import pandas as pd

current_dir = Path(__file__).resolve().parent if "__file__" in globals() else Path.cwd()
possible_dirs = [
    current_dir / "notebooks",
    current_dir,
    current_dir.parent / "notebooks",
    Path("notebooks"),
    Path("."),
]

excel_file = None
json_file = None

for d in possible_dirs:
    if excel_file is None and (d / "energy_stats.xlsx").exists():
        excel_file = d / "energy_stats.xlsx"
    if json_file is None and (d / "sydney_airbnb.json").exists():
        json_file = d / "sydney_airbnb.json"

print(f"Excel file: {excel_file}")
print(f"JSON file:  {json_file}")


# ## Code Snippets: Reading JSON Files
#
# ### 1. Reading Structured JSON with pd.read_json()
# JSON files structured as an array of records (list of objects) convert seamlessly into a 2D DataFrame.

# In[2]:


print("\n--- 1. Reading Sydney Airbnb Listings (JSON) ---")
df_airbnb = pd.read_json(json_file)
print(df_airbnb)

print("\n--- Summary of Airbnb Listings ---")
print(f"Total Listings: {len(df_airbnb)}")
print(f"Average Price:  ${df_airbnb['price'].mean():.2f} AUD/night")
print(f"Average Rating: {df_airbnb['rating'].mean():.2f} / 5.0")


# ### 2. Flattening Nested JSON with pd.json_normalize()
# Web APIs frequently return nested JSON hierarchies (dictionaries inside dictionaries). `pd.json_normalize()` flattens these into distinct columns.

# In[3]:


print("\n--- 2. Handling Nested API JSON Structures ---")
nested_api_data = [
    {
        "student_id": "S101",
        "name": "Nguyen An",
        "campus": {"city": "Sydney", "state": "NSW"},
        "enrolment": {"course": "ITEC102", "semester": 1},
    },
    {
        "student_id": "S102",
        "name": "Sarah Miller",
        "campus": {"city": "Melbourne", "state": "VIC"},
        "enrolment": {"course": "ITEC102", "semester": 1},
    },
]

df_nested = pd.json_normalize(nested_api_data)
print(df_nested)


# ## Code Snippets: Reading Microsoft Excel Files
#
# ### 3. Reading Specific Excel Sheets with pd.read_excel()
# Excel workbooks can contain multiple worksheets. You specify which sheet to read using the `sheet_name` parameter.

# In[4]:


print("\n--- 3. Reading Excel Worksheets ---")
try:
    df_energy = pd.read_excel(excel_file, sheet_name="NSW")
    print("NSW Clean Energy Generation (GWh):")
    print(df_energy)
    print(f"\nTotal Energy Produced (2021-2025): {df_energy['Energy_Produced'].sum()} GWh")
except ImportError:
    print(
        "Note: Reading .xlsx files requires the 'openpyxl' engine.\n"
        "Install via: uv add openpyxl (or pip install openpyxl)"
    )


# ### 4. Inspecting Available Sheet Names with pd.ExcelFile
# When you receive an unfamiliar Excel workbook, inspect all worksheet names before loading data.

# In[5]:


print("\n--- 4. Discovering Excel Sheet Names ---")
try:
    excel_reader = pd.ExcelFile(excel_file)
    print(f"Sheet names in workbook: {excel_reader.sheet_names}")
except ImportError:
    print("openpyxl required to inspect sheets.")


# ## Enrichment
# ### Format Trade-offs: CSV vs Excel vs JSON
# | Feature | CSV | Excel (`.xlsx`) | JSON |
# |---|---|---|---|
# | **Primary Use** | Universal data exchange | Business spreadsheets, multi-tab reports | Web APIs, semi-structured logs |
# | **Speed & Size** | Fast, compact plain text | Slower, heavier XML-based zip | Flexible, slightly verbose text |
# | **Hierarchy** | Flat tables only | Multiple flat 2D sheets | Nested dictionaries & arrays |
# | **Pandas Function** | `pd.read_csv()` | `pd.read_excel()` | `pd.read_json()` / `json_normalize()` |
#
# ### Reading All Sheets at Once
# Passing `sheet_name=None` to `pd.read_excel()` returns a Python dictionary where each key is a sheet name, and each value is the corresponding DataFrame!
# ```python
# # all_sheets = pd.read_excel('multi_state_energy.xlsx', sheet_name=None)
# # print(all_sheets.keys())
# ```

# ## Takeaways
# - Use `pd.read_json()` to load flat JSON records directly into DataFrames.
# - Use `pd.json_normalize()` to flatten nested, hierarchical JSON responses from web APIs.
# - Use `pd.read_excel()` with `sheet_name='SheetName'` to load specific tabs from Excel workbooks.
# - Use `pd.ExcelFile(file_path).sheet_names` to discover what sheets exist before loading.
# - Ensure `openpyxl` is installed in your Python environment when working with `.xlsx` files.

# ## Conclusion
# Real-world data analysts must be fluent across formats. Combining `pd.read_excel()`, `pd.read_json()`, and `pd.json_normalize()` ensures you can ingest whatever data format your organization or API provides.

# ## Exercises
#
# **Exercise 1:** Filter `df_airbnb` to show only listings located in `"Bondi"`, and compute their average price.
#
# **Exercise 2:** Identify the most affordable listing in the Airbnb dataset using `.loc[df['price'].idxmin()]`.
#
# **Exercise 3:** Flatten a nested dictionary with student marks using `pd.json_normalize()` and display the DataFrame.

# In[6]:


# --- Solutions ---

print("\n=== Exercise Solutions ===")

# Exercise 1 Solution:
bondi_listings = df_airbnb[df_airbnb["neighbourhood"] == "Bondi"]
print(f"Exercise 1: Average Bondi Price = ${bondi_listings['price'].mean():.2f} AUD/night")

# Exercise 2 Solution:
cheapest_idx = df_airbnb["price"].idxmin()
cheapest_listing = df_airbnb.loc[cheapest_idx]
print(f"Exercise 2: Cheapest listing is '{cheapest_listing['name']}' in {cheapest_listing['neighbourhood']} at ${cheapest_listing['price']} AUD/night")

# Exercise 3 Solution:
sample_marks = [
    {"name": "Liam Vu", "assessment": {"quiz": 18, "project": 45}},
    {"name": "Chloe Smith", "assessment": {"quiz": 20, "project": 48}},
]
df_marks = pd.json_normalize(sample_marks)
print("\nExercise 3 Normalized Marks:")
print(df_marks)
