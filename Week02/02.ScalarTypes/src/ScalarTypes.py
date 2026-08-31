#!/usr/bin/env python
# coding: utf-8

# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week02/02.ScalarTypes/notebooks/scalar_types.ipynb)
# [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/vuhung16au/ACU-ITEC102/blob/main/Week02/02.ScalarTypes/notebooks/scalar_types.ipynb)
# [![Open In SageMaker Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/vuhung16au/ACU-ITEC102/blob/main/Week02/02.ScalarTypes/notebooks/scalar_types.ipynb)
#

# # Overview: Scalar Types & Type Conversion
# int, float, bool, str, bytes, and datetime.
#
# This notebook can be run locally using Jupyter or on Google Colab.

# ## Code Snippets
# Below are code examples demonstrating the concepts.

# In[1]:


# Explicit Conversion (Casting)
price_string = "45.50"
# We cannot do math with text, so we convert it to a float
price_float = float(price_string)
total_with_tax = price_float * 1.10
print(f"Total with tax: ${total_with_tax}")

# Implicit Conversion
# Python automatically converts an int and a float into a float
a = 10  # int
b = 2.5  # float
result = a + b
print(f"Result type: {type(result)}")  # Outputs <class 'float'>


# ## Conclusion
# You should now be comfortable with these basic Python structures.

# ## Enrichment
# **Complex Numbers and isinstance()**
#
# Python natively supports complex numbers (used in engineering and data science). Also, checking types should usually be done with isinstance() instead of type().

# In[2]:


# Complex numbers
c = 3 + 4j
print(f"Complex number: {c}, Real part: {c.real}, Imaginary: {c.imag}")

# Best practice for type checking
x = 10
if isinstance(x, int):
    print("x is definitely an integer!")


# ## Takeaways
# Review the key syntax and concepts covered in this notebook.

# ## Exercises
# Complete the exercise below. A solution is provided in the comments.

# In[3]:


# Exercise 1: You have a variable `age_str = "30"`. Convert it to an integer and add 5 to it, storing the result in a new variable `future_age`.
# Hint: Use the int() function.

# Solution:
# age_str = "30"
# future_age = int(age_str) + 5
# print(future_age)
