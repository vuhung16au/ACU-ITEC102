#!/usr/bin/env python
# coding: utf-8

# # 03.Bar-Charts
#
# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week11/03.Bar-Charts/notebooks/01_03.Bar-Charts.ipynb)
#
# ## Overview
#
# This notebook explores the concepts of 03.Bar Charts.
#

# In[1]:


# Setup: Import libraries and generate synthetic data for the exercises
import pandas as pd
import matplotlib.pyplot as plt

# Create synthetic dataset
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
rainfall = [1.2, 0.5, 3.8, 0.0, 2.5]
print("Data ready!")


# ## Code Snippets
#
# Here are some code examples demonstrating the core concepts.

# In[2]:


# Example code placeholder
plt.plot(days, rainfall, marker="o", color="purple")
plt.title("Weekly Rainfall")
plt.xlabel("Day")
plt.ylabel("Rainfall (mm)")
plt.grid(True)
plt.show()


# ## Enrichment
#
# Advanced topics related to this module.

# ## Exercises
#
# Try to apply what you've learned.

# In[3]:


# Exercise 1: Create a basic plot
# Hint:
# plt.plot(x_data, y_data)
# plt.show()


# ## Takeaways
#
# - Matplotlib is a powerful visualisation library.
# - Always include titles and labels.
# - Use plt.show() to render the plot.
#
# ## Conclusion
#
# We have covered essential skills in data visualisation.
