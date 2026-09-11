#!/usr/bin/env python
# coding: utf-8

# # Filtering Loaded Data
#
# <a href="https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week07/04.Filtering-Loaded-Data/notebooks/04-filtering-loaded-data.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
#
# ## Overview
# Once data is loaded into Pandas, you frequently need to answer specific questions by filtering down to subsets of interest (e.g., "Which days had temperatures above 30°C?", "Which records belong to Sydney and had rain?").
#
# In this module, you will learn how to filter DataFrames using **boolean indexing**, logical operators (`&`, `|`, `~`), `.isin()`, string methods, and the readable `.query()` syntax.

# ## Setup: Locate Sample Dataset
# We locate `sample_weather.csv`.

# In[1]:


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
print(f"Loaded {len(df)} records from {csv_file}\n")


# ## Code Snippets: Filtering Techniques
#
# ### 1. Single Boolean Condition
# A comparison expression on a column produces a boolean Series (True/False mask). Passing that mask into `df[...]` filters the rows.

# In[2]:


# Filter for hot days (temperature > 30.0 degrees)
hot_mask = df["Temperature"] > 30.0
hot_days = df[hot_mask]

print("--- 1. Hot Days (Temperature > 30°C) ---")
print(hot_days[["Date", "City", "Temperature"]])


# ### 2. Multiple Conditions: Logical AND (&) and OR (|)
# **Crucial Rule:** In Pandas, you must use bitwise operators `&` (AND) and `|` (OR) instead of Python's `and` / `or`, and **each condition must be enclosed in parentheses `()`**.

# In[3]:


# Rainy days in Sydney or Melbourne
rainy_syd_melb = df[(df["City"].isin(["Sydney", "Melbourne"])) & (df["Rainfall"] > 0)]
print("\n--- 2. Rainy Days in Sydney or Melbourne (&) ---")
print(rainy_syd_melb)

# Extreme weather: Hot (> 33C) OR Rainy (> 5mm)
extreme_weather = df[(df["Temperature"] > 33.0) | (df["Rainfall"] > 5.0)]
print("\n--- Extreme Weather: Hot (>33°C) OR Rainy (>5mm) (|) ---")
print(extreme_weather)


# ### 3. Categorical Filtering with .isin() and Negation (~)
# Instead of chaining multiple `(df['City'] == 'Sydney') | (df['City'] == 'Perth')`, use `.isin()`. Add `~` in front to negate the condition.

# In[4]:


# Filter for selected cities
selected_cities = df[df["City"].isin(["Brisbane", "Perth"])]
print("\n--- 3. Cities in Brisbane or Perth (.isin()) ---")
print(selected_cities[["City", "Temperature"]])

# Negation: Cities NOT in Perth
non_perth = df[~df["City"].isin(["Perth"])]
print(f"\nTotal non-Perth records: {len(non_perth)}")


# ### 4. String-Based Filtering (.str Accessor)
# Filter text columns using vectorized string methods like `.str.startswith()`, `.str.contains()`.

# In[5]:


# Cities starting with 'M' (Melbourne)
m_cities = df[df["City"].str.startswith("M")]
print("\n--- 4. Cities Starting with 'M' (.str.startswith()) ---")
print(m_cities)


# ### 5. Alternative Syntax: df.query()
# `.query()` allows you to write filtering expressions as concise, readable strings.

# In[6]:


# Query hot dry days
dry_hot = df.query("Temperature >= 30.0 and Rainfall == 0")
print("\n--- 5. Clean Query: Hot & Dry Days (df.query()) ---")
print(dry_hot[["Date", "City", "Temperature", "Rainfall"]])


# ## Enrichment
# ### Filtering with .between()
# Select numerical ranges without chaining two conditions:
# ```python
# comfortable_days = df[df['Temperature'].between(24.0, 29.0)]
# ```
#
# ### Simultaneous Filtering and Column Selection with .loc
# Using `.loc[condition, [columns]]` is more efficient than filtering first and indexing second:
# ```python
# df.loc[df['Temperature'] > 30, ['City', 'Temperature']]
# ```

# ## Takeaways
# - Filter rows by passing boolean Series masks into `df[...]`.
# - Always wrap individual conditions in parentheses `(cond1) & (cond2)`.
# - Use `&` for AND, `|` for OR, and `~` for NOT.
# - Use `.isin([...])` for multi-value categorical membership checks.
# - Use `.query("col > val")` for cleaner, highly readable code.

# ## Conclusion
# Filtering is the core mechanism to interrogate datasets and extract meaningful insights. Mastering boolean masks and `.query()` ensures efficient data wrangling.

# ## Exercises
#
# **Exercise 1:** Filter all days where Rainfall was strictly greater than 0 mm (rainy days).
#
# **Exercise 2:** Find all records for Adelaide where Temperature was below 26°C.
#
# **Exercise 3:** Use `.query()` to find records where Temperature is between 25°C and 32°C inclusive.

# In[7]:


# --- Solutions ---

print("\n=== Exercise Solutions ===")

# Exercise 1 Solution:
rainy_days = df[df["Rainfall"] > 0]
print(f"Exercise 1: {len(rainy_days)} rainy days found:")
print(rainy_days[["Date", "City", "Rainfall"]])

# Exercise 2 Solution:
cool_adelaide = df[(df["City"] == "Adelaide") & (df["Temperature"] < 26.0)]
print("\nExercise 2 (Cool Adelaide Days):")
print(cool_adelaide[["Date", "City", "Temperature"]])

# Exercise 3 Solution:
query_res = df.query("Temperature >= 25.0 and Temperature <= 32.0")
print("\nExercise 3 (.query 25C to 32C):")
print(query_res[["Date", "City", "Temperature"]])
