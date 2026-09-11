"""Custom Aggregation Functions in Pandas.

This module teaches first-year data science students how to write and apply
custom Python functions and lambdas inside DataFrameGroupBy.agg() for domain-specific
statistical calculations.
"""

import pandas as pd
import numpy as np


def create_course_marks_dataset() -> pd.DataFrame:
    """Creates a sample dataset of university student assessment marks across units."""
    data = {
        "unit": [
            "ITEC102", "ITEC102", "ITEC102", "ITEC102", "ITEC102",
            "ITEC105", "ITEC105", "ITEC105", "ITEC105", "ITEC105",
            "ITEC108", "ITEC108", "ITEC108", "ITEC108", "ITEC108",
        ],
        "student_id": [
            101, 102, 103, 104, 105,
            106, 107, 108, 109, 110,
            111, 112, 113, 114, 115,
        ],
        "mark": [
            88, 42, 95, 76, 68,
            55, 62, 48, 70, 81,
            91, 85, 88, 79, 94,
        ],
    }
    return pd.DataFrame(data)


# --- Custom Aggregator Functions ---

def data_range(series: pd.Series) -> float:
    """Computes the statistical range (max - min) of a group, ignoring NaNs."""
    cleaned = series.dropna()
    if cleaned.empty:
        return np.nan
    return cleaned.max() - cleaned.min()


def interquartile_range(series: pd.Series) -> float:
    """Computes the Interquartile Range (IQR = Q3 - Q1), robust to outliers."""
    cleaned = series.dropna()
    if len(cleaned) < 2:
        return np.nan
    return cleaned.quantile(0.75) - cleaned.quantile(0.25)


def pass_rate_pct(series: pd.Series) -> float:
    """Calculates the percentage of students scoring a passing mark (>= 50)."""
    cleaned = series.dropna()
    if cleaned.empty:
        return 0.0
    return (cleaned >= 50).mean() * 100.0


def trimmed_mean(series: pd.Series) -> float:
    """Computes a 20% trimmed mean (drops the lowest and highest values in small groups)."""
    cleaned = series.dropna().sort_values()
    if len(cleaned) <= 2:
        return cleaned.mean()
    # Exclude lowest and highest score
    return cleaned.iloc[1:-1].mean()


def demonstrate_custom_functions(df: pd.DataFrame):
    """Demonstrates applying user-defined functions using .agg()."""
    print("\n--- 1. Applying User-Defined Functions with .agg() ---")

    # Passing custom functions to .agg() with custom column labels using tuples: ('Column_Label', function)
    unit_stats = df.groupby("unit")["mark"].agg([
        ("Student_Count", "count"),
        ("Mean_Mark", "mean"),
        ("Spread_Range", data_range),
        ("IQR", interquartile_range),
        ("Trimmed_Mean", trimmed_mean),
        ("Pass_Rate_pct", pass_rate_pct),
    ])

    print("Comprehensive Custom Unit Statistics:")
    print(unit_stats.round(1))


def demonstrate_lambda_aggregators(df: pd.DataFrame):
    """Demonstrates using inline lambda expressions for quick calculations."""
    print("\n--- 2. Inline Lambda Aggregators ---")

    # Percentage of distinction scores (mark >= 75)
    lambda_stats = df.groupby("unit")["mark"].agg([
        ("Avg_Mark", "mean"),
        ("Distinction_pct", lambda s: (s >= 75).mean() * 100.0),
    ])

    print("Distinction Rates via Lambda:")
    print(lambda_stats.round(1))


def run_exercises():
    """Hands-on practice exercises for students."""
    print("\n--- 3. Student Practice Exercises ---")

    # Call centre customer resolution times (in seconds)
    call_centre = pd.DataFrame({
        "centre": ["Sydney", "Sydney", "Sydney", "Melbourne", "Melbourne", "Melbourne", "Brisbane", "Brisbane"],
        "shift": ["Morning", "Evening", "Morning", "Morning", "Evening", "Evening", "Morning", "Evening"],
        "handling_time_sec": [120, 240, 150, 180, 95, 310, 140, 200],
        "rating": [4.8, 3.2, 4.5, 4.0, 4.9, 2.8, 4.2, 3.9],
    })

    print("Call Centre Dataset:")
    print(call_centre)

    # Custom Function 1: Service Level Compliance (calls <= 180s)
    def service_level_pct(s: pd.Series) -> float:
        return (s <= 180).mean() * 100.0

    # Custom Function 2: Rating Spread (max - min)
    def rating_spread(s: pd.Series) -> float:
        return s.max() - s.min()

    # Exercise: Group by 'centre' and compute service_level_pct and rating_spread
    results = call_centre.groupby("centre").agg(
        total_calls=("handling_time_sec", "count"),
        sla_compliance_pct=("handling_time_sec", service_level_pct),
        rating_spread=("rating", rating_spread),
    )

    print("\nExercise Result - Call Centre Performance Metrics:")
    print(results.round(1))


def main():
    print("=========================================================")
    print("   Week 10 Topic 04: Custom Aggregation Functions")
    print("=========================================================")

    df = create_course_marks_dataset()
    demonstrate_custom_functions(df)
    demonstrate_lambda_aggregators(df)
    run_exercises()

    print("\n[Done] Successfully completed Custom Aggregation Functions demonstrations.")


if __name__ == "__main__":
    main()
