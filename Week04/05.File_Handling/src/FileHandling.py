#!/usr/bin/env python
# coding: utf-8

# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week04/05.File_Handling/notebooks/05_file_handling.ipynb)
# [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/vuhung16au/ACU-ITEC102/blob/main/Week04/05.File_Handling/notebooks/05_file_handling.ipynb)
# [![Open In SageMaker Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/vuhung16au/ACU-ITEC102/blob/main/Week04/05.File_Handling/notebooks/05_file_handling.ipynb)
#

# # Overview
# This notebook covers **File Handling**.

# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vuhung/ACU-ITEC102/blob/main/Week04/05.File_Handling/notebooks/05_file_handling.ipynb)
#
# *Note: If the GitHub repository is private or not updated yet, you can download this `.ipynb` file and upload it manually at https://colab.research.google.com/*

# ## Code Snippets
# Here are the code examples demonstrating the concepts.

# In[1]:


with open("cities.txt", "a") as file:
    file.write("Sydney\n")

try:
    with open("cities.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")


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
