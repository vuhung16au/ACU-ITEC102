#!/usr/bin/env python
# coding: utf-8

# # Pandas DataFrames
#
# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vuhung/ACU-ITEC102/blob/main/Week06/02.Pandas_DataFrames/notebooks/pandas_dataframes.ipynb)
#
# ## Overview
# Pandas DataFrames: 2D data tables (Excel in Python).
#

# ## Code Snippet 1
#
# Brief explanation of the code snippet.

# In[1]:


import pandas as pd

# Creating a DataFrame from a dictionary
student_data = {
    "Name": ["Farshid", "Brooke", "Casey"],
    "Score": [85, 92, 78],
    "Age": [21, 22, 20],
}
students = pd.DataFrame(student_data, index=["S1", "S2", "S3"])

print("Original DataFrame:")
print(students)

# Changing a single value
students.loc["S2", "Score"] = 88
print("\nAfter updating Brooke's score:")
print(students)


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
