#!/usr/bin/env python
# coding: utf-8

# # Hierarchical Indexing (MultiIndex)
#
# <a href="https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week09/01.Hierarchical-Indexing/notebooks/01_01.Hierarchical-Indexing.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
#
# ## Overview
# **Hierarchical Indexing** (also known as `MultiIndex`) allows a Pandas Series or DataFrame to maintain multiple index levels on an axis.
# This enables you to represent higher-dimensional data (e.g., State -> City -> Year) within a standard 2D tabular format.
#
# In this module, you will learn how to:
# - Create a DataFrame with a MultiIndex.
# - Access and slice data across different index levels.
# - Use the cross-section `.xs()` method.
# - Group and aggregate data at specific hierarchical levels.
# - Convert between flat and hierarchical representations using `set_index()` and `reset_index()`.

# ## Setup: Creating Sample Hierarchical Data
# We construct a dataset tracking Australian retail store performance across states and cities.

# In[1]:


import numpy as np
import pandas as pd

# Define state and city hierarchy
states = ["NSW", "NSW", "VIC", "VIC", "QLD", "QLD"]
cities = ["Sydney", "Newcastle", "Melbourne", "Geelong", "Brisbane", "Gold Coast"]

multi_idx = pd.MultiIndex.from_arrays([states, cities], names=["State", "City"])

data = {
    "Sales_K_AUD": [850.5, 320.0, 780.0, 290.5, 620.0, 410.0],
    "Customer_Count": [4500, 1800, 4200, 1600, 3400, 2200],
}

df = pd.DataFrame(data, index=multi_idx)
print("--- 1. MultiIndex DataFrame Created ---")
print(df)


# ## Code Snippets: Indexing, Slicing, and Aggregating
#
# ### 1. Slicing with .loc[]
# Access data by outer level, or by outer and inner level tuple.

# In[2]:


# Select all cities in NSW (outer level)
nsw_data = df.loc["NSW"]
print("\n--- 2. Outer Level Selection (.loc['NSW']) ---")
print(nsw_data)

# Select a specific city by tuple (outer, inner)
sydney_record = df.loc[("NSW", "Sydney")]
print("\n--- Specific City Selection (.loc[('NSW', 'Sydney')]) ---")
print(sydney_record)


# ### 2. Cross-Section Selection with .xs()
# The `.xs()` method lets you slice directly at an inner level without needing to specify all outer levels.

# In[3]:


# Select Melbourne record directly using its inner level name
melb_xs = df.xs("Melbourne", level="City")
print("\n--- 3. Cross-Section (.xs('Melbourne', level='City')) ---")
print(melb_xs)


# ### 3. Level-Based Aggregations
# Compute summary statistics grouped directly by hierarchical index levels.

# In[4]:


# Total sales and customers by State
state_totals = df.groupby(level="State").sum()
print("\n--- 4. Grouped Totals by Outer Level (State) ---")
print(state_totals)

# Average sales by State
state_means = df.groupby(level="State")["Sales_K_AUD"].mean()
print("\nAverage Sales (K AUD) by State:")
print(state_means.round(1))


# ### 4. Converting Between Flat and Hierarchical Data
# Use `.reset_index()` to flatten a MultiIndex into regular columns, and `.set_index()` to promote columns to a MultiIndex.

# In[5]:


# Flatten MultiIndex into regular columns
flat_df = df.reset_index()
print("\n--- 5. Flattened DataFrame (.reset_index()) ---")
print(flat_df)

# Re-create MultiIndex from columns
restored_df = flat_df.set_index(["State", "City"])
print("\nRestored MultiIndex equals original?", restored_df.equals(df))


# ## Enrichment
# ### Swapping Index Levels
# Rearrange the hierarchy using `.swaplevel()`:
# ```python
# city_first_df = df.swaplevel('State', 'City').sort_index()
# print(city_first_df)
# ```
#
# ### Hierarchical Columns
# MultiIndex can also be applied to columns (e.g., Year -> Metric):
# ```python
# col_idx = pd.MultiIndex.from_product([['2025', '2026'], ['Sales', 'Profit']])
# ```

# ## Takeaways
# - A MultiIndex represents multi-dimensional relationships inside a 2D DataFrame.
# - Use `df.loc['OuterKey']` for outer level slicing; use `df.loc[('OuterKey', 'InnerKey')]` for precise tuples.
# - Use `df.xs(key, level='LevelName')` to slice through inner levels directly.
# - Aggregate by index levels using `df.groupby(level='LevelName').sum()`.
# - Use `set_index(['col1', 'col2'])` and `reset_index()` to move between flat and hierarchical schemas.

# ## Conclusion
# Hierarchical indexing allows sophisticated grouping, multi-level modeling, and compact representation of complex enterprise datasets.

# ## Exercises
#
# **Exercise 1:** Select all records for the state `VIC` from `df`.
#
# **Exercise 2:** Compute the average `Customer_Count` for each State using `df.groupby(level='State')`.
#
# **Exercise 3:** Use `.xs()` to select the record for `"Gold Coast"` at the `City` level.

# In[6]:


# --- Solutions ---

print("\n=== Exercise Solutions ===")

# Exercise 1 Solution:
vic_data = df.loc["VIC"]
print("Exercise 1 (VIC records):")
print(vic_data)

# Exercise 2 Solution:
avg_customers = df.groupby(level="State")["Customer_Count"].mean()
print("\nExercise 2 (Average Customer Count by State):")
print(avg_customers)

# Exercise 3 Solution:
gc_record = df.xs("Gold Coast", level="City")
print("\nExercise 3 (Gold Coast via .xs):")
print(gc_record)
