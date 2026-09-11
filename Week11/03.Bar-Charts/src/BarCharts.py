"""Bar Charts in Matplotlib: Categorical Data Visualisation.

This module teaches first-year data science students how to create vertical,
horizontal, grouped (clustered), and stacked bar charts for comparing discrete categories,
as well as adding direct data labels.
"""

import os
import matplotlib
matplotlib.use("Agg")  # Non-interactive headless backend for script execution
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def create_enrolment_dataset() -> pd.DataFrame:
    """Creates a sample dataset of university faculty enrolments across Australian campuses."""
    data = {
        "Faculty": [
            "Faculty of Health Sciences",
            "Faculty of Education & Arts",
            "Faculty of Law & Business",
            "Faculty of Theology & Philosophy",
        ],
        "Sydney": [3200, 2100, 2400, 850],
        "Melbourne": [3500, 2300, 1900, 920],
        "Brisbane": [2100, 1400, 1600, 610],
    }
    return pd.DataFrame(data)


def demonstrate_vertical_bar_chart(df: pd.DataFrame) -> plt.Figure:
    """Demonstrates a standard vertical bar chart with direct bar labels."""
    print("\n--- 1. Vertical Bar Chart with Data Labels ---")

    fig, ax = plt.subplots(figsize=(9, 5))

    short_labels = ["Health", "Education", "Business", "Theology"]
    bars = ax.bar(short_labels, df["Sydney"], color="#1f77b4", width=0.5, edgecolor="black")

    # Add numeric value labels on top of bars
    ax.bar_label(bars, padding=4, fontsize=10, fontweight="bold")

    ax.set_title("Sydney Campus Student Enrolments by Faculty", fontsize=12, fontweight="bold")
    ax.set_xlabel("Faculty")
    ax.set_ylabel("Student Count")
    ax.set_ylim(0, 4000)
    ax.grid(axis="y", linestyle="--", alpha=0.5)

    plt.tight_layout()
    fig.savefig("vertical_bar_chart.png", dpi=150)
    plt.close(fig)
    print("Saved plot: vertical_bar_chart.png")
    return fig


def demonstrate_horizontal_bar_chart(df: pd.DataFrame) -> plt.Figure:
    """Demonstrates horizontal bar charts for readable long category titles."""
    print("\n--- 2. Horizontal Bar Chart (Long Labels) ---")

    fig, ax = plt.subplots(figsize=(9, 4.5))

    # Reverse order so the top item appears at the top
    y_pos = np.arange(len(df["Faculty"]))
    bars = ax.barh(y_pos, df["Sydney"], color="#2ca02c", height=0.55, edgecolor="black")

    ax.set_yticks(y_pos, df["Faculty"])
    ax.bar_label(bars, padding=5, fontsize=9)

    ax.set_title("Enrolments by Faculty (Horizontal Layout)", fontsize=12, fontweight="bold")
    ax.set_xlabel("Student Count")
    ax.set_xlim(0, 4000)
    ax.grid(axis="x", linestyle="--", alpha=0.5)

    plt.tight_layout()
    fig.savefig("horizontal_bar_chart.png", dpi=150)
    plt.close(fig)
    print("Saved plot: horizontal_bar_chart.png")
    return fig


def demonstrate_grouped_bar_chart(df: pd.DataFrame) -> plt.Figure:
    """Demonstrates grouped (clustered) bar charts using coordinate width offsets."""
    print("\n--- 3. Grouped (Clustered) Bar Chart ---")

    fig, ax = plt.subplots(figsize=(10, 5.5))

    x = np.arange(len(df["Faculty"]))
    width = 0.25  # Width of each bar

    # Offset positions for side-by-side display
    bars_syd = ax.bar(x - width, df["Sydney"], width, label="Sydney", color="#004c6d")
    bars_mel = ax.bar(x, df["Melbourne"], width, label="Melbourne", color="#257d9d")
    bars_bne = ax.bar(x + width, df["Brisbane"], width, label="Brisbane", color="#de425b")

    short_labels = ["Health Sci", "Education", "Law & Business", "Theology"]
    ax.set_xticks(x, short_labels)
    ax.set_title("Cross-Campus Faculty Enrolments Comparison", fontsize=13, fontweight="bold")
    ax.set_xlabel("Faculty")
    ax.set_ylabel("Student Count")
    ax.set_ylim(0, 4200)
    ax.grid(axis="y", linestyle=":", alpha=0.6)
    ax.legend(loc="upper right")

    plt.tight_layout()
    fig.savefig("grouped_bar_chart.png", dpi=150)
    plt.close(fig)
    print("Saved plot: grouped_bar_chart.png")
    return fig


