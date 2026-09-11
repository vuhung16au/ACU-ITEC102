#!/usr/bin/env python
# coding: utf-8

# # Statistical Filling (Imputation)
#
# <a href="https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week08/03.Statistical-Filling/notebooks/03-statistical-filling.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
#
# ## Overview
# When dropping rows deletes too much data or biases results, **imputation** (filling missing values with statistically sound estimates) is the preferred solution.
#
# In this module, you will learn how to choose and apply central tendency measures:
# - **Mean**: Best for symmetric, normal numerical distributions.
# - **Median**: Best when distributions are skewed or contain heavy outliers.
# - **Mode**: Best for categorical or discrete attributes.
# - **Group-Specific Imputation**: Estimating missing values based on subgroup cohorts.

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
print(f"Loaded {len(df)} student records from {csv_file}")
print(f"Initial missing values:\n{df.isna().sum()}\n")


# ## Code Snippets: Imputation Strategies
#
# ### 1. Mean Imputation for Continuous Scores
# When numerical data is relatively symmetric, filling with the mean preserves the overall sample average.

# In[2]:


df_mean_fill = df.copy()
overall_mean_score = df_mean_fill["Score"].mean()
print(f"--- 1. Mean Imputation ---")
print(f"Computed Mean Score: {overall_mean_score:.2f}")

df_mean_fill["Score"] = df_mean_fill["Score"].fillna(overall_mean_score)
print(f"Missing scores remaining: {df_mean_fill['Score'].isna().sum()}")


# ### 2. Median Imputation for Skewed or Outlier-Prone Data
# Age and income data are often skewed. The median (50th percentile) is resilient against extreme outliers.

# In[3]:


df_median_fill = df.copy()
median_age = df_median_fill["Age"].median()
print(f"\n--- 2. Median Imputation ---")
print(f"Computed Median Age: {median_age}")

df_median_fill["Age"] = df_median_fill["Age"].fillna(median_age)
print(f"Missing ages remaining: {df_median_fill['Age'].isna().sum()}")


# ### 3. Mode Imputation for Categorical Columns
# For categorical columns (e.g. Pass/Fail, Campus, Gender), the mode (most frequent category) is used.

# In[4]:


print(f"\n--- 3. Mode Imputation ---")
most_common_status = df["Status"].mode()[0]
print(f"Most frequent Status (mode): {most_common_status}")


# ### 4. Group-Specific Imputation (Subgroup Means)
# Imputing a failing student's missing score with the overall class average is inaccurate!
# A far superior approach is filling missing scores using the mean of each student's specific `Status` cohort.

# In[5]:


df_grouped_fill = df.copy()

# Inspect group means before filling
print("\n--- 4. Group-Specific Imputation ---")
print("Average Score by Status:")
print(df_grouped_fill.groupby("Status")["Score"].mean())

# Impute by group
df_grouped_fill["Score"] = df_grouped_fill.groupby("Status")["Score"].transform(
    lambda grp: grp.fillna(grp.mean())
)
print("\nMissing scores remaining after group imputation:")
print(df_grouped_fill["Score"].isna().sum())


# ### 5. Comparing Pre- and Post-Imputation Summary Statistics
# Always confirm that imputation has not severely distorted standard deviations or quartile distributions.

# In[6]:


print("\n--- 5. Statistical Comparison (Score) ---")
comp = pd.DataFrame({
    "Original (with NaNs)": df["Score"].describe(),
    "Mean Imputed": df_mean_fill["Score"].describe(),
    "Group Imputed": df_grouped_fill["Score"].describe(),
})
print(comp.round(2))


# ## Enrichment
# ### Retaining Imputation Flags
# In machine learning pipelines, flagging which rows were imputed helps models detect potential imputation artifacts:
# ```python
# df['Score_Was_Missing'] = df['Score'].isna()
# df['Score'] = df['Score'].fillna(df['Score'].mean())
# ```

# ## Takeaways
# - Imputation retains your full sample size, avoiding the data loss of `.dropna()`.
# - Use **mean** for symmetric numerical features without extreme outliers.
# - Use **median** for skewed numerical variables (ages, prices, salaries).
# - Use **mode** for categorical features.
# - Group-specific imputation (`groupby().transform()`) yields more realistic, context-aware values than a blunt global average.

# ## Conclusion
# Statistical filling transforms an incomplete, unworkable dataset into a continuous, usable asset while maintaining aggregate statistical integrity.

# ## Exercises
#
# **Exercise 1:** Fill missing `Age` values in `df` with the median age, and display the first 5 rows.
#
# **Exercise 2:** Fill missing `Score` values using group-specific mean based on `Status`.
#
# **Exercise 3:** Verify with an assertion that zero missing values remain in both `Age` and `Score`.

# In[7]:


# --- Solutions ---

print("\n=== Exercise Solutions ===")

# Exercise 1 Solution:
clean_df = df.copy()
clean_df["Age"] = clean_df["Age"].fillna(clean_df["Age"].median())
print("Exercise 1 (First 5 rows after Age median fill):")
print(clean_df[["StudentID", "Name", "Age"]].head())

# Exercise 2 Solution:
clean_df["Score"] = clean_df.groupby("Status")["Score"].transform(
    lambda g: g.fillna(g.mean())
)
print("\nExercise 2 (Missing counts after group Score fill):")
print(clean_df[["Age", "Score"]].isna().sum())

# Exercise 3 Solution:
total_nulls = clean_df[["Age", "Score"]].isna().sum().sum()
assert total_nulls == 0, "Missing values still exist!"
print(f"\nExercise 3: Validation passed! Exactly {total_nulls} missing values remaining.")
