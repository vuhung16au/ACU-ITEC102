#!/usr/bin/env python
# coding: utf-8

# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week03/01.Lists/notebooks/01.Lists.ipynb)
# [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/vuhung16au/ACU-ITEC102/blob/main/Week03/01.Lists/notebooks/01.Lists.ipynb)
# [![Open In SageMaker Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/vuhung16au/ACU-ITEC102/blob/main/Week03/01.Lists/notebooks/01.Lists.ipynb)
#

# # Lists — Ordered, Mutable Data
#
# [Open this notebook in Google Colab](https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week03/01.Lists/notebooks/01.Lists.ipynb)
#
# ## Overview
# In this notebook, we will explore Python Lists. Lists are ordered, mutable sequences that can store any type of data. Think of a list like your weekly Coles or Woolworths shopping list. You can change it anytime—add items, remove them, or swap them around.

# ## Code Snippets

# In[1]:


# Creating and modifying a list
aussie_cities = ["Sydney", "Melbourne", "Brisbane"]

# Adding an item (Append adds to the end)
aussie_cities.append("Perth")

# Removing an item
aussie_cities.remove("Melbourne")

# Sorting alphabetically
aussie_cities.sort()
print(f"My travel itinerary: {aussie_cities}")


# ## Enrichment
# Lists are highly versatile but can be slow for searching if they contain millions of rows. Since they are mutable, Python has to over-allocate memory for them just in case you decide to `.append()` more items later.

# ## Takeaways
# - Lists are ordered and mutable (changeable).
# - Created using square brackets `[]`.
# - Support methods like `.append()`, `.remove()`, and `.sort()`.

# ## Conclusion
# Lists are your go-to data structure when you need a collection of items that might change over time.

# ## Exercises

# In[2]:


# Exercise: Create a list of your top 3 favorite movies.
# Add a 4th movie to the end of the list, then remove the first movie.
# Print the final list.

# Hint: Use .append() and .pop(0) or .remove().

# --- Solution ---
# movies = ["Inception", "The Matrix", "Interstellar"]
# movies.append("Dune")
# movies.pop(0) # or movies.remove("Inception")
# print(movies)
