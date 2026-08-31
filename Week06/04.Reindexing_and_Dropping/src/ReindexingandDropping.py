#!/usr/bin/env python
# coding: utf-8

# # Reindexing and Dropping
#
# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vuhung/ACU-ITEC102/blob/main/Week06/04.Reindexing_and_Dropping/notebooks/reindexing_and_dropping.ipynb)
#
# ## Overview
# Reindexing and Dropping Rows/Columns.
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

# Reordering the rows
reordered = students.reindex(["S3", "S1", "S2"])
print("Reordered DataFrame:")
print(reordered)

# Dropping the 'Age' column (axis=1 means columns)
no_age = students.drop("Age", axis=1)
print("\nDataFrame without Age column:")
print(no_age)


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
