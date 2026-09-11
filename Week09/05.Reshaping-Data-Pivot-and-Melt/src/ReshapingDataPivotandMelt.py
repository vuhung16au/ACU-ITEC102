"""Reshaping Data: Pivot and Melt in Pandas.

This module teaches first-year data science students how to reshape datasets
between "wide" and "long" formats using pd.melt(), DataFrame.pivot(),
and DataFrame.pivot_table().
"""

import pandas as pd
import numpy as np


def create_wide_grades_dataset() -> pd.DataFrame:
    """Creates a sample wide-format DataFrame of student assessment scores."""
    data = {
        "student_id": [101, 102, 103, 104, 105],
        "name": ["Liam Nguyen", "Emma Watson", "Oliver Brown", "Sophia Vu", "Noah Taylor"],
        "campus": ["Sydney", "Melbourne", "Sydney", "Brisbane", "Melbourne"],
        "assignment_1": [85, 78, 92, 65, 88],
        "assignment_2": [90, 82, 88, 70, 94],
        "final_exam": [88, 75, 95, 72, 91],
    }
    return pd.DataFrame(data)


def demonstrate_melt(df_wide: pd.DataFrame) -> pd.DataFrame:
    """Demonstrates reshaping wide data into long (tidy) format using pd.melt().

    Wide datasets are convenient for human data entry, but long format
    (one observation per row) is preferred for grouping, plotting, and relational modelling.
    """
    print("\n--- 1. Original Wide Format ---")
    print(df_wide)

    # Melt: wide to long
    df_long = pd.melt(
        df_wide,
        id_vars=["student_id", "name", "campus"],
        value_vars=["assignment_1", "assignment_2", "final_exam"],
        var_name="assessment",
        value_name="score",
    )

    print("\n--- 2. Reshaped Long Format (pd.melt) ---")
    print(df_long.head(10))
    print(f"\nLong format shape: {df_long.shape} (rows x columns)")
    return df_long


def demonstrate_pivot(df_long: pd.DataFrame) -> pd.DataFrame:
    """Demonstrates pivoting long format back to wide format using DataFrame.pivot().

    df.pivot() requires that the combination of index and columns produces unique rows.
    """
    print("\n--- 3. Pivoting Long to Wide (df.pivot) ---")

    # Pivot back to wide
    df_pivoted = df_long.pivot(
        index=["student_id", "name", "campus"],
        columns="assessment",
        values="score",
    ).reset_index()

    # Flatten columns index name
    df_pivoted.columns.name = None

    print(df_pivoted)
    return df_pivoted


def demonstrate_pivot_table() -> pd.DataFrame:
    """Demonstrates DataFrame.pivot_table() for handling duplicate keys and aggregations."""
    print("\n--- 4. Aggregating with df.pivot_table() ---")

    # Longitudinal course enrollment records with duplicates
    enrollment_data = {
        "student_id": [101, 101, 102, 102, 103, 103, 104, 104, 105, 105],
        "campus": ["Sydney", "Sydney", "Melbourne", "Melbourne", "Sydney", "Sydney", "Brisbane", "Brisbane", "Melbourne", "Melbourne"],
        "unit": ["ITEC102", "ITEC105", "ITEC102", "ITEC108", "ITEC102", "ITEC105", "ITEC102", "ITEC108", "ITEC105", "ITEC108"],
        "semester": ["Sem 1", "Sem 2", "Sem 1", "Sem 2", "Sem 1", "Sem 2", "Sem 1", "Sem 2", "Sem 1", "Sem 2"],
        "mark": [85, 90, 78, 82, 92, 88, 65, 70, 88, 94],
    }
    df_enrollments = pd.DataFrame(enrollment_data)
    print("Enrolment Data:")
    print(df_enrollments)

    # Pivot table: Mean mark by Campus and Unit, with margins (subtotals)
    pt = pd.pivot_table(
        df_enrollments,
        values="mark",
        index="campus",
        columns="unit",
        aggfunc="mean",
        fill_value=0,
        margins=True,
        margins_name="Campus Average",
    )

    print("\nPivot Table: Average Mark by Campus & Unit (with Margins):")
    print(pt.round(1))
    return pt


def run_exercises():
    """Hands-on practice exercises for students."""
    print("\n--- 5. Student Exercises ---")

    # Monthly rainfall in Australian cities (Wide format)
    rainfall_wide = pd.DataFrame({
        "city": ["Sydney", "Melbourne", "Brisbane", "Perth"],
        "Jan": [101.3, 44.8, 145.2, 15.4],
        "Feb": [118.0, 48.3, 151.0, 8.8],
        "Mar": [129.7, 52.8, 112.5, 19.7],
    })

    print("Exercise Wide Rainfall Data:")
    print(rainfall_wide)

    # Exercise 1: Melt rainfall_wide into columns: 'city', 'month', 'rainfall_mm'
    rainfall_long = pd.melt(
        rainfall_wide,
        id_vars=["city"],
        value_vars=["Jan", "Feb", "Mar"],
        var_name="month",
        value_name="rainfall_mm",
    )
    print("\nExercise 1 Result (Rainfall Long Format):")
    print(rainfall_long.head(6))

    # Exercise 2: Pivot rainfall_long so 'month' is the index and 'city' forms the columns
    rainfall_by_month = rainfall_long.pivot(
        index="month",
        columns="city",
        values="rainfall_mm",
    )
    print("\nExercise 2 Result (Pivoted by Month):")
    print(rainfall_by_month)


def main():
    print("=========================================================")
    print("   Week 09 Topic 05: Reshaping Data (Pivot and Melt)")
    print("=========================================================")

    wide_df = create_wide_grades_dataset()
    long_df = demonstrate_melt(wide_df)
    demonstrate_pivot(long_df)
    demonstrate_pivot_table()
    run_exercises()

    print("\n[Done] Successfully demonstrated wide-to-long and long-to-wide reshaping.")


if __name__ == "__main__":
    main()
