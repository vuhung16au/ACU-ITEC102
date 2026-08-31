#!/usr/bin/env python
# coding: utf-8

# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week02/05.Loops/notebooks/loops.ipynb)
# [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/vuhung16au/ACU-ITEC102/blob/main/Week02/05.Loops/notebooks/loops.ipynb)
# [![Open In SageMaker Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/vuhung16au/ACU-ITEC102/blob/main/Week02/05.Loops/notebooks/loops.ipynb)
#

# # Overview: Loops (for, while) and Loop Control
# Loops automate repetitive tasks.
#
# This notebook can be run locally using Jupyter or on Google Colab.

# ## Code Snippets
# Below are code examples demonstrating the concepts.

# In[1]:


# Using a for loop with range()
print("Countdown starting...")
for i in range(5, 0, -1):
    print(i)
print("Blastoff!")

# Using a while loop with a 'break' statement
coffee_cups_drunk = 0
while True:  # This is an infinite loop!
    coffee_cups_drunk += 1
    print(f"Drinking cup {coffee_cups_drunk}...")

    if coffee_cups_drunk == 3:
        print("Okay, I have had enough coffee. Stopping.")
        break  # This forcefully exits the infinite loop


# ## Enrichment
# **List Comprehensions**
#
# Python developers often use list comprehensions to write loops in a single, highly optimized line of code.

# In[2]:


# Standard Loop
squares = []
for x in range(5):
    squares.append(x**2)

# List Comprehension (Pythonic way)
fast_squares = [x**2 for x in range(5)]
print(f"List comprehension result: {fast_squares}")


# ## Takeaways
# Review the key syntax and concepts covered in this notebook.

# ## Conclusion
# You should now be comfortable with these basic Python structures.

# ## Exercises
# Complete the exercise below. A solution is provided in the comments.

# In[3]:


# Exercise 1: Use a for loop and range() to print the even numbers from 2 to 10.
# Hint: range(start, stop, step)

# Solution:
# for i in range(2, 11, 2):
#     print(i)
