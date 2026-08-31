#!/usr/bin/env python
# coding: utf-8

# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week02/03.Operators/notebooks/operators.ipynb)
# [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/vuhung16au/ACU-ITEC102/blob/main/Week02/03.Operators/notebooks/operators.ipynb)
# [![Open In SageMaker Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/vuhung16au/ACU-ITEC102/blob/main/Week02/03.Operators/notebooks/operators.ipynb)
#

# # Overview: Arithmetic, Comparison, and Logical Operators
# Operators allow us to manipulate and compare data.
#
# This notebook can be run locally using Jupyter or on Google Colab.

# ## Code Snippets
# Below are code examples demonstrating the concepts.

# In[1]:


# Modulus is incredibly useful for finding even/odd numbers
number = 14
if number % 2 == 0:
    print("The number is even.")

# Logical Operators
is_weekend = True
is_sunny = False

if is_weekend and is_sunny:
    print("Let's go to Bondi Beach!")
elif is_weekend and not is_sunny:
    print("Let's stay indoors and code in Python.")


# ## Enrichment
# **The Walrus Operator (:=)**
#
# Introduced in Python 3.8, the walrus operator allows you to assign and evaluate a variable in a single expression.

# In[2]:


# Walrus operator example
sample_data = [1, 2, 3, 4, 5]
# Assigns n and evaluates if n > 3 simultaneously
if (n := len(sample_data)) > 3:
    print(f"List is long enough, it has {n} elements.")


# ## Takeaways
# Review the key syntax and concepts covered in this notebook.

# ## Conclusion
# You should now be comfortable with these basic Python structures.

# ## Exercises
# Complete the exercise below. A solution is provided in the comments.

# In[3]:


# Exercise 1: Write an expression using the modulus operator to check if 25 is odd.
# Hint: If a number % 2 is equal to 1, it is odd.

# Solution:
# num = 25
# if num % 2 == 1:
#     print('Odd')
