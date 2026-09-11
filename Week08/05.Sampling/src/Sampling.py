#!/usr/bin/env python
# coding: utf-8

# # Data Sampling
#
# <a href="https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week08/05.Sampling/notebooks/05-sampling.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
#
# ## Overview
# In modern data science, datasets often contain millions or billions of rows. Running complex exploratory analyses or prototyping algorithms on the entire dataset can be prohibitively slow.
#
# **Sampling** allows you to extract a representative subset of your data to speed up development, perform quality control audits, or create machine learning training/testing splits.
#
# In this module, you will learn how to:
# - Draw random samples by count (`n`) and fraction (`frac`).
# - Guarantee scientific reproducibility using `random_state`.
# - Sample with and without replacement (`replace=True/False`).
# - Perform **stratified sampling** to maintain balanced demographic representation.

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
print(f"Loaded full dataset of {len(df)} student records from {csv_file}\n")


# ## Code Snippets: Sampling Techniques
#
# ### 1. Simple Random Sampling by Count and Fraction
# Use `df.sample(n=k)` to draw `k` rows, or `df.sample(frac=p)` to draw a proportion `p` (e.g., 0.10 for 10%).

# In[2]:


# Sample exactly 5 random students
sample_5 = df.sample(n=5, random_state=42)
print("--- 1. Simple Random Sample (n=5) ---")
print(sample_5[["StudentID", "Name", "Score", "Status"]])

# Sample a 10% fraction of the total dataset
sample_10pct = df.sample(frac=0.10, random_state=42)
print(f"\n10% fraction sample size: {len(sample_10pct)} rows")


# ### 2. Reproducibility with random_state (Random Seed)
# When developing or testing data pipelines, reproducibility is essential. Setting `random_state` ensures that running the script multiple times produces the exact same sample.

# In[3]:


# Two separate samples with the exact same seed
sample_run_a = df.sample(n=3, random_state=102)
sample_run_b = df.sample(n=3, random_state=102)

print("\n--- 2. Seed Reproducibility Check ---")
print("Run A Student IDs:", list(sample_run_a["StudentID"]))
print("Run B Student IDs:", list(sample_run_b["StudentID"]))
print("Are both samples identical?", sample_run_a.equals(sample_run_b))


# ### 3. Sampling With vs. Without Replacement
# By default, `replace=False` ensures a row can only be picked once. Setting `replace=True` allows duplicate picks (used in Bootstrapping and Monte Carlo simulations).

# In[4]:


# Sample with replacement
sample_bootstrap = df.sample(n=8, replace=True, random_state=7)
print(f"\n--- 3. Sampling With Replacement (replace=True) ---")
print(f"Sample size: {len(sample_bootstrap)}, Unique StudentIDs: {sample_bootstrap['StudentID'].nunique()}")


# ### 4. Stratified Sampling with groupby().sample()
# When populations have unequal subgroup sizes, purely random sampling can accidentally exclude or under-represent minority classes.
# **Stratified sampling** guarantees that a fixed or proportional number of samples is drawn from *every* subgroup.

# In[5]:


# Draw exactly 5 students from each Status group (Pass and Fail)
stratified_sample = df.groupby("Status").sample(n=5, random_state=42)

print("\n--- 4. Stratified Sampling by Status (5 per group) ---")
print(stratified_sample[["StudentID", "Name", "Score", "Status"]])
print("\nCounts per status in stratified sample:")
print(stratified_sample["Status"].value_counts())


# ## Enrichment
# ### Creating Train and Test Splits with df.sample()
# In machine learning, datasets are divided into training (e.g. 80%) and testing (20%) partitions:
# ```python
# train_df = df.sample(frac=0.80, random_state=42)
# test_df = df.drop(train_df.index)
# print(f"Train size: {len(train_df)}, Test size: {len(test_df)}")
# ```

# ## Takeaways
# - Use `df.sample(n=...)` for exact row counts and `df.sample(frac=...)` for proportions.
# - Always set `random_state` to ensure reproducible results across team members and CI pipelines.
# - Use `replace=False` for standard subsets; use `replace=True` for statistical bootstrapping.
# - Use `df.groupby('category').sample(...)` for stratified sampling to avoid demographic or class representation bias.

# ## Conclusion
# Sampling allows you to rapidly iterate, validate pipelines, and prototype models without waiting on long runtimes for massive datasets.

# ## Exercises
#
# **Exercise 1:** Draw a random sample of 15 students from `df` using `random_state=2026`.
#
# **Exercise 2:** Create a 70/30 train/test split using `sample(frac=0.7)` and confirm the row counts add up to 100.
#
# **Exercise 3:** Draw a stratified sample of 8 students from each `Status` category.

# In[6]:


# --- Solutions ---

print("\n=== Exercise Solutions ===")

# Exercise 1 Solution:
ex1_sample = df.sample(n=15, random_state=2026)
print(f"Exercise 1: Sampled {len(ex1_sample)} students successfully.")

# Exercise 2 Solution:
train = df.sample(frac=0.7, random_state=42)
test = df.drop(train.index)
print(f"Exercise 2: Train size = {len(train)}, Test size = {len(test)}, Total = {len(train) + len(test)}")

# Exercise 3 Solution:
ex3_stratified = df.groupby("Status").sample(n=8, random_state=42)
print("Exercise 3 Stratified counts:")
print(ex3_stratified["Status"].value_counts())
