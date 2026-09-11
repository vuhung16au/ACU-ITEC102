#!/usr/bin/env python
# coding: utf-8

# # Introduction to Data Cleaning
#
# <a href="https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week08/01.Introduction-to-Data-Cleaning/notebooks/01-introduction-to-data-cleaning.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
#
# ## Overview
# In data science and software engineering, **raw data is rarely clean**. Industry surveys consistently report that data professionals spend up to 80% of their time cleaning and preprocessing data.
#
# Common data quality problems include:
# - Missing values (`NaN`, empty strings).
# - Duplicate observations.
# - Inconsistent or inappropriate data types.
# - Invalid or out-of-range values (e.g., negative test scores).
# - Untrimmed leading or trailing whitespace in text fields.
#
# In this module, you will learn the foundational workflow for auditing and cleaning a student performance dataset (`messy_student_data.csv`).

# ## Setup: Locate Sample Dataset
# We locate `messy_student_data.csv` reliably.

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
print(f"Loaded {len(df)} student records from {csv_file}\n")


# ## Code Snippets: Auditing and Cleaning Data
#
# ### 1. Auditing Dataset Health: info(), isna(), and shape
# The first step in any data cleaning workflow is auditing column types, row counts, and missing values.

# In[2]:


print("--- 1. Dataset Dimensions and First 5 Records ---")
print(f"Shape: {df.shape} (rows, columns)")
print(df.head())

print("\n--- Missing Value Audit ---")
missing = df.isna().sum()
print(missing)

print("\nMissing Percentages:")
print((df.isna().mean() * 100).round(1).astype(str) + "%")


# ### 2. Detecting and Removing Duplicate Rows
# Duplicates can silently skew sums, averages, and statistical models. Check with `.duplicated()` and remove with `.drop_duplicates()`.

# In[3]:


# Simulate duplicate row for demonstration
df_with_dupes = pd.concat([df, df.iloc[[0]]], ignore_index=True)
print(f"\n--- 2. Duplicate Detection ---")
print(f"Row count with duplicate: {len(df_with_dupes)}")
print(f"Duplicate rows detected: {df_with_dupes.duplicated().sum()}")

# Drop duplicate records
df_deduped = df_with_dupes.drop_duplicates()
print(f"Row count after .drop_duplicates(): {len(df_deduped)}")


# ### 3. Data Type Consistency
# In Pandas, integers containing `NaN` historically had to be stored as `float64`. Modern Pandas supports the nullable integer type `'Int64'` (capital 'I').

# In[4]:


print(f"\n--- 3. Data Types Before & After Conversion ---")
print("Original dtypes:")
print(df.dtypes)

# Convert Age to nullable Int64
df_typed = df.copy()
df_typed["Age"] = df_typed["Age"].astype("Int64")
print("\nAfter converting 'Age' to nullable Int64:")
print(df_typed[["StudentID", "Name", "Age"]].head(6))


# ### 4. Detecting Invalid / Out-of-Range Values
# Validate business rules (e.g., student score must be between 0 and 100).

# In[5]:


print(f"\n--- 4. Validating Numerical Bounds ---")
min_score = df["Score"].min()
max_score = df["Score"].max()
print(f"Score Range: {min_score} to {max_score}")

# Identify any scores outside valid 0-100 range
invalid_scores = df[(df["Score"] < 0) | (df["Score"] > 100)]
print(f"Invalid scores (<0 or >100): {len(invalid_scores)}")


# ### 5. Cleaning String Values (.str Accessor)
# Text data often contains unintended whitespace or inconsistent casing.

# In[6]:


print(f"\n--- 5. String Sanitisation ---")
sample_names = pd.Series(["  nguyen van ", "SARAH MILLER  ", " chloe smith "])
cleaned_names = sample_names.str.strip().str.title()
print("Raw strings:    ", list(sample_names))
print("Cleaned strings:", list(cleaned_names))


# ## Enrichment
# ### Data Completeness Ratio
# Quantify how much of the dataset has complete records across all columns:
# ```python
# completeness = (df.dropna().shape[0] / df.shape[0]) * 100
# print(f"Complete records: {completeness:.1f}%")
# ```

# ## Takeaways
# - Never analyze raw data without an initial audit (`.shape`, `.info()`, `.isna().sum()`).
# - Check for duplicate observations using `.duplicated()` and remove them with `.drop_duplicates()`.
# - Use nullable types like `'Int64'` when integer columns contain missing values.
# - Validate domain rules (e.g. check score boundaries) to detect data entry errors.
# - Clean string columns with `.str.strip()` and `.str.title()` / `.str.lower()`.

# ## Conclusion
# Data cleaning is an iterative, disciplined process. Clean data forms the reliable bedrock for all subsequent statistical analysis and predictive modeling.

# ## Exercises
#
# **Exercise 1:** Compute the overall completeness ratio of `df` (percentage of rows with zero missing values).
#
# **Exercise 2:** Create a copy of `df` with `Age` converted to `'Int64'` and display the first 3 rows.
#
# **Exercise 3:** Check if any student has a missing `Age` AND a missing `Score` simultaneously.

# In[7]:


# --- Solutions ---

print("\n=== Exercise Solutions ===")

# Exercise 1 Solution:
complete_rows = df.dropna().shape[0]
completeness_pct = (complete_rows / len(df)) * 100
print(f"Exercise 1: {complete_rows}/{len(df)} rows are complete ({completeness_pct:.1f}% completeness)")

# Exercise 2 Solution:
ex2_df = df.copy()
ex2_df["Age"] = ex2_df["Age"].astype("Int64")
print("\nExercise 2 (First 3 rows with Int64 Age):")
print(ex2_df.head(3))

# Exercise 3 Solution:
both_missing = df[df["Age"].isna() & df["Score"].isna()]
print(f"\nExercise 3: Students missing both Age and Score: {len(both_missing)}")
