"""Advanced Aggregation in Pandas: Multi-Metric Summaries and Named Aggregations.

This module teaches first-year data science students how to compute multiple
statistical summaries simultaneously using DataFrameGroupBy.agg(), dictionary
mappings, and Pandas named aggregations.
"""

import pandas as pd
import numpy as np


def create_faculty_research_dataset() -> pd.DataFrame:
    """Creates a sample dataset of university research performance across faculties."""
    data = {
        "faculty": [
            "Health Sciences", "Health Sciences", "Health Sciences",
            "Education & Arts", "Education & Arts", "Education & Arts",
            "Law & Business", "Law & Business", "Law & Business",
            "Theology & Philosophy", "Theology & Philosophy", "Theology & Philosophy",
        ],
        "campus": [
            "North Sydney", "Melbourne", "Brisbane",
            "North Sydney", "Melbourne", "Strathfield",
            "North Sydney", "Melbourne", "Brisbane",
            "North Sydney", "Melbourne", "Brisbane",
        ],
        "research_grant_kaud": [450, 520, 380, 210, 240, 190, 310, 340, 280, 150, 180, 130],
        "publications": [28, 34, 22, 15, 18, 12, 19, 21, 16, 11, 14, 9],
        "satisfaction_pct": [89.5, 91.0, 87.5, 92.0, 93.5, 90.0, 85.0, 86.5, 84.0, 94.0, 95.5, 93.0],
    }
    return pd.DataFrame(data)


def demonstrate_multi_metric_single_column(df: pd.DataFrame):
    """Demonstrates computing multiple summary statistics on a single column."""
    print("\n--- 1. Multiple Summary Metrics on a Single Column ---")

    # Applying a list of function names to one column
    grant_stats = df.groupby("faculty")["research_grant_kaud"].agg(
        ["count", "mean", "std", "min", "max"]
    )
    print("Research Grant Statistics by Faculty:")
    print(grant_stats.round(1))


def demonstrate_dictionary_aggregation(df: pd.DataFrame):
    """Demonstrates column-specific aggregations using dictionary mapping."""
    print("\n--- 2. Column-Specific Dictionary Mapping ---")

    agg_dict = {
        "research_grant_kaud": ["sum", "mean"],
        "publications": "sum",
        "satisfaction_pct": "mean",
    }

    campus_summary = df.groupby("campus").agg(agg_dict)
    print("Campus Performance Summary (Dictionary Mapping):")
    print(campus_summary.round(1))


def demonstrate_named_aggregation(df: pd.DataFrame) -> pd.DataFrame:
    """Demonstrates modern Pandas Named Aggregations for clean, flat column names.

    Named aggregation avoids clumsy MultiIndex column tuples like ('grant', 'mean').
    Syntax: new_col_name=('existing_col', 'agg_func')
    """
    print("\n--- 3. Modern Named Aggregation (Flat Columns) ---")

    clean_summary = df.groupby("campus").agg(
        project_count=("research_grant_kaud", "count"),
        total_grant_kaud=("research_grant_kaud", "sum"),
        avg_grant_kaud=("research_grant_kaud", "mean"),
        total_publications=("publications", "sum"),
        avg_satisfaction=("satisfaction_pct", "mean"),
    )

    print("Clean Named Aggregation Summary:")
    print(clean_summary.round(1))
    print("\nResulting Column Names:", clean_summary.columns.tolist())
    return clean_summary


def run_exercises():
    """Hands-on practice exercises for students."""
    print("\n--- 4. Student Practice Exercises ---")

    # Australian energy generation and costs by sector
    energy_data = pd.DataFrame({
        "state": ["NSW", "NSW", "VIC", "VIC", "QLD", "QLD", "WA", "WA"],
        "sector": ["Residential", "Commercial", "Residential", "Commercial", "Residential", "Commercial", "Residential", "Commercial"],
        "energy_gwh": [4200, 3100, 3800, 2900, 3500, 2700, 2100, 1800],
        "cost_maud": [630.0, 465.0, 570.0, 435.0, 490.0, 378.0, 294.0, 252.0],
    })

    print("Australian Energy Dataset:")
    print(energy_data)

    # Exercise 1: Group by 'sector' and compute ['min', 'mean', 'max'] of energy_gwh
    sector_stats = energy_data.groupby("sector")["energy_gwh"].agg(["min", "mean", "max"])
    print("\nExercise 1 Result - Energy Statistics by Sector:")
    print(sector_stats)

    # Exercise 2: Group by 'state' using Named Aggregation:
    #   total_energy = sum of energy_gwh
    #   avg_cost = mean of cost_maud
    state_named = energy_data.groupby("state").agg(
        total_energy=("energy_gwh", "sum"),
        avg_cost=("cost_maud", "mean"),
    )
    print("\nExercise 2 Result - State Named Aggregation:")
    print(state_named.round(1))


def main():
    print("=========================================================")
    print("   Week 10 Topic 03: Advanced Aggregation in Pandas")
    print("=========================================================")

    df = create_faculty_research_dataset()
    demonstrate_multi_metric_single_column(df)
    demonstrate_dictionary_aggregation(df)
    demonstrate_named_aggregation(df)
    run_exercises()

    print("\n[Done] Successfully completed Advanced Aggregation demonstrations.")


if __name__ == "__main__":
    main()
