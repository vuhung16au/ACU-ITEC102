#!/usr/bin/env python
# coding: utf-8

# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week03/04.Dictionaries/notebooks/04.Dictionaries.ipynb)
# [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/vuhung16au/ACU-ITEC102/blob/main/Week03/04.Dictionaries/notebooks/04.Dictionaries.ipynb)
# [![Open In SageMaker Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/vuhung16au/ACU-ITEC102/blob/main/Week03/04.Dictionaries/notebooks/04.Dictionaries.ipynb)
#

# # Dictionaries — Key-Value Pairs
#
# [Open this notebook in Google Colab](https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week03/04.Dictionaries/notebooks/04.Dictionaries.ipynb)
#
# ## Overview
# Dictionaries map unique keys to values, acting like a database index or a phonebook. You provide a 'key' (a name), and it gives you the 'value' (the phone number).

# ## Code Snippets

# In[1]:


# Creating a dictionary for a student
student_grades = {"Farshid": 85, "Alice": 92, "Bob": 78}

# Accessing data via the Key
print(f"Alice's grade is: {student_grades['Alice']}")

# Adding a new key-value pair
student_grades["Charlie"] = 99
print(student_grades)


# ## Enrichment
# **Accessing Dicts Safely**: If you try to access a dictionary key that doesn't exist (e.g., `my_dict['missing']`), your code will crash. Use the `.get()` method instead (`my_dict.get('missing', 'Not Found')`), which safely returns a default value instead of crashing. Note: Dictionary keys must be immutable (Strings, Integers, Tuples).

# ## Takeaways
# - Dictionaries are unordered (historically) key-value pairs.
# - Accessed via keys, not index numbers.
# - Created using curly braces with colons `{key: value}`.

# ## Conclusion
# Dictionaries are essential when you need to map relationships, like Student ID to a Name.

# ## Exercises

# In[2]:


# Exercise: Create a dictionary containing your name, age, and major.
# Safely retrieve your 'GPA' from the dictionary using the .get() method, providing 'N/A' as the default.

# --- Solution ---
# my_info = {"name": "John", "age": 20, "major": "IT"}
# gpa = my_info.get("GPA", "N/A")
# print(f"My GPA is {gpa}")