def demonstrate_stacked_bar_chart(df: pd.DataFrame) -> plt.Figure:
    """Demonstrates stacked bar charts using the bottom parameter."""
    print("\n--- 4. Stacked Bar Chart ---")

    fig, ax = plt.subplots(figsize=(9, 5))

    short_labels = ["Health", "Education", "Business", "Theology"]

    # Sydney is the base
    ax.bar(short_labels, df["Sydney"], label="Sydney", color="#1f77b4", width=0.5)
    # Melbourne stacks on top of Sydney
    ax.bar(short_labels, df["Melbourne"], bottom=df["Sydney"], label="Melbourne", color="#ff7f0e", width=0.5)
    # Brisbane stacks on top of (Sydney + Melbourne)
    bottom_syd_mel = df["Sydney"] + df["Melbourne"]
    ax.bar(short_labels, df["Brisbane"], bottom=bottom_syd_mel, label="Brisbane", color="#2ca02c", width=0.5)

    ax.set_title("Total Enrolments per Faculty (Stacked by Campus)", fontsize=12, fontweight="bold")
    ax.set_xlabel("Faculty")
    ax.set_ylabel("Total Students")
    ax.grid(axis="y", linestyle="--", alpha=0.5)
    ax.legend(loc="upper right")

    plt.tight_layout()
    fig.savefig("stacked_bar_chart.png", dpi=150)
    plt.close(fig)
    print("Saved plot: stacked_bar_chart.png")
    return fig


def run_exercises():
    """Hands-on practice exercises for students."""
    print("\n--- 5. Student Practice Exercises ---")

    # Tech graduate median salaries by discipline (AUD)
    tech_salaries = pd.DataFrame({
        "Discipline": ["Cloud Architecture", "Cyber Security", "Data Science", "Software Engineering"],
        "Bachelor": [92000, 88000, 85000, 82000],
        "Master": [115000, 108000, 105000, 102000],
    })

    print("Tech Graduate Salaries Dataset:")
    print(tech_salaries)

    # Exercise: Grouped horizontal bar chart
    fig, ax = plt.subplots(figsize=(10, 5))
    y = np.arange(len(tech_salaries["Discipline"]))
    height = 0.35

    bars1 = ax.barh(y - height/2, tech_salaries["Bachelor"], height, label="Bachelor Degree", color="steelblue")
    bars2 = ax.barh(y + height/2, tech_salaries["Master"], height, label="Master Degree", color="darkorange")

    ax.set_yticks(y, tech_salaries["Discipline"])
    ax.set_title("Australian Tech Graduate Starting Salaries by Degree Level", fontsize=12, fontweight="bold")
    ax.set_xlabel("Starting Salary ($AUD)")
    ax.set_xlim(0, 135000)
    ax.grid(axis="x", linestyle=":", alpha=0.6)
    ax.legend(loc="lower right")

    plt.tight_layout()
    fig.savefig("tech_salaries_grouped_bar.png", dpi=150)
    plt.close(fig)
    print("  Saved exercise plot: tech_salaries_grouped_bar.png")


def main():
    print("=========================================================")
    print("   Week 11 Topic 03: Bar Charts in Matplotlib")
    print("=========================================================")

    df = create_enrolment_dataset()
    demonstrate_vertical_bar_chart(df)
    demonstrate_horizontal_bar_chart(df)
    demonstrate_grouped_bar_chart(df)
    demonstrate_stacked_bar_chart(df)
    run_exercises()

    # Clean up generated pngs
    for img in ["vertical_bar_chart.png", "horizontal_bar_chart.png", "grouped_bar_chart.png", "stacked_bar_chart.png", "tech_salaries_grouped_bar.png"]:
        if os.path.exists(img):
            os.remove(img)

    print("\n[Done] Successfully demonstrated Bar Charts.")


if __name__ == "__main__":
    main()
