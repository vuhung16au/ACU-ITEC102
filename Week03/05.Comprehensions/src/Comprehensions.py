#!/usr/bin/env python
# coding: utf-8

# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week03/05.Comprehensions/notebooks/05.Comprehensions.ipynb)
# [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/vuhung16au/ACU-ITEC102/blob/main/Week03/05.Comprehensions/notebooks/05.Comprehensions.ipynb)
# [![Open In SageMaker Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/vuhung16au/ACU-ITEC102/blob/main/Week03/05.Comprehensions/notebooks/05.Comprehensions.ipynb)
#

# # Comprehensions — Pythonic Shortcuts
#
# [Open this notebook in Google Colab](https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week03/05.Comprehensions/notebooks/05.Comprehensions.ipynb)
#
# ## Overview
# Comprehensions are the 'Pythonic' way to generate Collections in a single, fast, readable line of code, rather than writing a bulky `for` loop.

# ## Code Snippets

# In[1]:


# 1. List Comprehension (Extracting just the even numbers)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
print("Even numbers:", evens)

# 2. Dictionary Comprehension (Squaring numbers)
squares_dict = {x: x**2 for x in range(1, 6)}
print("Squares Dictionary:", squares_dict)


# ## Enrichment
# Comprehensions not only make your code more concise, but they often run slightly faster than traditional `for` loops in Python because the underlying implementation is written in C and optimized for appending elements.

# ## Takeaways
# - List Comprehensions: `[expression for item in iterable if condition]`.
# - Dictionary Comprehensions: `{key_expr: value_expr for item in iterable]`.
# - Set Comprehensions also exist!

# ## Conclusion
# Mastering comprehensions will make your Python code cleaner, faster, and more professional.

# ## Exercises

# In[2]:


# Exercise: Use a list comprehension to create a list of the first 10 perfect squares (1, 4, 9, 16...).

# --- Solution ---
# squares = [x**2 for x in range(1, 11)]
# print(squares)
