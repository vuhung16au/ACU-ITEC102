"""Multi-Level Grouping in Pandas: Hierarchical Cohort Aggregation.

This module teaches first-year data science students how to group by multiple
categorical dimensions simultaneously, slice the resulting MultiIndex structures,
and pivot dimensions with unstack().
"""

import pandas as pd
import numpy as np


def create_faculty_enrolment_dataset() -> pd.DataFrame:
    """Creates a sample dataset of Australian university faculties across campuses."""
    data = {
        "campus": [
            "North Sydney", "North Sydney", "North Sydney",
            "Melbourne", "Melbourne", "Melbourne",
            "Brisbane", "Brisbane", "Brisbane",
        ],
        "faculty": [
            "Health Sciences", "Education & Arts", "Law & Business",
            "Health Sciences", "Education & Arts", "Theology & Philosophy",
            "Health Sciences", "Law & Business", "Theology & Philosophy",
        ],
        "year": [2026, 2026, 2026, 2026, 2026, 2026, 2026, 2026, 2026],
        "enrolments": [1250, 820, 950, 1400, 910, 430, 890, 670, 310],
        "funding_kaud": [320.0, 180.5, 210.0, 380.0, 205.0, 115.0, 240.0, 160.0, 95.0],
        "satisfaction_pct": [88.5, 91.0, 84.0, 89.2, 92.5, 94.0, 87.0, 83.5, 93.0],
    }
    return pd.DataFrame(data)


def demonstrate_multi_level_groupby(df: pd.DataFrame) -> pd.DataFrame:
    """Demonstrates grouping by multiple keys and inspecting hierarchical results."""
    print("\n--- 1. Grouping by Multiple Keys (['campus', 'faculty']) ---")
    grouped = df.groupby(["campus", "faculty"])

    print(f"Number of composite groups: {grouped.ngroups}")

    # Aggregating multiple numeric columns
    hierarchical_summary = grouped[["enrolments", "funding_kaud"]].sum()
    print("\nHierarchical GroupBy Result (MultiIndex Rows):")
    print(hierarchical_summary)
    print(f"\nIndex Type: {type(hierarchical_summary.index)}")
    print(f"Index Level Names: {hierarchical_summary.index.names}")

    return hierarchical_summary


def demonstrate_slicing_and_unstacking(df_grouped: pd.DataFrame, df_raw: pd.DataFrame):
    """Demonstrates slicing MultiIndex rows and unstacking levels into columns."""
    print("\n--- 2. Slicing Multi-Level Grouped Data ---")

    # Slicing an entire top-level group ('North Sydney')
    print("Slicing top-level group ('North Sydney'):")
    print(df_grouped.loc["North Sydney"])

    # Slicing a specific composite key tuple
    print("\nSlicing specific tuple ('Melbourne', 'Health Sciences'):")
    print(df_grouped.loc[("Melbourne", "Health Sciences")])

    # Unstacking: rotating the inner level ('faculty') to column headers
    print("\n--- 3. Unstacking Faculty to Columns ---")
    enrolment_matrix = df_raw.groupby(["campus", "faculty"])["enrolments"].sum().unstack(fill_value=0)
    print(enrolment_matrix)


def demonstrate_within_group_proportions(df: pd.DataFrame):
    """Demonstrates computing within-group percentage shares using transform()."""
    print("\n--- 4. Computing Within-Campus Proportions ---")

    # Sum total enrolments per campus, broadcasting to matching rows
    campus_totals = df.groupby("campus")["enrolments"].transform("sum")
    df_with_share = df.copy()
    df_with_share["campus_total"] = campus_totals
    df_with_share["enrolment_share_pct"] = (
        df_with_share["enrolments"] / df_with_share["campus_total"] * 100
    ).round(1)

    display_cols = ["campus", "faculty", "enrolments", "campus_total", "enrolment_share_pct"]
    print(df_with_share[display_cols].sort_values(by=["campus", "enrolments"], ascending=[True, False]))


def run_exercises():
    """Hands-on practice exercises for students."""
    print("\n--- 5. Student Practice Exercises ---")

    # Retail store sales across Australian states and store formats
    retail_sales = pd.DataFrame({
        "state": ["NSW", "NSW", "NSW", "VIC", "VIC", "VIC", "QLD", "QLD"],
        "store_format": ["Flagship", "Express", "Suburban", "Flagship", "Express", "Suburban", "Flagship", "Express"],
        "revenue_kaud": [450, 180, 220, 410, 195, 205, 320, 140],
        "transactions": [12000, 8500, 6200, 11500, 9200, 5800, 8900, 6100],
    })

    print("Retail Sales Dataset:")
    print(retail_sales)

    # Exercise 1: Group by ['state', 'store_format'] and sum revenue_kaud
    state_format_rev = retail_sales.groupby(["state", "store_format"])["revenue_kaud"].sum()
    print("\nExercise 1 Result - Revenue by State and Store Format:")
    print(state_format_rev)

    # Exercise 2: Unstack 'store_format' to show formats as columns
    format_comparison = state_format_rev.unstack(fill_value=0)
    print("\nExercise 2 Result - Formats Unstacked to Columns:")
    print(format_comparison)


def main():
    print("=========================================================")
    print("   Week 10 Topic 02: Multi-Level Grouping in Pandas")
    print("=========================================================")

    df = create_faculty_enrolment_dataset()
    hierarchical_summary = demonstrate_multi_level_groupby(df)
    demonstrate_slicing_and_unstacking(hierarchical_summary, df)
    demonstrate_within_group_proportions(df)
    run_exercises()

    print("\n[Done] Successfully completed Multi-Level Grouping demonstrations.")


if __name__ == "__main__":
    main()
