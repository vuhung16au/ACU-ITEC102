#!/usr/bin/env python
# coding: utf-8

# # Data Manipulation
#
# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vuhung/ACU-ITEC102/blob/main/Week06/05.Data_Manipulation/notebooks/data_manipulation.ipynb)
#
# ## Overview
# Data Manipulation: Filtering, Arithmetic, Sorting, and Ranking.
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

# Filtering: Keep students older than 20
older_students = students[students["Age"] > 20]
print("Students older than 20:")
print(older_students)

# Arithmetic: Add 5 bonus points to all scores
students["Score"] = students["Score"] + 5

# Sorting: Sort by Score (highest first)
sorted_students = students.sort_values(by="Score", ascending=False)
print("\nStudents after bonus and sorted by Score:")
print(sorted_students)

# Ranking / Finding the top scorer
top_scorer = students.loc[students["Score"].idxmax()]
print("\nTop Scorer:")
print(top_scorer)


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
