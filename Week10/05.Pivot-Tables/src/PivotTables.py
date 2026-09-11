"""Pivot Tables in Pandas: Multidimensional Matrix Aggregation.

This module teaches first-year data science students how to create two-dimensional
summary reports using pd.pivot_table(), contrasting pivot tables with groupby,
and handling sparse combinations with fill_value.
"""

import pandas as pd
import numpy as np


def create_tech_employment_dataset() -> pd.DataFrame:
    """Creates a sample dataset of Australian tech graduate employment and salaries."""
    data = {
        "state": [
            "NSW", "NSW", "NSW", "NSW",
            "VIC", "VIC", "VIC", "VIC",
            "QLD", "QLD", "QLD", "QLD",
        ],
        "degree": [
            "Bachelor", "Master", "Bachelor", "Master",
            "Bachelor", "Master", "Bachelor", "Master",
            "Bachelor", "Master", "Bachelor", "Master",
        ],
        "specialisation": [
            "Software Eng", "Software Eng", "Cyber Security", "Data Science",
            "Software Eng", "Cyber Security", "Data Science", "Data Science",
            "Software Eng", "Cyber Security", "Data Science", "Cloud Computing",
        ],
        "salary_kaud": [85, 105, 90, 110, 82, 98, 92, 108, 78, 88, 85, 102],
        "placement_pct": [92, 96, 94, 95, 90, 93, 91, 97, 88, 91, 89, 94],
    }
    return pd.DataFrame(data)


def demonstrate_basic_pivot_table(df: pd.DataFrame):
    """Demonstrates creating a 2D cross-tabulated summary using pd.pivot_table()."""
    print("\n--- 1. Basic 2D Pivot Table (Average Salary) ---")

    # Pivot table: Rows = State, Columns = Specialisation, Values = Salary (mean)
    salary_table = pd.pivot_table(
        df,
        values="salary_kaud",
        index="state",
        columns="specialisation",
        aggfunc="mean",
        fill_value=0,
    )

    print("Average Starting Salary (kAUD) by State and Specialisation:")
    print(salary_table.round(1))


def demonstrate_groupby_vs_pivot(df: pd.DataFrame):
    """Contrasts the output structure of groupby() vs pivot_table()."""
    print("\n--- 2. Contrasting GroupBy vs. Pivot Table ---")

    # GroupBy approach: outputs tall, hierarchical Series
    grouped_result = df.groupby(["state", "specialisation"])["salary_kaud"].mean()
    print("GroupBy Output (Tall Hierarchy):")
    print(grouped_result.head(6))

    # Pivot Table approach: outputs wide 2D matrix
    pivoted_result = pd.pivot_table(
        df, values="salary_kaud", index="state", columns="specialisation", aggfunc="mean"
    )
    print("\nPivot Table Output (2D Matrix):")
    print(pivoted_result.round(1))


def demonstrate_multi_metric_pivot(df: pd.DataFrame):
    """Demonstrates multi-level rows, multi-level columns, and multiple aggregation functions."""
    print("\n--- 3. Multi-Metric and Hierarchical Pivot Tables ---")

    # Multi-level index: State and Degree
    multi_pivot = pd.pivot_table(
        df,
        values="salary_kaud",
        index=["state", "degree"],
        columns="specialisation",
        aggfunc="mean",
        fill_value=0,
    )
    print("Hierarchical Rows (State & Degree):")
    print(multi_pivot.round(1))

    # Multiple aggregation functions: Mean and Count
    agg_pivot = pd.pivot_table(
        df,
        values="salary_kaud",
        index="state",
        columns="specialisation",
        aggfunc=["mean", "count"],
        fill_value=0,
    )
    print("\nMultiple Functions (Mean & Count):")
    print(agg_pivot)


def run_exercises():
    """Hands-on practice exercises for students."""
    print("\n--- 4. Student Practice Exercises ---")

    # Australian electric vehicle (EV) charging stations
    ev_data = pd.DataFrame({
        "state": ["NSW", "NSW", "VIC", "VIC", "QLD", "QLD", "NSW", "VIC"],
        "provider": ["Chargefox", "Tesla", "Chargefox", "Evie", "Chargefox", "Evie", "Evie", "Tesla"],
        "stations": [45, 60, 38, 25, 30, 20, 35, 55],
        "power_kw": [150, 250, 150, 350, 150, 350, 350, 250],
    })

    print("EV Charging Infrastructure Dataset:")
    print(ev_data)

    # Exercise 1: Create a pivot table showing average power_kw by state and provider
    power_pivot = pd.pivot_table(
        ev_data,
        values="power_kw",
        index="state",
        columns="provider",
        aggfunc="mean",
        fill_value=0,
    )
    print("\nExercise 1 Result - Average Power (kW) by State & Provider:")
    print(power_pivot.round(1))

    # Exercise 2: Create a pivot table showing total stations by state and provider
    station_pivot = pd.pivot_table(
        ev_data,
        values="stations",
        index="state",
        columns="provider",
        aggfunc="sum",
        fill_value=0,
    )
    print("\nExercise 2 Result - Total Stations by State & Provider:")
    print(station_pivot)


def main():
    print("=========================================================")
    print("   Week 10 Topic 05: Pivot Tables in Pandas")
    print("=========================================================")

    df = create_tech_employment_dataset()
    demonstrate_basic_pivot_table(df)
    demonstrate_groupby_vs_pivot(df)
    demonstrate_multi_metric_pivot(df)
    run_exercises()

    print("\n[Done] Successfully completed Pivot Tables demonstrations.")


if __name__ == "__main__":
    main()
