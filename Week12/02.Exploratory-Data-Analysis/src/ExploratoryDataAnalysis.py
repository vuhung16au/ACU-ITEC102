"""Exploratory Data Analysis (EDA): A Systematic 5-Step Framework.

This module teaches first-year data science students how to perform systematic
Exploratory Data Analysis (EDA) on an Australian Graduate Employment dataset.
It covers structural auditing, univariate distribution/outlier analysis,
categorical breakdowns, correlation matrices, and group aggregations.
"""

import os
from pathlib import Path
os.environ["MPLCONFIGDIR"] = "/tmp/matplotlib_cache"

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def create_graduate_employment_data() -> pd.DataFrame:
    """Generates a realistic cohort dataset of recent university graduates."""
    np.random.seed(42)
    n = 120

    study_areas = np.random.choice(
        ["Software Engineering", "Data Science", "Cyber Security", "Business Analytics"],
        size=n,
        p=[0.35, 0.25, 0.20, 0.20],
    )

    internships = np.random.choice(["Yes", "No"], size=n, p=[0.60, 0.40])

    gpa = np.random.normal(loc=5.5, scale=0.8, size=n).clip(3.5, 7.0).round(2)

    # Base salary driven by discipline and internship experience + random noise
    discipline_boost = {
        "Software Engineering": 72000,
        "Data Science": 75000,
        "Cyber Security": 74000,
        "Business Analytics": 68000,
    }
    base = np.array([discipline_boost[d] for d in study_areas])
    internship_bonus = np.where(internships == "Yes", 6500, 0)
    salary = base + internship_bonus + (gpa - 5.0) * 4000 + np.random.normal(0, 4500, n)
    salary = salary.round(-2)  # Round to nearest 100

    # Inject 2 realistic outliers: one extreme high-earner, one data entry error
    salary[15] = 240000.0   # Legitimate high-outlier / niche contracting
    salary[42] = 7200.0     # Data entry defect (missing zero: $7,200 instead of $72,000)

    satisfaction = np.random.randint(55, 98, size=n)

    df = pd.DataFrame({
        "graduate_id": [f"GRAD-{2026000 + i}" for i in range(n)],
        "study_area": study_areas,
        "internship": internships,
        "gpa": gpa,
        "starting_salary": salary,
        "satisfaction_score": satisfaction,
    })
    return df


def audit_structure(df: pd.DataFrame):
    """Step 1: Inspect shape, data types, and initial sample."""
    print("--- Step 1: Structural Audit ---")
    print(f"Dataset Shape: {df.shape[0]} rows, {df.shape[1]} columns")
    print("\nData Types and Non-Null Counts:")
    print(df.info())
    print("\nHead of Dataset:")
    print(df.head(5))


def analyse_distributions_and_outliers(df: pd.DataFrame) -> tuple[float, float, pd.DataFrame]:
    """Step 2: Calculate 5-number summary and identify outliers using IQR."""
    print("\n--- Step 2: Distribution & Outlier Detection (Tukey's Fence) ---")
    summary = df[["gpa", "starting_salary", "satisfaction_score"]].describe().T
    print("Five-Number Summary & Statistics:")
    print(summary[["mean", "std", "min", "25%", "50%", "75%", "max"]])

    # IQR rule on starting salary
    q1 = df["starting_salary"].quantile(0.25)
    q3 = df["starting_salary"].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    print(f"\nSalary Q1: ${q1:,.2f} | Q3: ${q3:,.2f} | IQR: ${iqr:,.2f}")
    print(f"Lower Fence (Q1 - 1.5*IQR): ${lower_bound:,.2f}")
    print(f"Upper Fence (Q3 + 1.5*IQR): ${upper_bound:,.2f}")

    outliers = df[(df["starting_salary"] < lower_bound) | (df["starting_salary"] > upper_bound)]
    print(f"\nDetected {len(outliers)} Salary Outlier(s):")
    print(outliers[["graduate_id", "study_area", "starting_salary", "internship"]])
    return lower_bound, upper_bound, outliers


def analyse_categoricals(df: pd.DataFrame):
    """Step 3: Frequency distributions of categorical variables."""
    print("\n--- Step 3: Categorical Breakdown ---")
    print("Graduates by Study Area (Counts & Proportions):")
    counts = df["study_area"].value_counts()
    proportions = df["study_area"].value_counts(normalize=True).mul(100).round(1)
    cat_summary = pd.DataFrame({"Count": counts, "Percentage (%)": proportions})
    print(cat_summary)

    print("\nInternship Participation:")
    print(df["internship"].value_counts(normalize=True).mul(100).round(1))


