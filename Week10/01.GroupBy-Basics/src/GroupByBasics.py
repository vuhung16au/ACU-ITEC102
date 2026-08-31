#!/usr/bin/env python
# coding: utf-8

# # 01.GroupBy-Basics
#
# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week10/01.GroupBy-Basics/notebooks/01_01.GroupBy-Basics.ipynb)
#
# ## Overview
#
# This notebook explores the concepts of 01.GroupBy Basics.
#

# In[1]:


# Setup: Import libraries and generate synthetic data for the exercises
import pandas as pd
import numpy as np

# Create synthetic dataset
data = {
    "Store": ["Sydney", "Sydney", "Melbourne", "Brisbane", "Melbourne", "Brisbane"],
    "Year": [2022, 2023, 2022, 2022, 2023, 2023],
    "Sales": [100, 150, 300, 200, 320, 210],
    "Staff": [5, 5, 10, 8, 12, 9],
}
df = pd.DataFrame(data)
print(df.head())


# ## Code Snippets
#
# Here are some code examples demonstrating the core concepts.

# In[2]:


# Example code placeholder
total_sales = df.groupby("Store")["Sales"].sum()
print(total_sales)


# ## Enrichment
#
# Advanced topics related to this module.

# ## Exercises
#
# Try to apply what you've learned.

# In[3]:


# Exercise 1: Group by Store and Year, and find the average Sales
# Hint:
# df.groupby(['Store', 'Year'])['Sales'].mean()


# ## Takeaways
#
# - Use `.groupby()` to aggregate data.
# - Use `pivot_table` for 2D reports.
#
# ## Conclusion
#
# We have covered essential skills in data aggregation.
