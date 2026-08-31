#!/usr/bin/env python
# coding: utf-8

# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week03/06.Mini-Project-Student-Enrolment/notebooks/06.Mini-Project-Student-Enrolment.ipynb)
# [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/vuhung16au/ACU-ITEC102/blob/main/Week03/06.Mini-Project-Student-Enrolment/notebooks/06.Mini-Project-Student-Enrolment.ipynb)
# [![Open In SageMaker Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/vuhung16au/ACU-ITEC102/blob/main/Week03/06.Mini-Project-Student-Enrolment/notebooks/06.Mini-Project-Student-Enrolment.ipynb)
#

# # Mini-Project: Building a Student Enrolment System
#
# [Open this notebook in Google Colab](https://colab.research.google.com/github/vuhung16au/ACU-ITEC102/blob/main/Week03/06.Mini-Project-Student-Enrolment/notebooks/06.Mini-Project-Student-Enrolment.ipynb)
#
# ## Overview
# At the end of the session, we will combine Lists, Tuples, Sets, and Dictionaries into a single, cohesive script that manages student enrolments, ensures no duplicate workshop bookings, and calculates the popularity of different classes.

# ## Code Snippets

# In[1]:


# Student Enrolment System

# We'll use a dictionary to act as our database.
# Keys are student IDs (immutable), Values are dictionaries of student details.
enrolment_db = {
    1001: {"name": "Alice", "courses": set(["Python", "Data Science"])},
    1002: {"name": "Bob", "courses": set(["Python"])},
}


def enrol_student(student_id, name, course):
    if student_id not in enrolment_db:
        # Create a new record using a dictionary
        enrolment_db[student_id] = {"name": name, "courses": set()}

    # Add course to the set (automatically ignores duplicates)
    enrolment_db[student_id]["courses"].add(course)
    print(f"{name} successfully enrolled in {course}.")


# Enrol some students
enrol_student(1003, "Charlie", "AI")
enrol_student(1001, "Alice", "Python")  # Duplicate, won't add a second time

print("\n--- Final Database ---")
for sid, data in enrolment_db.items():
    print(f"ID: {sid}, Name: {data['name']}, Courses: {list(data['courses'])}")


# ## Enrichment
# By using a `set` for the courses, we didn't have to write any `if course in courses:` logic to prevent duplicate enrolments. The Set handled it instantly. Using a dictionary for the main database allowed us to quickly look up a student by ID in O(1) time.

# ## Takeaways
# - Combining collections is how real-world applications are built.
# - Dictionaries are great for databases, Sets for unique attributes, and Lists for ordered outputs.

# ## Conclusion
# Congratulations on building a functioning enrolment system using Core Python Data Structures!

# ## Exercises

# In[2]:


# Exercise: Add a function `drop_course(student_id, course)` that removes a course from a student's set.
# Safely handle the case where the student ID doesn't exist, or the course isn't in their set.

# --- Solution ---
# def drop_course(student_id, course):
#     student = enrolment_db.get(student_id)
#     if student:
#         if course in student["courses"]:
#             student["courses"].remove(course)
#             print(f"Dropped {course}")
#         else:
#             print("Not enrolled in course.")
#     else:
#         print("Student ID not found.")