def analyse_relationships(df: pd.DataFrame):
    """Step 4: Correlation analysis and segmented group summaries."""
    print("\n--- Step 4: Bivariate Correlation & Group Analysis ---")
    numeric_df = df[["gpa", "starting_salary", "satisfaction_score"]]
    corr = numeric_df.corr().round(3)
    print("Correlation Matrix:")
    print(corr)

    print("\nMedian Starting Salary by Study Area and Internship Status:")
    grouped = df.groupby(["study_area", "internship"])["starting_salary"].agg(["count", "median", "mean"]).round(0)
    print(grouped)


def generate_eda_figures(df: pd.DataFrame, lower_bound: float, upper_bound: float):
    """Creates publication-ready EDA visualisations saved to disk."""
    print("\n--- Step 5: Generating EDA Visualisations ---")
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Boxplot of salary across disciplines
    study_order = sorted(df["study_area"].unique())
    salary_data = [df[df["study_area"] == area]["starting_salary"] for area in study_order]

    axes[0].boxplot(salary_data, tick_labels=study_order, patch_artist=True)
    axes[0].set_title("Graduate Starting Salary by Study Area (with Outliers)", fontsize=11, fontweight="bold")
    axes[0].set_ylabel("Starting Salary (AUD)")
    axes[0].grid(True, linestyle="--", alpha=0.5, axis="y")
    axes[0].tick_params(axis="x", rotation=15)

    # Scatter plot: GPA vs Starting Salary coloured by Internship
    intern_yes = df[df["internship"] == "Yes"]
    intern_no = df[df["internship"] == "No"]

    axes[1].scatter(intern_yes["gpa"], intern_yes["starting_salary"], color="#2b5c8f", alpha=0.7, label="Internship Completed")
    axes[1].scatter(intern_no["gpa"], intern_no["starting_salary"], color="#d95f02", alpha=0.7, label="No Internship")
    axes[1].axhline(upper_bound, color="red", linestyle=":", label="Outlier Threshold")
    axes[1].set_title("Starting Salary vs. Academic GPA", fontsize=11, fontweight="bold")
    axes[1].set_xlabel("GPA (3.5 - 7.0 Scale)")
    axes[1].set_ylabel("Starting Salary (AUD)")
    axes[1].legend(loc="upper left")
    axes[1].grid(True, linestyle="--", alpha=0.5)

    plt.tight_layout()
    output_path = Path(__file__).resolve().parent.parent / "graduate_eda_summary.png"
    fig.savefig(output_path, dpi=120)
    plt.close(fig)
    print(f"Saved EDA chart summary to '{output_path}'.")


def run_exercises():
    """Hands-on practice exercises for students."""
    print("\n--- 6. Student Practice Exercises ---")
    data = pd.DataFrame({
        "student_id": [f"S{i}" for i in range(1, 9)],
        "exam_score": [65, 72, 88, 45, 92, 78, 85, 15],  # 15 is an outlier
        "study_hours": [12, 15, 22, 8, 25, 18, 20, 3],
    })
    print("Exercise Dataset:")
    print(data)

    # Calculate IQR for exam_score
    q1 = data["exam_score"].quantile(0.25)
    q3 = data["exam_score"].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    outlier_rows = data[(data["exam_score"] < lower_bound) | (data["exam_score"] > upper_bound)]
    print(f"\nExam Score IQR: {iqr:.1f} | Lower Fence: {lower_bound:.1f} | Upper Fence: {upper_bound:.1f}")
    print("Identified Outlier Student(s):")
    print(outlier_rows)


def main():
    print("=========================================================")
    print("   Week 12 Topic 02: Exploratory Data Analysis (EDA)")
    print("=========================================================")

    df = create_graduate_employment_data()
    audit_structure(df)
    lower, upper, outliers = analyse_distributions_and_outliers(df)
    analyse_categoricals(df)
    analyse_relationships(df)
    generate_eda_figures(df, lower, upper)
    run_exercises()

    print("\n[Done] Successfully completed Exploratory Data Analysis pipeline.")


if __name__ == "__main__":
    main()
