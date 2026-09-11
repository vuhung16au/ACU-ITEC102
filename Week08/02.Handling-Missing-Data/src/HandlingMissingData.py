#!/usr/bin/env python
# coding: utf-8

# # Handling Missing Data
#
# <a href="https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week08/02.Handling-Missing-Data/notebooks/02-handling-missing-data.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
#
# ## Overview
# Missing data is ubiquitous in data science. Before feeding data into models or reports, analysts must decide whether to **drop** incomplete records or **impute** them.
#
# In this module, you will learn how to detect missing values, inspect affected rows, and apply various dropping strategies using `df.dropna()`. You will also evaluate the trade-offs and risks of data loss.

# ## Setup: Locate Sample Dataset
# We locate `messy_student_data.csv`.

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


# ## Code Snippets: Missing Data Detection & Dropping Strategies
#
# ### 1. Locating Missing Data Rows
# Use `.isna().any(axis=1)` to pull out all records containing one or more missing fields.

# In[2]:


rows_with_nulls = df[df.isna().any(axis=1)]
print("--- 1. Rows with Incomplete Information ---")
print(f"Total incomplete rows: {len(rows_with_nulls)}")
print(rows_with_nulls.head(6))


# ### 2. Dropping Strategy A: Any Null (Default dropna)
# `df.dropna()` (or `df.dropna(how='any')`) eliminates any row that contains even a single null.

# In[3]:


df_drop_any = df.dropna()
data_loss_pct = ((len(df) - len(df_drop_any)) / len(df)) * 100

print("\n--- 2. Default dropna() (how='any') ---")
print(f"Original row count: {len(df)}")
print(f"Remaining row count: {len(df_drop_any)}")
print(f"Data loss: {data_loss_pct:.1f}%")


# ### 3. Dropping Strategy B: All Nulls (how='all')
# `df.dropna(how='all')` only drops a row if *every single column* is missing.

# In[4]:


# Add an empty record for demonstration
df_with_empty = pd.concat([df, pd.DataFrame([{col: np.nan for col in df.columns}])], ignore_index=True)
print(f"\n--- 3. Dropping Only Completely Blank Rows (how='all') ---")
print(f"Total rows with blank entry: {len(df_with_empty)}")
df_drop_all = df_with_empty.dropna(how="all")
print(f"Rows after dropna(how='all'): {len(df_drop_all)}")


# ### 4. Dropping Strategy C: Targeted Dropping with subset=[...]
# In education analytics, a student record without a test `Score` cannot be graded, but a record missing `Age` might still be valid for pass/fail metrics. Use `subset` to only drop when essential columns are null.

# In[5]:


# Drop only if Score is missing
df_drop_score_na = df.dropna(subset=["Score"])
print(f"\n--- 4. Targeted Dropping (subset=['Score']) ---")
print(f"Rows with valid Score: {len(df_drop_score_na)}")
print(f"Missing Scores dropped: {len(df) - len(df_drop_score_na)}")
print(f"Remaining missing Ages preserved: {df_drop_score_na['Age'].isna().sum()}")


# ### 5. Dropping Strategy D: Minimum Threshold with thresh=k
# Keep rows that contain at least `k` non-null values.

# In[6]:


# Keep rows with at least 4 valid values (out of 5 total columns)
df_thresh = df.dropna(thresh=4)
print(f"\n--- 5. Threshold Dropping (thresh=4 of 5 columns) ---")
print(f"Rows preserved with at least 4 valid columns: {len(df_thresh)}")


# ## Enrichment
# ### Converting Sentinel Values to NaN
# Data exported from legacy systems often marks missing data with `-999`, `"N/A"`, or `"?"`. Convert them before dropping:
# ```python
# df['Score'] = df['Score'].replace(-999, np.nan)
# df = df.dropna(subset=['Score'])
# ```

# ## Takeaways
# - Inspect which columns contain missing values using `df.isna().sum()` before deciding on a strategy.
# - Default `dropna()` (`how='any'`) is simple but can discard a significant percentage of observations.
# - Use `subset=['ColName']` to restrict row dropping to mission-critical fields.
# - Use `thresh=k` to enforce minimum acceptable data density per row.
# - Always calculate and report the percentage of data lost when dropping rows.

# ## Conclusion
# Dropping missing data should be done with deliberate intent. Targeted dropping via `subset` protects valuable data in secondary columns while removing invalid rows.

# ## Exercises
#
# **Exercise 1:** Drop only rows where `Age` is missing. How many rows remain?
#
# **Exercise 2:** Calculate the percentage of rows retained when dropping rows missing `Score`.
#
# **Exercise 3:** Drop any column that contains more than 10 missing values using `axis=1`.

# In[7]:


# --- Solutions ---

print("\n=== Exercise Solutions ===")

# Exercise 1 Solution:
df_age_clean = df.dropna(subset=["Age"])
print(f"Exercise 1: Rows remaining after dropping missing Age: {len(df_age_clean)}")

# Exercise 2 Solution:
retained_pct = (len(df.dropna(subset=["Score"])) / len(df)) * 100
print(f"Exercise 2: Percentage of rows retained: {retained_pct:.1f}%")

# Exercise 3 Solution:
# Drop columns with > 10 missing values
cols_to_drop = [col for col in df.columns if df[col].isna().sum() > 10]
df_cols_dropped = df.drop(columns=cols_to_drop)
print(f"Exercise 3: Dropped columns {cols_to_drop}. Remaining columns: {list(df_cols_dropped.columns)}")
