#!/usr/bin/env python
# coding: utf-8

# # Combining and Merging Datasets
#
# <a href="https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week09/02.Combining-and-Merging-Datasets/notebooks/01_02.Combining-and-Merging-Datasets.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
#
# ## Overview
# In practical data engineering, information is typically split across multiple files, database tables, or time periods.
# Pandas offers two core mechanisms to unify datasets:
# - **`pd.concat()`**: Stacking data along an axis (e.g. appending new rows from Semester 2, or appending side-by-side columns).
# - **`pd.merge()`**: Performing relational joins based on shared key columns (e.g. matching Student ID across student records and exam marks).
#
# In this module, you will learn how and when to combine datasets with `concat()` and merge relational tables with `merge()`.

# ## Setup: Creating Sample University Datasets
# We construct student cohort records and an academic enrolments table.

# In[1]:


import pandas as pd

# Semester 1 intake
sem1_students = pd.DataFrame({
    "StudentID": [101, 102, 103],
    "Name": ["Liam Nguyen", "Emma Watson", "Oliver Brown"],
    "Degree": ["B.CS", "B.IT", "B.DataSci"],
})

# Semester 2 intake
sem2_students = pd.DataFrame({
    "StudentID": [104, 105],
    "Name": ["Sophia Vu", "Noah Taylor"],
    "Degree": ["B.CS", "B.IT"],
})

# Enrolment and marks table
enrolments = pd.DataFrame({
    "StudentID": [101, 102, 103, 104, 106],
    "CourseCode": ["ITEC102", "ITEC102", "ITEC102", "ITEC102", "ITEC102"],
    "Mark": [88, 74, 91, 82, 65],
})

print("--- Semester 1 Students ---")
print(sem1_students)
print("\n--- Semester 2 Students ---")
print(sem2_students)
print("\n--- Enrolment Records ---")
print(enrolments)


# ## Code Snippets: Concatenation and Merging
#
# ### 1. Appending Rows with pd.concat(axis=0)
# Stacking two DataFrames vertically. Always pass `ignore_index=True` to create a continuous 0, 1, 2... index.

# In[2]:


all_students = pd.concat([sem1_students, sem2_students], ignore_index=True)
print("\n--- 1. Vertical Concatenation (Combined Cohorts) ---")
print(all_students)


# ### 2. Relational Merging with pd.merge()
# Combine student personal details with their academic marks using the common key `StudentID`.

# In[3]:


# Inner merge on StudentID
student_grades = pd.merge(all_students, enrolments, on="StudentID")
print("\n--- 2. Relational Merge on 'StudentID' ---")
print(student_grades)


# ### 3. Tracking Record Lineage with indicator=True
# Adding `indicator=True` appends a special `_merge` column showing whether each record existed in `left_only`, `right_only`, or `both` tables.

# In[4]:


tracked_merge = pd.merge(all_students, enrolments, on="StudentID", how="outer", indicator=True)
print("\n--- 3. Merge with Lineage Indicator ---")
print(tracked_merge[["StudentID", "Name", "Mark", "_merge"]])


# ### 4. Side-by-Side Concatenation (axis=1)
# Combine tables horizontally along columns by matching on index.

# In[5]:


scores_df = pd.DataFrame({"Midterm": [85, 78, 92]}, index=[101, 102, 103])
practicals_df = pd.DataFrame({"Lab_Exam": [90, 82, 88]}, index=[101, 102, 103])

side_by_side = pd.concat([scores_df, practicals_df], axis=1)
print("\n--- 4. Horizontal Concatenation (axis=1) ---")
print(side_by_side)


# ## Enrichment
# ### Tagging Cohorts with Keys in Concat
# Preserve the origin of each row by creating a hierarchical index on concatenation:
# ```python
# tagged_df = pd.concat([sem1_students, sem2_students], keys=['Semester_1', 'Semester_2'])
# print(tagged_df)
# ```

# ## Takeaways
# - Use `pd.concat([df1, df2], ignore_index=True)` to append rows when schemas are identical.
# - Use `pd.merge(df1, df2, on='Key')` to join relational tables on common attributes.
# - Use `indicator=True` in `pd.merge()` to audit which rows matched across datasets.
# - Use `pd.concat(..., axis=1)` to glue columns together by index alignment.

# ## Conclusion
# Mastering concatenation and merging enables you to stitch together disparate operational tables into unified analytical views.

# ## Exercises
#
# **Exercise 1:** Concatenate `sem1_students` and `sem2_students` using `keys=['S1', 'S2']` to create a hierarchical index.
#
# **Exercise 2:** Merge `all_students` and `enrolments` on `StudentID`, keeping only students who are enrolled in `ITEC102`.
#
# **Exercise 3:** Use the `_merge` column from snippet 3 to identify which student ID was enrolled in `enrolments` but was missing from `all_students`.

# In[6]:


# --- Solutions ---

print("\n=== Exercise Solutions ===")

# Exercise 1 Solution:
tagged = pd.concat([sem1_students, sem2_students], keys=["S1", "S2"])
print("Exercise 1 (Tagged Concat):")
print(tagged)

# Exercise 2 Solution:
itec_students = pd.merge(all_students, enrolments[enrolments["CourseCode"] == "ITEC102"], on="StudentID")
print(f"\nExercise 2 (Enrolled ITEC102 Students: {len(itec_students)}):")
print(itec_students[["StudentID", "Name", "Mark"]])

# Exercise 3 Solution:
right_only_student = tracked_merge[tracked_merge["_merge"] == "right_only"]["StudentID"].iloc[0]
print(f"\nExercise 3: Student present only in enrolments table: ID {right_only_student}")
