#!/usr/bin/env python
# coding: utf-8

# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week04/06.Mini_Project_Survey_Data/notebooks/06_survey_project.ipynb)
# [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/vuhung16au/ACU-ITEC102/blob/main/Week04/06.Mini_Project_Survey_Data/notebooks/06_survey_project.ipynb)
# [![Open In SageMaker Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/vuhung16au/ACU-ITEC102/blob/main/Week04/06.Mini_Project_Survey_Data/notebooks/06_survey_project.ipynb)
#

# # Overview
# This notebook covers **Mini Project (Survey Data)**.

# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vuhung/ACU-ITEC102/blob/main/Week04/06.Mini_Project_Survey_Data/notebooks/06_survey_project.ipynb)
#
# *Note: If the GitHub repository is private or not updated yet, you can download this `.ipynb` file and upload it manually at https://colab.research.google.com/*

# ## Code Snippets
# Here are the code examples demonstrating the concepts.

# In[1]:


def run_survey():
    city = input("What is your favourite Australian city? ")
    with open("survey_results.txt", "a") as file:
        file.write(city + "\n")


if __name__ == "__main__":
    pass  # run_survey()


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
