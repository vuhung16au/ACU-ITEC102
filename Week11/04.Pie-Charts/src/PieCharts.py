"""Pie Charts and Donut Charts in Matplotlib: Proportions and Visual Perception.

This module teaches first-year data science students how to construct pie and donut
charts for part-to-whole relationships, apply slice emphasis (explode), and understand
the perceptual limitations of radial charts versus bar charts.
"""

import os
os.environ["MPLCONFIGDIR"] = "/tmp/matplotlib_cache"
import matplotlib
matplotlib.use("Agg")  # Non-interactive headless backend for script execution
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def create_energy_mix_dataset() -> pd.DataFrame:
    """Creates a sample dataset of the Australian National Electricity Market generation mix."""
    data = {
        "Source": ["Coal", "Solar", "Wind", "Gas", "Hydro", "Bioenergy/Storage"],
        "Share_pct": [46.5, 21.2, 14.8, 9.2, 6.5, 1.8],
    }
    return pd.DataFrame(data)


def demonstrate_standard_pie_chart(df: pd.DataFrame) -> plt.Figure:
    """Demonstrates a standard pie chart with percentages and slice explosion."""
    print("\n--- 1. Standard Pie Chart with Explode ---")

    fig, ax = plt.subplots(figsize=(8, 6))

    # Explode the 2nd slice (Solar) to draw attention to renewable growth
    explode = (0.0, 0.1, 0.0, 0.0, 0.0, 0.0)
    colors = ["#4a4a4a", "#ffbb33", "#33b5e5", "#ff4444", "#00C851", "#aa66cc"]

    wedges, texts, autotexts = ax.pie(
        df["Share_pct"],
        explode=explode,
        labels=df["Source"],
        autopct="%1.1f%%",
        pctdistance=0.75,
        startangle=140,
        colors=colors,
        wedgeprops=dict(edgecolor="white", linewidth=1.5),
    )

    # Style percentage font
    for at in autotexts:
        at.set_color("black")
        at.set_fontsize(9)
        at.set_fontweight("bold")

    ax.set_title("Australian National Electricity Market: Generation Mix (%)", fontsize=12, fontweight="bold")

    plt.tight_layout()
    fig.savefig("standard_pie_chart.png", dpi=150)
    plt.close(fig)
    print("Saved plot: standard_pie_chart.png")
    return fig


def demonstrate_donut_chart(df: pd.DataFrame) -> plt.Figure:
    """Demonstrates a modern Donut Chart with central metric text."""
    print("\n--- 2. Modern Donut Chart ---")

    fig, ax = plt.subplots(figsize=(8, 6))

    colors = ["#4a4a4a", "#ffbb33", "#33b5e5", "#ff4444", "#00C851", "#aa66cc"]

    wedges, texts, autotexts = ax.pie(
        df["Share_pct"],
        labels=df["Source"],
        autopct="%1.1f%%",
        pctdistance=0.82,
        startangle=90,
        colors=colors,
        wedgeprops=dict(width=0.4, edgecolor="white", linewidth=2),  # width creates the donut hole!
    )

    for at in autotexts:
        at.set_fontsize(9)
        at.set_fontweight("bold")

    # Central hole text
    ax.text(0, 0, "Total\n218 TWh", ha="center", va="center", fontsize=13, fontweight="bold", color="#333333")

    ax.set_title("Australian Energy Generation Mix (Donut Chart)", fontsize=12, fontweight="bold")

    plt.tight_layout()
    fig.savefig("donut_chart.png", dpi=150)
    plt.close(fig)
    print("Saved plot: donut_chart.png")
    return fig


def demonstrate_pie_vs_bar(df: pd.DataFrame) -> plt.Figure:
    """Compares a Pie Chart against a sorted Bar Chart to illustrate visual perceptual accuracy."""
    print("\n--- 3. Perceptual Comparison: Pie vs. Horizontal Bar Chart ---")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

    # Pie Chart on left
    ax1.pie(df["Share_pct"], labels=df["Source"], autopct="%1.1f%%", startangle=90)
    ax1.set_title("Pie Chart: Angles & Areas (Harder to rank)", fontsize=11, fontweight="bold")

    # Sorted Horizontal Bar Chart on right
    sorted_df = df.sort_values(by="Share_pct", ascending=True)
    bars = ax2.barh(sorted_df["Source"], sorted_df["Share_pct"], color="steelblue", height=0.6)
    ax2.bar_label(bars, fmt="%.1f%%", padding=3, fontweight="bold")
    ax2.set_xlim(0, 55)
    ax2.set_xlabel("Share of Total Generation (%)")
    ax2.set_title("Bar Chart: Lengths (Instant, unambiguous ranking)", fontsize=11, fontweight="bold")
    ax2.grid(axis="x", linestyle=":", alpha=0.6)

    plt.tight_layout()
    fig.savefig("pie_vs_bar_comparison.png", dpi=150)
    plt.close(fig)
    print("Saved plot: pie_vs_bar_comparison.png")
    return fig


def run_exercises():
    """Hands-on practice exercises for students."""
    print("\n--- 4. Student Practice Exercises ---")

    # University student enrolment composition
    student_cohort = pd.DataFrame({
        "Cohort": ["Domestic Full-Time", "Domestic Part-Time", "International Full-Time", "International Part-Time"],
        "Students": [5800, 2200, 1500, 500],
    })

    print("Student Cohort Dataset:")
    print(student_cohort)

    # Exercise: Donut chart with explode on International Full-Time
    fig, ax = plt.subplots(figsize=(7, 6))
    explode = (0, 0, 0.1, 0)
    cohort_colors = ["#1f77b4", "#aec7e8", "#ff7f0e", "#ffbb78"]

    ax.pie(
        student_cohort["Students"],
        explode=explode,
        labels=student_cohort["Cohort"],
        autopct="%1.1f%%",
        pctdistance=0.8,
        colors=cohort_colors,
        wedgeprops=dict(width=0.45, edgecolor="white", linewidth=2),
    )

    total_enrolments = student_cohort["Students"].sum()
    ax.text(0, 0, f"Enrolments\n{total_enrolments:,}", ha="center", va="center", fontsize=11, fontweight="bold")
    ax.set_title("ACU Student Cohort Residency and Study Mode", fontsize=12, fontweight="bold")

    plt.tight_layout()
    fig.savefig("student_cohort_donut.png", dpi=150)
    plt.close(fig)
    print("  Saved exercise plot: student_cohort_donut.png")


def main():
    print("=========================================================")
    print("   Week 11 Topic 04: Pie and Donut Charts in Matplotlib")
    print("=========================================================")

    df = create_energy_mix_dataset()
    demonstrate_standard_pie_chart(df)
    demonstrate_donut_chart(df)
    demonstrate_pie_vs_bar(df)
    run_exercises()

    # Clean up generated pngs
    for img in ["standard_pie_chart.png", "donut_chart.png", "pie_vs_bar_comparison.png", "student_cohort_donut.png"]:
        if os.path.exists(img):
            os.remove(img)

    print("\n[Done] Successfully demonstrated Pie and Donut Charts.")


if __name__ == "__main__":
    main()
