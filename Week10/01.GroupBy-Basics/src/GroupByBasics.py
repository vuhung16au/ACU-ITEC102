"""GroupBy Basics in Pandas: The Split-Apply-Combine Paradigm.

This module introduces first-year data science students to grouping operations
in Pandas, explaining how to split data into cohorts, apply aggregation functions,
and combine results into summary reports.
"""

import pandas as pd
import numpy as np


def create_student_cohort_dataset() -> pd.DataFrame:
    """Creates a sample DataFrame of Australian Catholic University (ACU) students."""
    data = {
        "student_id": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
        "name": [
            "Liam Nguyen",
            "Emma Watson",
            "Oliver Brown",
            "Sophia Vu",
            "Noah Taylor",
            "Ava Wilson",
            "Lucas Martin",
            "Mia Anderson",
        ],
        "campus": [
            "North Sydney",
            "Melbourne",
            "North Sydney",
            "Brisbane",
            "Melbourne",
            "Strathfield",
            "Brisbane",
            "Strathfield",
        ],
        "study_mode": [
            "Full-time",
            "Part-time",
            "Full-time",
            "Full-time",
            "Part-time",
            "Full-time",
            "Part-time",
            "Full-time",
        ],
        "course": [
            "Bachelor of IT",
            "Bachelor of Nursing",
            "Bachelor of IT",
            "Bachelor of Business",
            "Bachelor of IT",
            "Bachelor of Education",
            "Bachelor of Business",
            "Bachelor of Education",
        ],
        "wam": [82.5, 76.0, 89.0, 71.5, 84.0, 78.5, 68.0, 91.0],
        "attendance": [92, 85, 95, 78, 88, 82, 70, 96],
        "units_completed": [8, 4, 12, 6, 8, 10, 4, 12],
    }
    return pd.DataFrame(data)


def demonstrate_split_concept(df: pd.DataFrame):
    """Demonstrates splitting a DataFrame into groups and inspecting group metadata."""
    print("\n--- 1. The Split Step (df.groupby) ---")
    grouped = df.groupby("campus")

    print(f"GroupBy object type: {type(grouped)}")
    print(f"Total number of groups: {grouped.ngroups}")
    print(f"Group names (keys): {list(grouped.groups.keys())}")

    # Inspecting cohort size (number of observations per campus)
    print("\nGroup Sizes (.size()):")
    print(grouped.size())

    # Extracting a specific cohort
    print("\nExtracting a single group ('Melbourne'):")
    melbourne_students = grouped.get_group("Melbourne")
    print(melbourne_students[["student_id", "name", "course", "wam"]])


def demonstrate_apply_combine(df: pd.DataFrame):
    """Demonstrates applying aggregation functions and combining results."""
    print("\n--- 2. The Apply and Combine Steps ---")

    # Aggregating a single column: returns a Series
    avg_wam_by_campus = df.groupby("campus")["wam"].mean()
    print("\nAverage WAM by Campus (returns Series):")
    print(avg_wam_by_campus.round(2))

    # Aggregating multiple numeric columns: returns a DataFrame
    cohort_stats = df.groupby("campus")[["wam", "attendance"]].mean()
    print("\nAverage WAM & Attendance by Campus (returns DataFrame):")
    print(cohort_stats.round(2))

    # Common built-in aggregators
    print("\nSummary Statistics on Units Completed:")
    print("Min:", df.groupby("campus")["units_completed"].min().to_dict())
    print("Max:", df.groupby("campus")["units_completed"].max().to_dict())
    print("Sum:", df.groupby("campus")["units_completed"].sum().to_dict())


def demonstrate_as_index(df: pd.DataFrame):
    """Demonstrates index behavior: as_index=True vs as_index=False."""
    print("\n--- 3. Controlling Result Index (as_index) ---")

    # Default: as_index=True (grouping key becomes DataFrame Index)
    result_with_index = df.groupby("campus", as_index=True)["wam"].mean()
    print("Default (as_index=True) Index:")
    print(result_with_index)
    print("Index values:", result_with_index.index)

    # as_index=False (grouping key is retained as a regular column)
    result_as_column = df.groupby("campus", as_index=False)["wam"].mean()
    print("\nWith as_index=False (tabular column output):")
    print(result_as_column)
    print("Columns:", result_as_column.columns.tolist())


def run_exercises():
    """Hands-on exercises for students with worked solutions."""
    print("\n--- 4. Student Practice Exercises ---")

    # Patient admissions across Australian metropolitan hospitals
    hospital_data = pd.DataFrame({
        "patient_id": [201, 202, 203, 204, 205, 206],
        "hospital": ["Sydney", "Melbourne", "Sydney", "Brisbane", "Melbourne", "Brisbane"],
        "department": ["Emergency", "Cardiology", "Cardiology", "Emergency", "Pediatrics", "Emergency"],
        "wait_time_mins": [45, 15, 20, 50, 10, 60],
        "length_of_stay_days": [2, 5, 4, 1, 3, 2],
    })

    print("Hospital Admissions Dataset:")
    print(hospital_data)

    # Exercise 1: Group by department and find average wait_time_mins
    dept_wait = hospital_data.groupby("department")["wait_time_mins"].mean()
    print("\nExercise 1 Result - Average Wait Time by Department:")
    print(dept_wait.round(1))

    # Exercise 2: Group by hospital with as_index=False and find maximum length_of_stay_days
    hosp_max_stay = hospital_data.groupby("hospital", as_index=False)["length_of_stay_days"].max()
    print("\nExercise 2 Result - Max Length of Stay by Hospital (as_index=False):")
    print(hosp_max_stay)


def main():
    print("=========================================================")
    print("   Week 10 Topic 01: GroupBy Basics (Split-Apply-Combine)")
    print("=========================================================")

    df = create_student_cohort_dataset()
    demonstrate_split_concept(df)
    demonstrate_apply_combine(df)
    demonstrate_as_index(df)
    run_exercises()

    print("\n[Done] Successfully completed GroupBy Basics demonstrations.")


if __name__ == "__main__":
    main()
