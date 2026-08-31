#!/usr/bin/env python
# coding: utf-8

# # Sampling
#
# <a href="https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week08/05.Sampling/notebooks/05-sampling.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
#
# ## Overview
# This notebook covers the concepts and practical applications of Sampling in Pandas.

# ## Setup: Generate Dummy Data
# First, let's create a synthetic dataset containing missing values (NaN) to work with.

# In[1]:


import pandas as pd
import numpy as np

# Create a dummy student dataset with missing data
data = {
    "StudentID": range(1, 101),
    "Name": [f"Student_{i}" for i in range(1, 101)],
    "Age": np.random.randint(18, 25, 100).astype(float),
    "Score": np.random.randint(40, 100, 100).astype(float),
    "Status": ["Pass", "Fail"] * 50,
}
df = pd.DataFrame(data)

# Inject missing data randomly
np.random.seed(42)
for col in ["Age", "Score"]:
    indices = np.random.choice(df.index, size=15, replace=False)
    df.loc[indices, col] = np.nan

df.to_csv("messy_student_data.csv", index=False)
print("Created messy_student_data.csv")


# ## Code Snippets
# Here are some examples demonstrating the concepts.

# In[2]:


import pandas as pd

# Replace with specific topic code
pass


# ## Enrichment
# ### Imputation Algorithms
# Advanced data scientists use algorithms like *K-Nearest Neighbours (KNN)* to guess missing values based on similarities in other columns.
#
# ### Stratified Sampling
# If you pull a random 10% sample of Australians, you might accidentally select zero people from Tasmania just purely by chance. *Stratified Sampling* ensures that the random sample perfectly mimics the demographic ratios of the entire population.

# ## Takeaways
# - Data Cleaning is the unglamorous but utterly essential core of data analytics.
# - `.dropna()` deletes rows with missing values (fast but causes data loss).
# - `.fillna()` replaces missing values.
# - Binning simplifies exact numbers into broad categories.
# - Sampling pulls a random fraction of a massive dataset to speed up testing.

# ## Conclusion
# By mastering dropna, fillna, pd.cut, and sample, you can rescue broken datasets and categorise them into clean, actionable business intelligence.

# ## Exercises
# **Exercise 1:** Try loading the `messy_student_data.csv` file into a DataFrame and use `.isnull().sum()` to count the missing values.
#
# *Hint: Use `pd.read_csv()` and `.isnull().sum()`*

# In[3]:


# Write your code here

# --- Solution ---
# df = pd.read_csv('messy_student_data.csv')
# print(df.isnull().sum())
