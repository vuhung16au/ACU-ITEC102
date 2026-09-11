"""Customising and Styling in Matplotlib: Publication-Quality Dashboards.

This module teaches first-year data science students how to apply built-in themes,
construct multi-panel subplots (plt.subplots), add annotations, and export
high-resolution figures.
"""

import os
os.environ["MPLCONFIGDIR"] = "/tmp/matplotlib_cache"
import matplotlib
matplotlib.use("Agg")  # Non-interactive headless backend for script execution
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def create_performance_dashboard_dataset() -> tuple[pd.DataFrame, pd.DataFrame]:
    """Creates sample datasets of campus performance and student metrics."""
    campus_df = pd.DataFrame({
        "Campus": ["North Sydney", "Melbourne", "Brisbane", "Strathfield"],
        "Enrolments": [4200, 4800, 2600, 1900],
        "Pass_Rate": [88.5, 85.0, 82.3, 91.0],
    })

    np.random.seed(42)
    attendance = np.random.uniform(60, 100, size=150)
    # WAM correlates positively with attendance
    wam = 25 + 0.65 * attendance + np.random.normal(0, 5, size=150)
    wam = np.clip(wam, 35, 100)

    student_df = pd.DataFrame({"Attendance": attendance, "WAM": wam})
    return campus_df, student_df


def demonstrate_multi_panel_dashboard(campus_df: pd.DataFrame, student_df: pd.DataFrame) -> plt.Figure:
    """Demonstrates building a 2x2 multi-panel figure with unified styling and annotations."""
    print("\n--- 1. Building a 2x2 Multi-Panel Styled Dashboard ---")

    # Apply a clean, modern built-in style
    plt.style.use("seaborn-v0_8-whitegrid")

    fig, axes = plt.subplots(2, 2, figsize=(12, 9))
    fig.suptitle("ACU Academic Performance & Student Engagement Dashboard", fontsize=15, fontweight="bold")

    # Subplot 1: Top-Left - Campus Enrolments (Horizontal Bar Chart)
    ax1 = axes[0, 0]
    bars = ax1.barh(campus_df["Campus"], campus_df["Enrolments"], color="#1f77b4", height=0.55)
    ax1.bar_label(bars, padding=4, fmt="%d")
    ax1.set_title("Total Enrolments by Campus", fontsize=11, fontweight="bold")
    ax1.set_xlabel("Number of Students")
    ax1.set_xlim(0, 5500)

    # Subplot 2: Top-Right - Attendance vs WAM (Scatter with Annotation)
    ax2 = axes[0, 1]
    scatter = ax2.scatter(student_df["Attendance"], student_df["WAM"], c=student_df["WAM"], cmap="viridis", alpha=0.7, edgecolors="none")
    fig.colorbar(scatter, ax=ax2, label="WAM Score")
    # Add trendline
    slope, intercept = np.polyfit(student_df["Attendance"], student_df["WAM"], 1)
    x_line = np.linspace(60, 100, 50)
    ax2.plot(x_line, slope * x_line + intercept, color="crimson", linestyle="--", linewidth=1.8, label="Linear Trend")

    # Annotate high achiever
    ax2.annotate(
        "High Attendance & WAM",
        xy=(98, 92),
        xytext=(70, 95),
        arrowprops=dict(facecolor="black", arrowstyle="->", lw=1.5),
        fontweight="bold",
        fontsize=9,
    )
    ax2.set_title("Student Attendance vs. WAM", fontsize=11, fontweight="bold")
    ax2.set_xlabel("Attendance Rate (%)")
    ax2.set_ylabel("Weighted Average Mark (WAM)")
    ax2.legend(loc="lower right")

    # Subplot 3: Bottom-Left - Pass Rates by Campus
    ax3 = axes[1, 0]
    pass_bars = ax3.bar(campus_df["Campus"], campus_df["Pass_Rate"], color="#2ca02c", width=0.45)
    ax3.bar_label(pass_bars, padding=3, fmt="%.1f%%")
    ax3.axhline(85.0, color="orange", linestyle=":", linewidth=1.8, label="Target Benchmark (85%)")
    ax3.set_title("Course Pass Rates by Campus", fontsize=11, fontweight="bold")
    ax3.set_ylabel("Pass Rate (%)")
    ax3.set_ylim(0, 100)
    ax3.legend(loc="lower left")

    # Subplot 4: Bottom-Right - WAM Distribution
    ax4 = axes[1, 1]
    ax4.hist(student_df["WAM"], bins=15, color="#9467bd", edgecolor="black", alpha=0.8)
    median_wam = student_df["WAM"].median()
    ax4.axvline(median_wam, color="red", linestyle="--", linewidth=2, label=f"Median: {median_wam:.1f}")
    ax4.set_title("Cohort WAM Distribution", fontsize=11, fontweight="bold")
    ax4.set_xlabel("WAM")
    ax4.set_ylabel("Student Count")
    ax4.legend(loc="upper left")

    plt.tight_layout()
    output_path = "academic_performance_dashboard.png"
    fig.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved dashboard figure: {output_path}")
    return fig


def run_exercises():
    """Hands-on practice exercises for students."""
    print("\n--- 2. Student Practice Exercises ---")

    # 1x2 Side-by-Side Figure
    units = ["ITEC102", "ITEC105", "ITEC108", "ITEC110"]
    satisfaction = [92.5, 88.0, 84.5, 90.0]
    enrolments = [320, 280, 240, 210]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))

    # Left: Enrolments
    bars = ax1.bar(units, enrolments, color="teal", width=0.5)
    ax1.bar_label(bars, padding=3)
    ax1.set_title("Unit Enrolments", fontsize=11, fontweight="bold")
    ax1.set_ylabel("Students")

    # Right: Student Satisfaction (%)
    bars2 = ax2.bar(units, satisfaction, color="coral", width=0.5)
    ax2.bar_label(bars2, padding=3, fmt="%.1f%%")
    ax2.axhline(90.0, color="grey", linestyle="--", label="ACU Target (90%)")
    ax2.set_title("Student Satisfaction Rating", fontsize=11, fontweight="bold")
    ax2.set_ylabel("Satisfaction (%)")
    ax2.set_ylim(0, 100)
    ax2.legend()

    plt.tight_layout()
    fig.savefig("unit_summary_exercise.png", dpi=150)
    plt.close(fig)
    print("  Saved exercise plot: unit_summary_exercise.png")


def main():
    print("=========================================================")
    print("   Week 11 Topic 06: Customising and Styling in Matplotlib")
    print("=========================================================")

    campus_df, student_df = create_performance_dashboard_dataset()
    demonstrate_multi_panel_dashboard(campus_df, student_df)
    run_exercises()

    # Clean up generated pngs
    for img in ["academic_performance_dashboard.png", "unit_summary_exercise.png"]:
        if os.path.exists(img):
            os.remove(img)

    print("\n[Done] Successfully demonstrated Customising and Styling.")


if __name__ == "__main__":
    main()
