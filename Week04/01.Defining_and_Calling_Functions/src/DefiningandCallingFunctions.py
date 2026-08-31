#!/usr/bin/env python
# coding: utf-8

# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week04/01.Defining_and_Calling_Functions/notebooks/01_functions.ipynb)
# [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/vuhung16au/ACU-ITEC102/blob/main/Week04/01.Defining_and_Calling_Functions/notebooks/01_functions.ipynb)
# [![Open In SageMaker Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/vuhung16au/ACU-ITEC102/blob/main/Week04/01.Defining_and_Calling_Functions/notebooks/01_functions.ipynb)
#

# # Overview
# This notebook covers **Defining and Calling Functions**.

# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vuhung/ACU-ITEC102/blob/main/Week04/01.Defining_and_Calling_Functions/notebooks/01_functions.ipynb)
#
# *Note: If the GitHub repository is private or not updated yet, you can download this `.ipynb` file and upload it manually at https://colab.research.google.com/*

# ## Code Snippets
# Here are the code examples demonstrating the concepts.

# In[1]:


def calculate_discount(price, discount_rate=0.10):
    return price - (price * discount_rate)


print(f"Discounted price: ${calculate_discount(100)}")


# ## Enrichment
# Advanced topics and additional information.

# ## Takeaways
# Key points covered in this notebook.

# ## Conclusion
# Summary of the content and its relevance.

# ## Exercises
# Interactive exercises for practice.

# In[2]:


# Try it yourself:

# Solution:
# print('Hello World')
