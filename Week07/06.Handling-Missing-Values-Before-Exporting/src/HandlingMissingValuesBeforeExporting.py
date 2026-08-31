#!/usr/bin/env python
# coding: utf-8

# # Handling Missing Values Before Exporting
#
# <a href="https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week07/06.Handling-Missing-Values-Before-Exporting/notebooks/06-handling-missing-values-before-exporting.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
#
# ## Overview
# This notebook covers the concepts and practical applications of Handling Missing Values Before Exporting in Pandas.

# ## Setup: Generate Dummy Data
# First, let's create a synthetic dataset to work with.

# In[1]:


import pandas as pd
import numpy as np
import os

# Create a dummy weather dataset
data = {
    "Date": pd.date_range(start="1/1/2026", periods=10, freq="D"),
    "City": ["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide"] * 2,
    "Temperature": [28.5, 22.1, 31.0, 35.5, 25.0, 27.0, np.nan, 30.5, 34.0, 26.5],
    "Rainfall": [0.0, 5.2, 0.0, 0.0, 1.5, 0.0, 10.5, 0.0, 0.0, 2.0],
}
df_weather = pd.DataFrame(data)
df_weather.to_csv("sample_weather.csv", index=False)
print("Created sample_weather.csv")


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
