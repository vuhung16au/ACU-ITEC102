#!/usr/bin/env python
# coding: utf-8

# # Reading Excel and JSON Files
#
# <a href="https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week07/03.Reading-Excel-and-JSON-Files/notebooks/03-reading-excel-and-json-files.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
#
# ## Overview
# This notebook covers the concepts and practical applications of Reading Excel and JSON Files in Pandas.

# ## Setup: Generate Additional Dummy Data
# Let's also create dummy Excel and JSON files.

# In[1]:


import pandas as pd
import numpy as np

# Create a dummy energy dataset for Excel
energy_data = {
    "Year": [2021, 2022, 2023, 2024, 2025],
    "State": ["NSW", "NSW", "NSW", "NSW", "NSW"],
    "Energy_Produced": [1500, 1600, 1550, 1700, 1650],
}
df_energy = pd.DataFrame(energy_data)
df_energy.to_excel("energy_stats.xlsx", sheet_name="NSW", index=False)
print("Created energy_stats.xlsx")

# Create a dummy Airbnb dataset for JSON
airbnb_data = [
    {"id": 1, "neighbourhood": "Bondi", "price": 150},
    {"id": 2, "neighbourhood": "Manly", "price": 200},
    {"id": 3, "neighbourhood": "Bondi", "price": 180},
]
df_airbnb = pd.DataFrame(airbnb_data)
df_airbnb.to_json("sydney_airbnb.json", orient="records", indent=2)
print("Created sydney_airbnb.json")


# ## Code Snippets
# Here are some examples demonstrating the concepts.

# In[2]:


import pandas as pd

# Replace with specific topic code
pass


# ## Enrichment
# ### The Trap of Compression
# Saving tiny CSV files in compressed format (`.gz`) can actually increase their file size due to metadata overhead! Compression is meant for large files.
#
# ### Encoding Nightmares (UTF-8)
# If you see weird symbols instead of accented characters, try specifying the encoding when reading a file:
# `pd.read_csv('file.csv', encoding='utf-8')`

# ## Takeaways
# - Pandas simplifies reading from and writing to files.
# - Exploring and summarizing data is quick using `df.head()` and filtering techniques.
# - Handling missing values before exporting ensures downstream compatibility with tools like Excel.

# ## Conclusion
# Understanding Data Input and Output (I/O) forms the foundation of any data pipeline in Python.

# ## Exercises
# **Exercise 1:** Try loading the `sample_weather.csv` file into a DataFrame and display the first 3 rows.
#
# *Hint: Use `pd.read_csv()` and `.head()`*

# In[3]:


# Write your code here

# --- Solution ---
# df = pd.read_csv('sample_weather.csv')
# print(df.head(3))
