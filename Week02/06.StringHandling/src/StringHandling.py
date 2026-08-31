#!/usr/bin/env python
# coding: utf-8

# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week02/06.StringHandling/notebooks/string_handling.ipynb)
# [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/vuhung16au/ACU-ITEC102/blob/main/Week02/06.StringHandling/notebooks/string_handling.ipynb)
# [![Open In SageMaker Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/vuhung16au/ACU-ITEC102/blob/main/Week02/06.StringHandling/notebooks/string_handling.ipynb)
#

# # Overview: String Handling Basics
# Slicing, formatting, and escape sequences.
#
# This notebook can be run locally using Jupyter or on Google Colab.

# ## Code Snippets
# Below are code examples demonstrating the concepts.

# In[1]:


# String Slicing: string[start:stop]
course_code = "ITEC102-Python"
print("Unit prefix:", course_code[0:7])  # Output: ITEC102

# Escape Sequences: \n for newline, \t for tab
report = "Name:\tAlice\nGrade:\tHD\nStatus:\tPassed"
print(report)


# ## Enrichment
# **Advanced f-String Formatting**
#
# f-strings can do math, format decimals, and even print variable names for debugging.

# In[2]:


# Advanced f-strings
pi = 3.14159265
print(f"Pi rounded to 2 decimals: {pi:.2f}")

# Debugging feature (Python 3.8+)
my_var = 100
print(f"{my_var=}")  # Prints my_var=100


# ## Takeaways
# Review the key syntax and concepts covered in this notebook.

# ## Conclusion
# You should now be comfortable with these basic Python structures.

# ## Exercises
# Complete the exercise below. A solution is provided in the comments.

# In[3]:


# Exercise 1: Extract the word 'Data' from the string `title = 'Introduction to Data Science'` using slicing.
# Hint: The word starts at index 16.

# Solution:
# title = 'Introduction to Data Science'
# word = title[16:20]
# print(word)
