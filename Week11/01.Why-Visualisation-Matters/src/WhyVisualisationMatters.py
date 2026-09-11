"""Why Visualisation Matters: Anscombe's Quartet and Matplotlib Anatomy.

This module teaches first-year data science students why summary statistics
alone can be deceptive and introduces the core Object-Oriented anatomy of Matplotlib
(Figure vs. Axes).
"""

import os
from pathlib import Path
import matplotlib
matplotlib.use("Agg")  # Non-interactive headless backend for script execution
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def get_anscombe_quartet() -> list[tuple[np.ndarray, np.ndarray]]:
    """Returns the four datasets comprising Francis Anscombe's famous 1973 quartet."""
    x1 = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5], dtype=float)
    y1 = np.array([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68])

    x2 = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5], dtype=float)
    y2 = np.array([9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74])

    x3 = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5], dtype=float)
    y3 = np.array([7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73])

    x4 = np.array([8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8], dtype=float)
    y4 = np.array([6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89])

    return [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]


def demonstrate_summary_statistics(quartet: list[tuple[np.ndarray, np.ndarray]]):
    """Demonstrates that all four datasets have near-identical summary statistics."""
    print("\n--- 1. Summary Statistics of Anscombe's Quartet ---")
    summaries = []
    for i, (x, y) in enumerate(quartet, 1):
        corr = np.corrcoef(x, y)[0, 1]
        slope, intercept = np.polyfit(x, y, deg=1)
        summaries.append({
            "Dataset": f"Dataset {i}",
            "x Mean": round(float(np.mean(x)), 2),
            "x Var": round(float(np.var(x, ddof=1)), 2),
            "y Mean": round(float(np.mean(y)), 2),
            "y Var": round(float(np.var(y, ddof=1)), 2),
            "Correlation": round(float(corr), 3),
            "Regression Fit": f"y = {slope:.2f}x + {intercept:.2f}",
        })

    summary_df = pd.DataFrame(summaries)
    print(summary_df.to_string(index=False))
    print("\nObservation: In tabular form, all four datasets appear virtually identical!")


def demonstrate_anscombe_plot(quartet: list[tuple[np.ndarray, np.ndarray]]) -> plt.Figure:
    """Plots Anscombe's Quartet in a 2x2 grid using Matplotlib's Object-Oriented interface."""
    print("\n--- 2. Visualising Anscombe's Quartet ---")

    # Create 2x2 subplot grid
    fig, axes = plt.subplots(2, 2, figsize=(10, 8), sharex=True, sharey=True)
    fig.suptitle("Anscombe's Quartet: Same Statistics, Radically Different Distributions", fontsize=14, fontweight="bold")

    descriptions = [
        "Dataset I: Standard Linear Trend",
        "Dataset II: Non-Linear (Quadratic)",
        "Dataset III: Linear with Severe Outlier",
        "Dataset IV: Vertical Cluster with Leverage Point",
    ]

    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]

    # Common x line for regression
    x_line = np.linspace(2, 20, 100)
    y_line = 3.0 + 0.5 * x_line

    for idx, (ax, (x, y)) in enumerate(zip(axes.flat, quartet)):
        # Scatter actual data points
        ax.scatter(x, y, color=colors[idx], s=60, edgecolors="black", zorder=3, label="Data Points")
        # Plot identical fitted regression line
        ax.plot(x_line, y_line, color="black", linestyle="--", linewidth=1.5, label="Fit (y = 0.5x + 3.0)")

        ax.set_title(descriptions[idx], fontsize=11)
        ax.set_xlabel("X Variable")
        ax.set_ylabel("Y Variable")
        ax.grid(True, linestyle=":", alpha=0.6)
        ax.legend(loc="upper left", fontsize=9)
        ax.set_xlim(2, 20)
        ax.set_ylim(2, 14)

    plt.tight_layout()
    output_path = Path(__file__).resolve().parent / "anscombes_quartet.png"
    fig.savefig(output_path, dpi=150)
    plt.close(fig)
    print(f"Generated and saved chart: {output_path.name}")
    return fig


def run_exercises():
    """Hands-on practice exercises for students."""
    print("\n--- 3. Student Practice Exercises ---")

    # Student study hours vs exam mark with a recording typo outlier
    study_hours = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 50])  # Outlier: 50 hours recorded as mark 15
    exam_marks = np.array([45, 52, 58, 63, 67, 72, 75, 80, 84, 88, 92, 15])

    print("Student Study Hours vs Marks Dataset:")
    print("Hours:", study_hours)
    print("Marks:", exam_marks)

    # Exercise 1: Calculate correlation before and after removing the outlier
    corr_with_outlier = np.corrcoef(study_hours, exam_marks)[0, 1]
    # Filter out study_hours > 20
    mask = study_hours <= 20
    corr_without_outlier = np.corrcoef(study_hours[mask], exam_marks[mask])[0, 1]

    print(f"\nExercise 1 Result:")
    print(f"  Correlation WITH outlier:    {corr_with_outlier:.3f} (Severely degraded)")
    print(f"  Correlation WITHOUT outlier: {corr_without_outlier:.3f} (Strong true relationship)")

    # Exercise 2: Plot scatter and save
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(study_hours[mask], exam_marks[mask], color="teal", s=70, label="Standard Students")
    ax.scatter(study_hours[~mask], exam_marks[~mask], color="crimson", s=100, marker="x", label="Identified Outlier")
    ax.set_title("Impact of Data Entry Error on Study Hours vs Exam Marks", fontsize=12)
    ax.set_xlabel("Weekly Study Hours")
    ax.set_ylabel("Final Exam Mark (%)")
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.legend()
    plt.tight_layout()

    outlier_plot_path = Path(__file__).resolve().parent / "student_study_hours_outlier.png"
    fig.savefig(outlier_plot_path, dpi=150)
    plt.close(fig)
    print(f"  Saved plot: {outlier_plot_path.name}")


def main():
    print("=========================================================")
    print("   Week 11 Topic 01: Why Visualisation Matters")
    print("=========================================================")

    quartet = get_anscombe_quartet()
    demonstrate_summary_statistics(quartet)
    demonstrate_anscombe_plot(quartet)
    run_exercises()

    print("\n[Done] Successfully demonstrated Why Visualisation Matters.")


if __name__ == "__main__":
    main()
