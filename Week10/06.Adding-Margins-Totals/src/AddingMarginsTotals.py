"""Adding Margins and Totals to Aggregations and Pivot Tables.

This module teaches first-year data science students how to compute row, column,
and grand totals using margins=True in pd.pivot_table() and pd.crosstab(),
explaining normalisation and the mathematical nuances of unweighted margins.
"""

import pandas as pd
import numpy as np


def create_university_scholarship_dataset() -> pd.DataFrame:
    """Creates a sample dataset of university scholarships and tuition revenues."""
    data = {
        "campus": [
            "North Sydney", "North Sydney", "North Sydney", "North Sydney",
            "Melbourne", "Melbourne", "Melbourne", "Melbourne",
            "Brisbane", "Brisbane", "Brisbane", "Brisbane",
        ],
        "residency": [
            "Domestic", "International", "Domestic", "International",
            "Domestic", "International", "Domestic", "International",
            "Domestic", "International", "Domestic", "International",
        ],
        "faculty": [
            "Health Sciences", "Health Sciences", "Law & Business", "Law & Business",
            "Health Sciences", "Health Sciences", "Education & Arts", "Education & Arts",
            "Health Sciences", "Health Sciences", "Law & Business", "Law & Business",
        ],
        "enrolments": [450, 150, 380, 220, 520, 180, 410, 90, 320, 110, 290, 140],
        "scholarship_kaud": [45, 60, 30, 85, 50, 75, 25, 40, 35, 55, 20, 65],
    }
    return pd.DataFrame(data)


def demonstrate_pivot_table_margins(df: pd.DataFrame):
    """Demonstrates adding row, column, and grand totals to pivot tables."""
    print("\n--- 1. Pivot Table with Margins (Sum of Enrolments) ---")

    # Sum of enrolments across Campus and Residency with Margins
    enrolment_table = pd.pivot_table(
        df,
        values="enrolments",
        index="campus",
        columns="residency",
        aggfunc="sum",
        margins=True,
        margins_name="Total Enrolments",
    )

    print(enrolment_table)


def demonstrate_margins_nuance(df: pd.DataFrame):
    """Explains why margins compute grand aggregates rather than 'averages of averages'."""
    print("\n--- 2. The Margins Aggregation Nuance (Mean Scholarship) ---")

    # When aggregating by mean, the margin is the true cohort mean, not the average of row means!
    mean_table = pd.pivot_table(
        df,
        values="scholarship_kaud",
        index="campus",
        columns="residency",
        aggfunc="mean",
        margins=True,
        margins_name="Cohort Average",
    )

    print("Average Scholarship (kAUD) with Margins:")
    print(mean_table.round(1))

    # True overall mean of entire dataset
    overall_mean = df["scholarship_kaud"].mean()
    print(f"\nVerification - True unpartitioned mean across all rows: {overall_mean:.1f} kAUD")


def demonstrate_crosstab_and_normalisation(df: pd.DataFrame):
    """Demonstrates pd.crosstab() with margins and percentage normalisation."""
    print("\n--- 3. Frequency Tables with pd.crosstab() ---")

    # Frequency count of offerings
    raw_counts = pd.crosstab(df["campus"], df["faculty"], margins=True, margins_name="Total")
    print("Cohort Observation Counts:")
    print(raw_counts)

    # Row normalisation (percentage of each campus's offerings)
    row_pct = pd.crosstab(
        df["campus"], df["faculty"], normalize="index", margins=True, margins_name="Total"
    ) * 100
    print("\nRow Normalisation (Percentage by Campus):")
    print(row_pct.round(1))


def run_exercises():
    """Hands-on practice exercises for students."""
    print("\n--- 4. Student Practice Exercises ---")

    # Australian national park visitors by state and activity
    park_data = pd.DataFrame({
        "state": ["NSW", "NSW", "VIC", "VIC", "QLD", "QLD", "TAS", "TAS"],
        "activity": ["Hiking", "Camping", "Hiking", "Camping", "Hiking", "Kayaking", "Hiking", "Kayaking"],
        "visitors": [12500, 8400, 11200, 9600, 14100, 4200, 6800, 3100],
    })

    print("National Park Visitors Dataset:")
    print(park_data)

    # Exercise 1: Create a pivot table of total visitors with margins
    visitor_pivot = pd.pivot_table(
        park_data,
        values="visitors",
        index="state",
        columns="activity",
        aggfunc="sum",
        fill_value=0,
        margins=True,
        margins_name="Grand Total",
    )
    print("\nExercise 1 Result - Total Visitors with Grand Totals:")
    print(visitor_pivot)

    # Exercise 2: Frequency cross-tabulation of activities by state normalized by row ('index')
    activity_dist = pd.crosstab(
        park_data["state"], park_data["activity"], normalize="index", margins=True
    ) * 100
    print("\nExercise 2 Result - Activity Proportions (% by State):")
    print(activity_dist.round(1))


def main():
    print("=========================================================")
    print("   Week 10 Topic 06: Adding Margins and Totals in Pandas")
    print("=========================================================")

    df = create_university_scholarship_dataset()
    demonstrate_pivot_table_margins(df)
    demonstrate_margins_nuance(df)
    demonstrate_crosstab_and_normalisation(df)
    run_exercises()

    print("\n[Done] Successfully completed Margins and Totals demonstrations.")


if __name__ == "__main__":
    main()
