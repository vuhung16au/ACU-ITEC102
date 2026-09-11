#!/usr/bin/env python
# coding: utf-8

# # Data Binning (Discretisation)
#
# <a href="https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week08/04.Binning/notebooks/04-binning.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
#
# ## Overview
# In data analysis, continuous numerical values (such as test marks from 0 to 100 or ages from 18 to 65) are often easier to interpret and analyze when converted into discrete categorical groups or buckets. This process is called **binning** or **discretisation**.
#
# Common applications:
# - Converting continuous test scores into academic grades (Fail, Pass, Credit, Distinction, High Distinction).
# - Grouping customer ages into demographic brackets (18-24, 25-34, 35-49).
# - Segmenting income into quartiles.
#
# In this module, you will learn how to use `pd.cut()` for custom and equal-width intervals, and `pd.qcut()` for quantile-based equal-frequency bins.

# ## Setup: Locate Sample Dataset
# We locate `messy_student_data.csv` and impute missing values for clean binning.

# In[1]:


import os
from pathlib import Path
import numpy as np
import pandas as pd

current_dir = Path(__file__).resolve().parent if "__file__" in globals() else Path.cwd()
possible_paths = [
    current_dir / "messy_student_data.csv",
    current_dir / "notebooks" / "messy_student_data.csv",
    current_dir.parent / "notebooks" / "messy_student_data.csv",
    Path("messy_student_data.csv"),
    Path("notebooks/messy_student_data.csv"),
]

csv_file = None
for p in possible_paths:
    if p.exists():
        csv_file = p
        break

if csv_file is None:
    csv_file = Path("messy_student_data.csv")
    np.random.seed(42)
    df_fallback = pd.DataFrame({
        "StudentID": range(1, 101),
        "Name": [f"Student_{i}" for i in range(1, 101)],
        "Age": np.random.randint(18, 25, 100).astype(float),
        "Score": np.random.randint(40, 100, 100).astype(float),
        "Status": ["Pass", "Fail"] * 50,
    })
    for col in ["Age", "Score"]:
        indices = np.random.choice(df_fallback.index, size=15, replace=False)
        df_fallback.loc[indices, col] = np.nan
    df_fallback.to_csv(csv_file, index=False)

df = pd.read_csv(csv_file)
# Pre-clean missing scores and ages for binning demonstrations
df["Score"] = df["Score"].fillna(df["Score"].mean())
df["Age"] = df["Age"].fillna(df["Age"].median())
print(f"Loaded and pre-cleaned {len(df)} student records from {csv_file}\n")


# ## Code Snippets: Binning with pd.cut() and pd.qcut()
#
# ### 1. Custom Bin Edges: Australian Higher Education Grades
# Use `pd.cut()` with explicit interval boundaries and human-readable grade labels:
# - **Fail (N)**: 0 to < 50
# - **Pass (P)**: 50 to < 65
# - **Credit (C)**: 65 to < 75
# - **Distinction (D)**: 75 to < 85
# - **High Distinction (HD)**: 85 to 100

# In[2]:


# Define custom bin boundaries and corresponding grade labels
grade_bins = [0, 50, 65, 75, 85, 100]
grade_labels = ["Fail (N)", "Pass (P)", "Credit (C)", "Distinction (D)", "High Distinction (HD)"]

df["Grade"] = pd.cut(df["Score"], bins=grade_bins, labels=grade_labels, right=False)

print("--- 1. Australian Academic Grade Binning (pd.cut) ---")
print(df[["StudentID", "Name", "Score", "Grade"]].head(8))

print("\nGrade Frequency Distribution:")
print(df["Grade"].value_counts().sort_index())


# ### 2. Automatic Equal-Width Binning
# Passing an integer `bins=k` to `pd.cut()` automatically divides the range into `k` equal-width numerical ranges.

# In[3]:


# Divide student ages into 3 equal-width intervals
df["Age_Bracket"] = pd.cut(df["Age"], bins=3)
print(f"\n--- 2. Equal-Width Age Brackets ---")
print(df["Age_Bracket"].value_counts().sort_index())


# ### 3. Equal-Frequency Binning with pd.qcut() (Quantiles)
# While `pd.cut()` creates bins with equal numerical width, `pd.qcut()` creates bins with **equal numbers of observations** based on percentiles (e.g., quartiles).

# In[4]:


quartile_labels = ["Q1 (Lowest 25%)", "Q2 (Lower-Mid)", "Q3 (Upper-Mid)", "Q4 (Top 25%)"]
df["Score_Quartile"] = pd.qcut(df["Score"], q=4, labels=quartile_labels)

print("\n--- 3. Quartile Discretisation (pd.qcut) ---")
print("Observations per quartile:")
print(df["Score_Quartile"].value_counts().sort_index())


# ### 4. Cross-Tabulation Analysis
# Examine how categories correlate across cohorts using `pd.crosstab()`.

# In[5]:


print("\n--- 4. Cross-Tabulation: Grade vs Status ---")
print(pd.crosstab(df["Grade"], df["Status"]))


# ## Enrichment
# ### Left-Open vs Right-Closed Intervals
# By default, `pd.cut()` creates intervals that are left-open and right-closed: `(0, 50]` means greater than 0 up to and including 50.
# Setting `right=False` creates left-closed intervals: `[0, 50)` means 0 up to but not including 50.

# ## Takeaways
# - Binning simplifies continuous variance into actionable categorical levels.
# - Use `pd.cut()` when you have specific domain thresholds (e.g. university grade cutoffs).
# - Use `pd.qcut()` when you want balanced cohorts with an equal count of observations in each bucket.
# - Combine binned columns with `.value_counts()` and `pd.crosstab()` to analyze demographic breakdowns.

# ## Conclusion
# Discretising continuous metrics enables clear executive reporting, simplifies complex data patterns, and prepares features for classification models.

# ## Exercises
#
# **Exercise 1:** Bin student scores into 3 custom performance bands: `Low (<50)`, `Medium (50-74)`, `High (75-100)`.
#
# **Exercise 2:** Use `pd.qcut()` to split `Age` into 2 equal-sized groups: `Younger` and `Older`.
#
# **Exercise 3:** Display the count of students in each performance band from Exercise 1.

# In[6]:


# --- Solutions ---

print("\n=== Exercise Solutions ===")

# Exercise 1 Solution:
band_bins = [0, 50, 75, 100]
band_labels = ["Low (<50)", "Medium (50-74)", "High (75-100)"]
df["Performance_Band"] = pd.cut(df["Score"], bins=band_bins, labels=band_labels, right=False)
print("Exercise 1 Result (First 5 records):")
print(df[["Name", "Score", "Performance_Band"]].head())

# Exercise 2 Solution:
df["Age_Group"] = pd.qcut(df["Age"], q=2, labels=["Younger", "Older"])
print("\nExercise 2 Result (Age Group distribution):")
print(df["Age_Group"].value_counts())

# Exercise 3 Solution:
print("\nExercise 3 Result (Counts per Performance Band):")
print(df["Performance_Band"].value_counts().sort_index())
