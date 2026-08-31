#!/usr/bin/env python
# coding: utf-8

# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week03/03.Sets/notebooks/03.Sets.ipynb)
# [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/vuhung16au/ACU-ITEC102/blob/main/Week03/03.Sets/notebooks/03.Sets.ipynb)
# [![Open In SageMaker Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/vuhung16au/ACU-ITEC102/blob/main/Week03/03.Sets/notebooks/03.Sets.ipynb)
#

# # Sets — Unordered, Unique Items
#
# [Open this notebook in Google Colab](https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week03/03.Sets/notebooks/03.Sets.ipynb)
#
# ## Overview
# This notebook introduces Sets. Sets are like an exclusive VIP club—no duplicates are allowed. They are unordered collections of unique items.

# ## Code Snippets

# In[1]:


# Using a set to clean up messy, duplicate data
messy_responses = ["Python", "Java", "Python", "C++", "Java", "Python"]
unique_languages = set(messy_responses)

print(f"Unique languages requested: {unique_languages}")

# Adding to a set
unique_languages.add("R")
print(f"Updated languages: {unique_languages}")


# ## Enrichment
# **Big-O Notation: Why Sets are Magic**: When you search for an item in a List containing 10 million rows, Python checks row 1, then row 2, all the way to the end (Time Complexity: O(N)). If you convert that List to a Set, Python uses a mathematical hash function to jump instantly to the item (Time Complexity: O(1)). For data scientists, converting lists to sets before searching them can reduce a 5-hour script to a 5-second script.

# ## Takeaways
# - Sets are unordered and hold unique values only.
# - Created using curly braces `{}` or the `set()` function.
# - Never try to access the 'first' item in a Set using `my_set[0]`. Sets do not record order.

# ## Conclusion
# If you need lightning-fast duplicate removal or membership testing, rely on a Set.

# ## Exercises

# In[2]:


# Exercise: Given a list of user IDs with duplicates, convert it into a set to find the unique users.
user_ids = [101, 102, 101, 103, 104, 102]

# --- Solution ---
# unique_users = set(user_ids)
# print(unique_users)
