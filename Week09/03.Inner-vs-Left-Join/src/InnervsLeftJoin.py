#!/usr/bin/env python
# coding: utf-8

# # Inner vs Left Join
#
# <a href="https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week09/03.Inner-vs-Left-Join/notebooks/01_03.Inner-vs-Left-Join.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
#
# ## Overview
# When merging relational tables, the **join type** (`how` parameter) dictates which records are preserved and which are discarded:
# - **Inner Join (`how='inner'`)**: Keeps only records where the key exists in **both** tables (intersection).
# - **Left Join (`how='left'`)**: Keeps **all** records from the left table, filling unmatched right-table fields with `NaN`.
# - **Right Join (`how='right'`)**: Keeps all records from the right table.
# - **Outer Join (`how='outer'`)**: Keeps all records from both tables (union).
#
# In business and data science analytics, **Left Joins are the standard default** because you rarely want primary entities (customers, patients, students) to disappear simply because they lack an optional secondary record.

# ## Setup: Creating Sample Relational Datasets
# We construct a primary Students table and an auxiliary Scholarships award table.

# In[1]:


import pandas as pd

students = pd.DataFrame({
    "StudentID": [101, 102, 103, 104, 105],
    "Name": ["Liam Nguyen", "Emma Watson", "Oliver Brown", "Sophia Vu", "Noah Taylor"],
    "Campus": ["Sydney", "Melbourne", "Brisbane", "Sydney", "Perth"],
})

scholarships = pd.DataFrame({
    "StudentID": [102, 104, 106, 107],
    "ScholarshipName": ["Vice-Chancellor Award", "STEM Excellence", "Alumni Grant", "Regional Bursary"],
    "Amount_AUD": [5000, 7500, 3000, 4000],
})

print("--- Students Table (Left) ---")
print(students)
print("\n--- Scholarships Table (Right) ---")
print(scholarships)


# ## Code Snippets: Comparing Join Behaviors
#
# ### 1. Inner Join (how='inner'): Intersection Only
# Only records with matching keys in **both** tables are included. Students without scholarships (101, 103, 105) and awards for non-current students (106, 107) are dropped.

# In[2]:


inner_merged = pd.merge(students, scholarships, on="StudentID", how="inner")
print("--- 1. Inner Join (Matching Students Only) ---")
print(inner_merged)
print(f"Row count: {len(inner_merged)}")


# ### 2. Left Join (how='left'): Preserving All Primary Entities
# Every single student from the left table is retained. Students without scholarships receive `NaN` for scholarship columns.

# In[3]:


left_merged = pd.merge(students, scholarships, on="StudentID", how="left")
print("\n--- 2. Left Join (All Students Retained) ---")
print(left_merged)
print(f"Row count: {len(left_merged)} (equals left table row count)")


# ### 3. Identifying Unmatched Records via Left Join
# Use the left join to easily find which students do **not** receive a scholarship by filtering for nulls in the right-side columns.

# In[4]:


unfunded_students = left_merged[left_merged["ScholarshipName"].isna()]
print("\n--- 3. Students Without Scholarships ---")
print(unfunded_students[["StudentID", "Name", "Campus"]])


# ### 4. Outer Join (how='outer'): Complete Union
# Retains all records from both datasets.

# In[5]:


outer_merged = pd.merge(students, scholarships, on="StudentID", how="outer")
print("\n--- 4. Full Outer Join ---")
print(outer_merged)


# ## Enrichment
# ### Preventing Row Multiplication with validate
# If a merge key unexpectedly contains duplicate entries, a left join will duplicate rows! Prevent this with `validate='one_to_one'` or `'one_to_many'`:
# ```python
# # Raises MergeError if StudentID is not unique in both tables:
# pd.merge(students, scholarships, on='StudentID', how='left', validate='one_to_one')
# ```

# ## Takeaways
# - **Inner Join**: Intersection of keys. Unmatched rows on either side are silently deleted.
# - **Left Join**: Preserves 100% of rows from the left table. Unmatched right columns become `NaN`.
# - In data reporting, default to **Left Join** so primary entities (students, customers) are never lost.
# - Combine Left Join with `.isna()` to quickly discover non-matching / unengaged entities.

# ## Conclusion
# Selecting the right join strategy is critical to avoid accidental data deletion and prevent false assumptions in downstream analytics.

# ## Exercises
#
# **Exercise 1:** Calculate how many students were dropped by the inner join compared to the total student count.
#
# **Exercise 2:** Calculate the total scholarship dollars awarded to currently active students using `inner_merged`.
#
# **Exercise 3:** Perform a Right Join (`how='right'`) on `students` and `scholarships`. Which scholarship award has no matching active student?

# In[6]:


# --- Solutions ---

print("\n=== Exercise Solutions ===")

# Exercise 1 Solution:
dropped_count = len(students) - len(inner_merged)
print(f"Exercise 1: {dropped_count} students were dropped by the inner join.")

# Exercise 2 Solution:
total_active_funding = inner_merged["Amount_AUD"].sum()
print(f"Exercise 2: Total active scholarship funding: ${total_active_funding:,} AUD")

# Exercise 3 Solution:
right_merged = pd.merge(students, scholarships, on="StudentID", how="right")
unmatched_awards = right_merged[right_merged["Name"].isna()]
print("\nExercise 3 Unmatched Awards in Right Join:")
print(unmatched_awards[["StudentID", "ScholarshipName", "Amount_AUD"]])
