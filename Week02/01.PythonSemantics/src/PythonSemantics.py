#!/usr/bin/env python
# coding: utf-8

# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week02/01.PythonSemantics/notebooks/python_semantics.ipynb)
# [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/vuhung16au/ACU-ITEC102/blob/main/Week02/01.PythonSemantics/notebooks/python_semantics.ipynb)
# [![Open In SageMaker Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/vuhung16au/ACU-ITEC102/blob/main/Week02/01.PythonSemantics/notebooks/python_semantics.ipynb)
#

# # Overview: Python Semantics & Readability
# Indentation, variables, and comments.
#
# This notebook can be run locally using Jupyter or on Google Colab.

# ## Code Snippets
# Below are code examples demonstrating the concepts.

# In[1]:


# Variables store data. We don't need to declare their type beforehand.
student_name = "Alex"
age = 21

# Comments start with a hash symbol (#) and are ignored by the computer.
# Indentation matters! Notice the 4 spaces inside the 'if' block:
if age >= 18:
    print(f"{student_name} is allowed to vote.")
    print("This line is also inside the if block because it is indented.")
print("This line is outside the if block and will always run.")


# ## Enrichment
# **Type Hinting and PEP 8**
#
# While Python doesn't require type declarations, 'type hinting' is an advanced feature often used in modern Python to make code more readable and catch errors.

# In[2]:


# Type hinting example
def greet(name: str) -> str:
    return f"Hello {name}"


age: int = 21
print(greet("Alice"))


# ## Takeaways
# Review the key syntax and concepts covered in this notebook.

# ## Conclusion
# You should now be comfortable with these basic Python structures.

# ## Exercises
# Complete the exercise below. A solution is provided in the comments.

# In[3]:


# Exercise 1: Create a variable called 'temperature' and set it to 25. Then write an if statement that prints 'It is warm' if the temperature is greater than 20.
# Hint: Remember to indent the print statement by 4 spaces.

# Solution:
# temperature = 25
# if temperature > 20:
#     print('It is warm')
