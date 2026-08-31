#!/usr/bin/env python
# coding: utf-8

# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week02/04.Conditionals/notebooks/conditionals.ipynb)
# [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/vuhung16au/ACU-ITEC102/blob/main/Week02/04.Conditionals/notebooks/conditionals.ipynb)
# [![Open In SageMaker Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/vuhung16au/ACU-ITEC102/blob/main/Week02/04.Conditionals/notebooks/conditionals.ipynb)
#

# # Overview: Conditional Statements (if, elif, else)
# Conditional statements give our programs a brain.
#
# This notebook can be run locally using Jupyter or on Google Colab.

# ## Code Snippets
# Below are code examples demonstrating the concepts.

# In[1]:


# Simulating a grading system
score = 85

if score >= 85:
    grade = "High Distinction"
elif score >= 75:
    grade = "Distinction"
elif score >= 65:
    grade = "Credit"
elif score >= 50:
    grade = "Pass"
else:
    grade = "Fail"

print(f"Your grade is: {grade}")


# ## Enrichment
# **Truthiness and Ternary Operators**
#
# Empty objects (like '', 0, [], None) evaluate to False. You can also write one-line if statements called Ternary Operators.

# In[2]:


# Truthiness
user_input = ""
if not user_input:
    print("No input provided!")

# Ternary Operator
score = 80
result = "Pass" if score >= 50 else "Fail"
print(f"Ternary result: {result}")


# ## Takeaways
# Review the key syntax and concepts covered in this notebook.

# ## Conclusion
# You should now be comfortable with these basic Python structures.

# ## Exercises
# Complete the exercise below. A solution is provided in the comments.

# In[3]:


# Exercise 1: Ask the user for their favorite color using input() and store it in `color`. If it is 'blue', print 'The sky is blue'. Otherwise print 'Nice color!'.
# Note: In a notebook, input() works interactively.
# Hint: Use if and else.

# Solution:
# color = input('Favorite color: ')
# if color.lower() == 'blue':
#     print('The sky is blue')
# else:
#     print('Nice color!')
