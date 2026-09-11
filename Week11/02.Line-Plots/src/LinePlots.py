"""Line Plots in Matplotlib: Time-Series and Continuous Trend Visualisation.

This module teaches first-year data science students how to create, format,
and style line plots to illustrate trends across time or continuous variables.
"""

import os
import matplotlib
matplotlib.use("Agg")  # Non-interactive headless backend for script execution
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def create_temperature_dataset() -> pd.DataFrame:
    """Creates a sample dataset of monthly mean temperatures across Australian capital cities."""
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    data = {
        "Month": months,
        "Sydney": [26.0, 25.8, 24.8, 22.5, 19.5, 17.0, 16.4, 17.9, 20.1, 22.2, 23.7, 25.2],
        "Melbourne": [26.0, 25.8, 23.9, 20.3, 16.7, 14.1, 13.5, 15.0, 17.3, 19.7, 22.0, 24.2],
        "Brisbane": [30.4, 30.1, 29.0, 27.2, 24.5, 22.0, 21.9, 23.4, 25.7, 27.1, 28.3, 29.6],
    }
    return pd.DataFrame(data)


def demonstrate_single_line_plot(df: pd.DataFrame) -> plt.Figure:
    """Demonstrates a basic line plot tracking Sydney monthly temperatures."""
    print("\n--- 1. Basic Single Line Plot ---")

    fig, ax = plt.subplots(figsize=(8, 4.5))

    ax.plot(
        df["Month"],
        df["Sydney"],
        color="#1f77b4",
        linestyle="-",
        linewidth=2.0,
        marker="o",
        markersize=6,
        label="Sydney",
    )

    ax.set_title("Sydney Monthly Mean Temperature Trend", fontsize=12, fontweight="bold")
    ax.set_xlabel("Month")
    ax.set_ylabel("Temperature (°C)")
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.legend(loc="upper right")

    plt.tight_layout()
    fig.savefig("sydney_temperature.png", dpi=150)
    plt.close(fig)
    print("Saved plot: sydney_temperature.png")
    return fig


def demonstrate_multi_line_plot(df: pd.DataFrame) -> plt.Figure:
    """Demonstrates plotting multiple lines on the same axes with distinct styles and legend."""
    print("\n--- 2. Comparative Multi-Line Plot ---")

    fig, ax = plt.subplots(figsize=(9, 5))

    # Sydney
    ax.plot(
        df["Month"], df["Sydney"],
        color="#004c6d", linestyle="-", linewidth=2.2,
        marker="o", markersize=6, label="Sydney",
    )

    # Melbourne
    ax.plot(
        df["Month"], df["Melbourne"],
        color="#257d9d", linestyle="--", linewidth=2.0,
        marker="s", markersize=6, label="Melbourne",
    )

    # Brisbane
    ax.plot(
        df["Month"], df["Brisbane"],
        color="#de425b", linestyle="-.", linewidth=2.0,
        marker="^", markersize=6, label="Brisbane",
    )

    ax.set_title("Australian Capital Cities: Annual Temperature Profiles", fontsize=13, fontweight="bold")
    ax.set_xlabel("Month", fontsize=10)
    ax.set_ylabel("Mean Maximum Temperature (°C)", fontsize=10)
    ax.set_ylim(10, 35)
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.legend(loc="lower center", ncol=3, frameon=True)

    plt.tight_layout()
    fig.savefig("australia_city_temperatures.png", dpi=150)
    plt.close(fig)
    print("Saved plot: australia_city_temperatures.png")
    return fig


def run_exercises():
    """Hands-on practice exercises for students."""
    print("\n--- 3. Student Practice Exercises ---")

    # Monthly Australian renewable energy generation (GWh)
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    energy_df = pd.DataFrame({
        "Month": months,
        "Solar_GWh": [3200, 2900, 2600, 2100, 1700, 1450, 1600, 2050, 2500, 3100, 3400, 3600],
        "Wind_GWh": [2400, 2200, 2500, 2700, 3100, 3400, 3300, 3200, 2900, 2800, 2600, 2500],
    })

    print("Australian Renewable Energy Generation (GWh):")
    print(energy_df.head(6))

    # Exercise 1: Create comparative line plot for Solar vs Wind
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(energy_df["Month"], energy_df["Solar_GWh"], color="goldenrod", linestyle="-", linewidth=2.2, marker="o", label="Solar Generation")
    ax.plot(energy_df["Month"], energy_df["Wind_GWh"], color="teal", linestyle="--", linewidth=2.0, marker="^", label="Wind Generation")

    # Exercise 2: Highlight the summer peak for solar using an annotation
    peak_month = energy_df.loc[energy_df["Solar_GWh"].idxmax()]
    ax.annotate(
        f"Peak Solar: {peak_month['Solar_GWh']} GWh",
        xy=(peak_month["Month"], peak_month["Solar_GWh"]),
        xytext=(8, 3800),
        arrowprops=dict(facecolor="black", shrink=0.08, width=1, headwidth=6),
        fontsize=9,
        fontweight="bold",
    )

    ax.set_title("Australian National Energy Market: Solar vs Wind Generation", fontsize=12, fontweight="bold")
    ax.set_xlabel("Month")
    ax.set_ylabel("Generation (GWh)")
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.legend(loc="lower left")

    plt.tight_layout()
    fig.savefig("renewable_energy_comparison.png", dpi=150)
    plt.close(fig)
    print("  Saved exercise plot: renewable_energy_comparison.png")


def main():
    print("=========================================================")
    print("   Week 11 Topic 02: Line Plots in Matplotlib")
    print("=========================================================")

    df = create_temperature_dataset()
    demonstrate_single_line_plot(df)
    demonstrate_multi_line_plot(df)
    run_exercises()

    # Clean up generated pngs
    for img in ["sydney_temperature.png", "australia_city_temperatures.png", "renewable_energy_comparison.png"]:
        if os.path.exists(img):
            os.remove(img)

    print("\n[Done] Successfully demonstrated Line Plots.")


if __name__ == "__main__":
    main()
