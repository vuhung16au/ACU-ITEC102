#!/usr/bin/env python
# coding: utf-8

# # 04.Privacy-in-Action-Anonymisation
#
# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week12/04.Privacy-in-Action-Anonymisation/notebooks/01_04.Privacy-in-Action-Anonymisation.ipynb)
#
# ## Overview
#
# This notebook explores the concepts of 04.Privacy in Action Anonymisation.
#

# In[1]:


# Setup: Import libraries and generate synthetic data for the exercises
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Create synthetic dataset
data = {
    "Patient_ID": [f"P{i:03d}" for i in range(1, 11)],
    "Name": [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Eva",
        "Frank",
        "Grace",
        "Heidi",
        "Ivan",
        "Judy",
    ],
    "Age": np.random.randint(20, 80, 10),
    "Medical_Bill": np.random.uniform(500, 5000, 10).round(2),
    "Condition": np.random.choice(["Healthy", "Sick", "Recovering"], 10),
}
df = pd.DataFrame(data)
df.head()


# ## Code Snippets
#
# Here are some code examples demonstrating the core concepts.

# In[2]:


# Example code placeholder
print(df.isnull().sum())
df_clean = df.dropna()


# ## Enrichment
#
# Advanced topics related to this module.

# ## Exercises
#
# Try to apply what you've learned.

# In[3]:


# Exercise 1: Anonymise the 'Name' column in df
# Hint:
# df['Name'] = df['Patient_ID']


# ## Takeaways
#
# - Always check for missing values using `.isnull().sum()`.
# - Drop empty rows with `.dropna()`.
# - Ensure PII (Personally Identifiable Information) is anonymised.
#
# ## Conclusion
#
# We have covered essential skills in data wrangling and ethical data science.
