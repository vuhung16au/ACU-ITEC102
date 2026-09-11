#!/usr/bin/env python
# coding: utf-8

# # Merging with Different Column Names
#
# <a href="https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week09/04.Merging-with-Different-Column-Names/notebooks/01_04.Merging-with-Different-Column-Names.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
#
# ## Overview
# In enterprise IT environments, different departments and software systems rarely use identical column names for the same entity.
# - The Student Administration system may identify students by `student_id`.
# - The Finance Billing system may call the exact same identifier `id_number` or `account_no`.
#
# In this module, you will learn how to:
# - Join tables with mismatched key names using `left_on` and `right_on`.
# - Clean up redundant duplicate key columns after merging.
# - Join a table's column against another table's index (`right_index=True`).
# - Disambiguate overlapping non-key column names using custom `suffixes`.

# ## Setup: Creating Sample Disparate Datasets
# We construct student portal records and finance billing data.

# In[1]:


import pandas as pd

# Academic Portal Data
portal_df = pd.DataFrame({
    "student_id": [101, 102, 103, 104],
    "full_name": ["Liam Nguyen", "Emma Watson", "Oliver Brown", "Sophia Vu"],
    "major": ["Computer Science", "Information Technology", "Data Science", "Software Engineering"],
    "status": ["Active", "Active", "Probation", "Active"],
})

# Finance & Billing Data
finance_df = pd.DataFrame({
    "id_number": [101, 102, 103, 105],
    "tuition_due_aud": [4500.0, 0.0, 3200.0, 1800.0],
    "payment_plan": ["Upfront", "HECS-HELP", "Installments", "Upfront"],
    "status": ["Current", "Current", "Overdue", "Current"],
})

print("--- Academic Portal (Key: 'student_id') ---")
print(portal_df)
print("\n--- Finance Portal (Key: 'id_number') ---")
print(finance_df)


# ## Code Snippets: Merging Across Key Discrepancies
#
# ### 1. Joining on Mismatched Column Names (left_on & right_on)
# Specify the respective key names for the left and right tables.

# In[2]:


merged_raw = pd.merge(
    portal_df,
    finance_df,
    left_on="student_id",
    right_on="id_number",
    how="left",
)
print("--- 1. Merged with left_on and right_on ---")
print(merged_raw)


# ### 2. Dropping Redundant Key Columns
# Notice above that both `student_id` and `id_number` exist in the result. Keep your schema clean by removing the duplicate key.

# In[3]:


merged_clean = merged_raw.drop(columns=["id_number"])
print("\n--- 2. Cleaned Schema (Redundant 'id_number' Dropped) ---")
print(merged_clean)


# ### 3. Disambiguating Overlapping Columns with suffixes
# Both tables contain a column named `status` (Academic Status vs Billing Status).
# By default, Pandas appends `_x` and `_y`. Use the `suffixes` argument to assign clear, self-documenting names.

# In[4]:


merged_suffixed = pd.merge(
    portal_df,
    finance_df,
    left_on="student_id",
    right_on="id_number",
    how="left",
    suffixes=("_academic", "_billing"),
).drop(columns=["id_number"])

print("\n--- 3. Clean Suffixes Assigned ---")
print(merged_suffixed[["student_id", "full_name", "status_academic", "status_billing", "tuition_due_aud"]])


# ### 4. Merging on DataFrame Index (right_index=True)
# If one dataset has its key in the index rather than a standard column:

# In[5]:


# Set finance table index to id_number
finance_indexed = finance_df.set_index("id_number")

# Merge column student_id with right_index
index_merged = pd.merge(
    portal_df,
    finance_indexed,
    left_on="student_id",
    right_index=True,
    how="left",
    suffixes=("_portal", "_finance"),
)
print("\n--- 4. Merged with right_index=True ---")
print(index_merged[["student_id", "full_name", "tuition_due_aud", "payment_plan"]])


# ## Enrichment
# ### Merging on Multiple Keys with Different Names
# You can pass lists of keys to `left_on` and `right_on`:
# ```python
# # pd.merge(df1, df2, left_on=['campus_id', 'term'], right_on=['campus_code', 'semester'])
# ```

# ## Takeaways
# - Use `left_on='key1'` and `right_on='key2'` when joining columns with differing header names.
# - Always drop the redundant secondary key column after merging to avoid confusing users.
# - Use `suffixes=('_label1', '_label2')` to cleanly distinguish overlapping column names.
# - Use `left_index=True` or `right_index=True` when joining against a DataFrame's index.

# ## Conclusion
# Real-world data integration requires mapping between varying column schemas. Using `left_on`, `right_on`, and explicit `suffixes` ensures consistent, readable analytical views.

# ## Exercises
#
# **Exercise 1:** Merge `portal_df` and `finance_df` using `how='inner'`, `left_on='student_id'`, and `right_on='id_number'`.
#
# **Exercise 2:** Apply custom suffixes `('_portal', '_finance')` to the inner merge and drop `'id_number'`.
#
# **Exercise 3:** Filter the merged DataFrame for students who have an overdue billing status (`status_finance == 'Overdue'`).

# In[6]:


# --- Solutions ---

print("\n=== Exercise Solutions ===")

# Exercise 1 & 2 Solution:
inner_clean = pd.merge(
    portal_df,
    finance_df,
    left_on="student_id",
    right_on="id_number",
    how="inner",
    suffixes=("_portal", "_finance"),
).drop(columns=["id_number"])

print("Exercise 1 & 2 Result:")
print(inner_clean[["student_id", "full_name", "status_portal", "status_finance", "tuition_due_aud"]])

# Exercise 3 Solution:
overdue_students = inner_clean[inner_clean["status_finance"] == "Overdue"]
print("\nExercise 3 (Overdue Students):")
print(overdue_students[["student_id", "full_name", "tuition_due_aud"]])
