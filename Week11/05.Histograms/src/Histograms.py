"""Histograms in Matplotlib: Frequency Distributions of Continuous Data.

This module teaches first-year data science students how to bin continuous numeric
variables, contrast histograms with bar charts, choose bin sizes, and overlay
central tendency reference lines (mean and median).
"""

import os
os.environ["MPLCONFIGDIR"] = "/tmp/matplotlib_cache"
import matplotlib
matplotlib.use("Agg")  # Non-interactive headless backend for script execution
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def generate_exam_marks() -> np.ndarray:
    """Generates a realistic distribution of final exam marks for 250 university students."""
    np.random.seed(42)
    # Mixture: main cohort centered around 72 + small tail of struggling students
    main_cohort = np.random.normal(loc=73, scale=11, size=220)
    tail_cohort = np.random.normal(loc=42, scale=8, size=30)
    marks = np.concatenate([main_cohort, tail_cohort])
    # Clip marks between 0 and 100
    return np.clip(np.round(marks, 1), 0, 100)


def demonstrate_basic_histogram(marks: np.ndarray) -> plt.Figure:
    """Demonstrates a basic continuous histogram with reference lines for mean and median."""
    print("\n--- 1. Basic Histogram with Mean & Median Reference Lines ---")

    fig, ax = plt.subplots(figsize=(9, 5))

    mean_mark = np.mean(marks)
    median_mark = np.median(marks)

    counts, bins, patches = ax.hist(
        marks,
        bins=15,
        color="#1f77b4",
        edgecolor="black",
        alpha=0.75,
        label="Student Marks",
    )

    # Add vertical reference lines for mean and median
    ax.axvline(mean_mark, color="crimson", linestyle="--", linewidth=2, label=f"Mean: {mean_mark:.1f}")
    ax.axvline(median_mark, color="gold", linestyle="-.", linewidth=2, label=f"Median: {median_mark:.1f}")
    ax.axvline(50, color="darkgrey", linestyle=":", linewidth=1.5, label="Pass Threshold (50)")

    ax.set_title("ITEC102 Final Examination Marks Distribution (n=250)", fontsize=12, fontweight="bold")
    ax.set_xlabel("Exam Mark (%)")
    ax.set_ylabel("Number of Students")
    ax.set_xlim(20, 100)
    ax.grid(axis="y", linestyle=":", alpha=0.6)
    ax.legend(loc="upper left")

    plt.tight_layout()
    fig.savefig("basic_histogram.png", dpi=150)
    plt.close(fig)
    print(f"Saved plot: basic_histogram.png (Mean={mean_mark:.1f}, Median={median_mark:.1f})")
    return fig


def demonstrate_grade_boundary_bins(marks: np.ndarray) -> plt.Figure:
    """Demonstrates explicit custom bin edges matching Australian university grading scales."""
    print("\n--- 2. Custom Grade Boundary Bins ---")

    fig, ax = plt.subplots(figsize=(9, 5))

    # Australian Grading Scale: Fail (<50), Pass (50-64), Credit (65-74), Distinction (75-84), High Distinction (85-100)
    grade_bins = [0, 50, 65, 75, 85, 100]
    grade_colors = ["#d9534f", "#f0ad4e", "#5bc0de", "#0275d8", "#5cb85c"]

    counts, bins, patches = ax.hist(
        marks,
        bins=grade_bins,
        edgecolor="black",
        alpha=0.85,
    )

    # Color each bin according to grade tier
    for patch, color in zip(patches, grade_colors):
        patch.set_facecolor(color)

    ax.set_title("Exam Mark Distribution Binned by Australian Grade Tiers", fontsize=12, fontweight="bold")
    ax.set_xlabel("Mark Range")
    ax.set_ylabel("Number of Students")
    ax.set_xticks(grade_bins)
    ax.set_xticklabels(["0", "50\n(Fail)", "65\n(Pass)", "75\n(Credit)", "85\n(Dist)", "100\n(HD)"])
    ax.grid(axis="y", linestyle=":", alpha=0.6)

    # Add count labels on top of grade bins
    for count, left_edge, right_edge in zip(counts, grade_bins[:-1], grade_bins[1:]):
        mid = (left_edge + right_edge) / 2
        ax.text(mid, count + 2, f"{int(count)} students", ha="center", fontsize=9, fontweight="bold")

    ax.set_ylim(0, max(counts) + 12)
    plt.tight_layout()
    fig.savefig("grade_tier_histogram.png", dpi=150)
    plt.close(fig)
    print("Saved plot: grade_tier_histogram.png")
    return fig


def run_exercises():
    """Hands-on practice exercises for students."""
    print("\n--- 3. Student Practice Exercises ---")

    # Sydney property price distribution (kAUD) - typical right-skewed economic data
    np.random.seed(10)
    prices = np.random.lognormal(mean=7.0, sigma=0.45, size=400)  # median around $1,100k, tail to $4,000k

    print(f"Property Prices (kAUD): n={len(prices)}, Min={prices.min():.0f}, Max={prices.max():.0f}")

    mean_price = np.mean(prices)
    median_price = np.median(prices)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.hist(prices, bins=25, color="cadetblue", edgecolor="black", alpha=0.75)
    ax.axvline(median_price, color="darkorange", linestyle="-", linewidth=2, label=f"Median: ${median_price:,.0f}k")
    ax.axvline(mean_price, color="crimson", linestyle="--", linewidth=2, label=f"Mean: ${mean_price:,.0f}k")

    ax.set_title("Sydney Property Price Distribution: Demonstrating Right Skewness", fontsize=12, fontweight="bold")
    ax.set_xlabel("Price ($k AUD)")
    ax.set_ylabel("Property Count")
    ax.grid(axis="y", linestyle=":", alpha=0.6)
    ax.legend(loc="upper right")

    plt.tight_layout()
    fig.savefig("property_price_histogram.png", dpi=150)
    plt.close(fig)
    print(f"  Saved exercise plot: property_price_histogram.png (Mean={mean_price:.0f}k pulled above Median={median_price:.0f}k by right tail)")


def main():
    print("=========================================================")
    print("   Week 11 Topic 05: Histograms in Matplotlib")
    print("=========================================================")

    marks = generate_exam_marks()
    demonstrate_basic_histogram(marks)
    demonstrate_grade_boundary_bins(marks)
    run_exercises()

    # Clean up generated pngs
    for img in ["basic_histogram.png", "grade_tier_histogram.png", "property_price_histogram.png"]:
        if os.path.exists(img):
            os.remove(img)

    print("\n[Done] Successfully demonstrated Histograms.")


if __name__ == "__main__":
    main()
