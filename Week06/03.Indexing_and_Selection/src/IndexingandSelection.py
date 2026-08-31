#!/usr/bin/env python
# coding: utf-8

# # Indexing and Selection
#
# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vuhung/ACU-ITEC102/blob/main/Week06/03.Indexing_and_Selection/notebooks/indexing_and_selection.ipynb)
#
# ## Overview
# Indexing and Selection: `.loc[]` vs `.iloc[]`.
#

# ## Code Snippet 1
#
# Brief explanation of the code snippet.

# In[1]:


import pandas as pd

student_data = {
    "Name": ["Farshid", "Brooke", "Casey"],
    "Score": [85, 92, 78],
    "Age": [21, 22, 20],
}
students = pd.DataFrame(student_data, index=["S1", "S2", "S3"])

# Using .loc (by label S1)
print("Using .loc (by label S1):")
print(students.loc["S1"])

# Using .iloc (by position 0)
print("\nUsing .iloc (by position 0):")
print(students.iloc[0])

# Selecting specific rows and columns
subset = students.loc[["S1", "S3"], ["Name", "Score"]]
print("\nSubset (S1 and S3, Name and Score only):")
print(subset)


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
