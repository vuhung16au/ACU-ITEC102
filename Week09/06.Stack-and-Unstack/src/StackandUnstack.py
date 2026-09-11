"""Stack and Unstack Operations in Pandas.

This module teaches first-year data science students how to pivot hierarchical
index levels between row indices and column headers using DataFrame.stack()
and DataFrame.unstack().
"""

import pandas as pd
import numpy as np


def create_hierarchical_grades_dataset() -> pd.DataFrame:
    """Creates a sample DataFrame with hierarchical MultiIndex columns and rows."""
    # MultiIndex row: Campus and StudentID
    row_tuples = [
        ("Sydney", "Liam Nguyen"),
        ("Sydney", "Emma Watson"),
        ("Melbourne", "Oliver Brown"),
        ("Melbourne", "Sophia Vu"),
    ]
    row_index = pd.MultiIndex.from_tuples(row_tuples, names=["Campus", "Student"])

    # MultiIndex columns: Unit and Assessment component
    col_tuples = [
        ("ITEC102", "Assignment"),
        ("ITEC102", "Final_Exam"),
        ("ITEC105", "Assignment"),
        ("ITEC105", "Final_Exam"),
    ]
    col_index = pd.MultiIndex.from_tuples(col_tuples, names=["Unit", "Component"])

    scores = [
        [88, 92, 75, 80],
        [85, 78, 82, 85],
        [90, 89, 94, 91],
        [72, 68, 70, 75],
    ]

    return pd.DataFrame(scores, index=row_index, columns=col_index)


def demonstrate_stack(df: pd.DataFrame) -> pd.DataFrame:
    """Demonstrates DataFrame.stack(): moves column headers into row index levels.

    Stacking pivots the innermost (or specified) column level to become the innermost row index.
    """
    print("\n--- 1. Original MultiIndex DataFrame ---")
    print(df)

    # Stack the innermost column level ('Component') into row index
    print("\n--- 2. Stacking Innermost Column Level (df.stack()) ---")
    df_stacked = df.stack(future_stack=True)
    print(df_stacked)

    # Stack a specific column level by name ('Unit')
    print("\n--- 3. Stacking Specific Level (level='Unit') ---")
    df_stacked_unit = df.stack(level="Unit", future_stack=True)
    print(df_stacked_unit)

    return df_stacked


def demonstrate_unstack(df_stacked: pd.DataFrame) -> pd.DataFrame:
    """Demonstrates DataFrame.unstack(): moves row index levels into column headers.

    Unstacking pivots the innermost (or specified) row index level to become column headers.
    """
    print("\n--- 4. Unstacking Row Level to Column Level (df_stacked.unstack()) ---")
    # Unstack the innermost row index level ('Component') back to columns
    df_unstacked = df_stacked.unstack()
    print(df_unstacked)

    print("\n--- 5. Unstacking Specific Level (level='Campus') ---")
    # Unstack 'Campus' level to see how it pivots to columns
    df_unstack_campus = df_stacked.unstack(level="Campus")
    print(df_unstack_campus)

    return df_unstacked


def demonstrate_missing_values_and_fill():
    """Demonstrates handling missing values (NaN) introduced by unstacking incomplete matrices."""
    print("\n--- 6. Unstacking with fill_value ---")

    # Incomplete records across campuses and terms
    index = pd.MultiIndex.from_tuples([
        ("Sydney", "Term 1"),
        ("Sydney", "Term 2"),
        ("Melbourne", "Term 1"),
        ("Brisbane", "Term 2"),  # Brisbane didn't run Term 1
    ], names=["Campus", "Term"])

    df = pd.DataFrame({"Enrolments": [350, 420, 280, 190]}, index=index)
    print("Incomplete Hierarchical DataFrame:")
    print(df)

    # Default unstack introduces NaN where combinations do not exist
    print("\nDefault unstack() introduces NaN:")
    print(df.unstack())

    # Unstack with fill_value=0 replaces missing combinations cleanly
    print("\nUnstack with fill_value=0:")
    print(df.unstack(fill_value=0))


def run_exercises():
    """Hands-on practice exercises for students."""
    print("\n--- 7. Student Exercises ---")

    # Sales data for tech retail stores in Sydney and Melbourne
    tuples = [
        ("Sydney", 2025),
        ("Sydney", 2026),
        ("Melbourne", 2025),
        ("Melbourne", 2026),
    ]
    idx = pd.MultiIndex.from_tuples(tuples, names=["City", "Year"])
    store_sales = pd.DataFrame(
        {
            "Laptops_kAUD": [120, 145, 95, 110],
            "Phones_kAUD": [85, 90, 70, 80],
        },
        index=idx,
    )

    print("Store Sales MultiIndex DataFrame:")
    print(store_sales)

    # Exercise 1: Stack store_sales so that the product columns become a row index level named 'Product'
    stacked_sales = store_sales.stack(future_stack=True)
    print("\nExercise 1 Result (Stacked Sales):")
    print(stacked_sales)

    # Exercise 2: Unstack 'City' from the stacked_sales DataFrame
    unstacked_by_city = stacked_sales.unstack(level="City")
    print("\nExercise 2 Result (Unstacked by City):")
    print(unstacked_by_city)


def main():
    print("=========================================================")
    print("   Week 09 Topic 06: Stack and Unstack Operations")
    print("=========================================================")

    df = create_hierarchical_grades_dataset()
    df_stacked = demonstrate_stack(df)
    demonstrate_unstack(df_stacked)
    demonstrate_missing_values_and_fill()
    run_exercises()

    print("\n[Done] Successfully demonstrated stack and unstack transformations.")


if __name__ == "__main__":
    main()
