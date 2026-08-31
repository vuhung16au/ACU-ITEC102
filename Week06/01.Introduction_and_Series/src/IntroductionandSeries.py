#!/usr/bin/env python
# coding: utf-8

# # Introduction to Pandas and Series
#
# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vuhung/ACU-ITEC102/blob/main/Week06/01.Introduction_and_Series/notebooks/introduction_and_series.ipynb)
#
# ## Overview
# What is Pandas and how to use Pandas Series (1D data with labels).
#

# ## Code Snippet 1
#
# Brief explanation of the code snippet.

# In[1]:


import pandas as pd

# Creating a Series with labels
temps = pd.Series([22, 26, 19], index=["Sydney", "Melbourne", "Brisbane"])
print(temps)
print(f"\nMelbourne Temperature: {temps.loc['Melbourne']}")

# Adding a new city is easy
temps.loc["Perth"] = 24
print(f"\nUpdated Series:\n{temps}")


# ## Enrichment
#
# Advanced topics or additional information with sample code snippets for students who want to explore further.

# ## Takeaways
#
# - Summary of key points.

# ## Conclusion
#
# Brief conclusion summarizing the notebook's content.

# ## Exercises
#
# Interactive exercises for students to practice the concepts.

# In[2]:


# Exercise 1: Write your code here

# Hint: Think about what function to use.
# Solution:
# print('Hello World')
