#!/usr/bin/env python
# coding: utf-8

# # 05.Reshaping-Data-Pivot-and-Melt
#
# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week09/05.Reshaping-Data-Pivot-and-Melt/notebooks/01_05.Reshaping-Data-Pivot-and-Melt.ipynb)
#
# ## Overview
#
# This notebook explores the concepts of 05.Reshaping Data Pivot and Melt.
#

# In[1]:


# Setup: Import libraries and generate synthetic data for the exercises
import pandas as pd
import numpy as np

# Create synthetic dataset
students = pd.DataFrame({"id": [1, 2, 3], "name": ["Alice", "Bob", "Charlie"]})
grades = pd.DataFrame({"id": [2, 3, 4], "grade": ["A", "B", "C"]})
print(students.head())
print(grades.head())


# ## Code Snippets
#
# Here are some code examples demonstrating the core concepts.

# In[2]:


# Example code placeholder
merged_table = pd.merge(students, grades, on="id", how="inner")
print(merged_table)


# ## Enrichment
#
# Advanced topics related to this module.

# ## Exercises
#
# Try to apply what you've learned.

# In[3]:


# Exercise 1: Perform a left join on students and grades
# Hint:
# left_join = pd.merge(students, grades, on='id', how='left')


# ## Takeaways
#
# - Use pd.merge() to join dataframes.
# - Default to left joins when in doubt.
# - Always verify your merges.
#
# ## Conclusion
#
# We have covered essential skills in data wrangling.
