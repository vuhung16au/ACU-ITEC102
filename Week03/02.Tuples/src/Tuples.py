#!/usr/bin/env python
# coding: utf-8

# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week03/02.Tuples/notebooks/02.Tuples.ipynb)
# [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/vuhung16au/ACU-ITEC102/blob/main/Week03/02.Tuples/notebooks/02.Tuples.ipynb)
# [![Open In SageMaker Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/vuhung16au/ACU-ITEC102/blob/main/Week03/02.Tuples/notebooks/02.Tuples.ipynb)
#

# # Tuples — Ordered, Immutable Data
#
# [Open this notebook in Google Colab](https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week03/02.Tuples/notebooks/02.Tuples.ipynb)
#
# ## Overview
# In this notebook, we focus on Python Tuples. Tuples are ordered, immutable sequences. They are like your passport details—fixed and unable to be changed once issued.

# ## Code Snippets

# In[1]:


# Creating a tuple
student_record = ("Liam", 98765432, "Data Science Major")

# Accessing elements works exactly like lists (0-indexed)
print(f"Student Name: {student_record[0]}")

# Uncommenting the next line will cause a TypeError! Tuples are locked.
# student_record[1] = 11111111


# ## Enrichment
# **Memory Efficiency of Tuples**: Because Tuples are immutable, Python allocates exactly the right amount of memory. For large, static datasets (like historical climate coordinates), using Tuples instead of Lists saves significant RAM.

# ## Takeaways
# - Tuples are ordered and immutable (locked).
# - Created using round brackets `()`.
# - Faster and more memory-efficient than lists for fixed data.

# ## Conclusion
# If your data must be protected from accidental tampering or is completely static, use a Tuple.

# ## Exercises

# In[2]:


# Exercise: Create a tuple representing the coordinates of a city (latitude, longitude).
# Try to change the latitude and observe the error.

# --- Solution ---
# coords = (-33.8688, 151.2093)
# print(coords)
# coords[0] = -34.0  # This will raise a TypeError
