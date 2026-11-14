"""Seaborn visualisation suite for the SciPy Statistical EDA pipeline."""

from pathlib import Path
import matplotlib
import numpy as np
import pandas as pd
from scipy import stats

# Use non-interactive backend so charts render cleanly in terminals and CI/tests.
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

from src.stats_analysis import (
    CorrelationAnalysisResult,
    GroupComparisonResult,
    MonteCarloSplitResult,
)

# Set a clean, consistent Seaborn theme for all figures.
sns.set_theme(style="whitegrid", context="notebook", palette="Set2")


# Consistent colour mapping so Male and Female keep identical colours across all charts.
SEX_ORDER = ["Male", "Female"]
SEX_PALETTE = {"Male": "#4c72b0", "Female": "#dd8452"}


def plot_weight_change_by_sex(
    df_clean: pd.DataFrame,
    comparison: GroupComparisonResult,
    output_dir: Path,
) -> Path:
    """Plot distribution and boxplot of 12-week weight change by sex."""
    output_dir.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # Left panel: Overlapping density histogram + KDE
    sns.histplot(
        data=df_clean,
        x="weight_change",
        hue="sex_label",
        hue_order=SEX_ORDER,
        palette=SEX_PALETTE,
        kde=True,
        stat="density",
        common_norm=False,
        alpha=0.35,
        ax=axes[0],
    )
    axes[0].axvline(
        comparison.mean_a,
        color=SEX_PALETTE["Male"],
        linestyle="--",
        linewidth=2.0,
        label=f"Male mean ({comparison.mean_a:.2f} kg)",
    )
    axes[0].axvline(
        comparison.mean_b,
        color=SEX_PALETTE["Female"],
        linestyle="--",
        linewidth=2.0,
        label=f"Female mean ({comparison.mean_b:.2f} kg)",
    )
    axes[0].set_title("Distribution of 12-Week Weight Change by Sex")
    axes[0].set_xlabel("Weight Change (kg) [negative = weight loss]")
    axes[0].set_ylabel("Density")
    axes[0].legend(fontsize=9)

    # Right panel: Boxplot summary with Welch's t-test annotation
    sns.boxplot(
        data=df_clean,
        x="sex_label",
        y="weight_change",
        order=SEX_ORDER,
        hue="sex_label",
        hue_order=SEX_ORDER,
        palette=SEX_PALETTE,
        legend=False,
        width=0.45,
        ax=axes[1],
    )
    axes[1].axhline(0, color="grey", linestyle=":", linewidth=1)
    axes[1].set_title(
        f"Group Comparison (Welch t = {comparison.t_stat:.2f}, p = {comparison.p_value:.2e})"
    )
    axes[1].set_xlabel("Sex")
    axes[1].set_ylabel("Weight Change (kg)")

    fig.tight_layout()
    out_path = output_dir / "01_weight_change_by_sex.png"
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return out_path


def plot_random_splits_pvalues(
    mc_result: MonteCarloSplitResult,
    output_dir: Path,
) -> Path:
    """Plot -log10(p-value) histogram across 1,000 random 50/50 dataset splits."""
    output_dir.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(9, 5))

    threshold = -np.log10(mc_result.alpha)
    sns.histplot(
        mc_result.negative_log10_p,
        bins=40,
        kde=False,
        color="steelblue",
        edgecolor="black",
        ax=ax,
    )
    ax.axvline(
        threshold,
        color="crimson",
        linestyle="--",
        linewidth=2,
        label=f"p = {mc_result.alpha} threshold (-log10 = {threshold:.2f})",
    )
    pct_sig = mc_result.proportion_below_alpha * 100
    ax.set_title(
        f"P-value Results from {mc_result.n_iterations:,} Random Splits "
        f"({pct_sig:.1f}% below p = {mc_result.alpha})"
    )
    ax.set_xlabel("-log10(p-value) [higher = smaller p-value]")
    ax.set_ylabel("Number of Random Split Tests")
    ax.legend()

    fig.tight_layout()
    out_path = output_dir / "02_random_splits_neg_log10_p.png"
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return out_path


def plot_weight_height_ratio_by_sex(
    df_clean: pd.DataFrame,
    ratio_comparison: GroupComparisonResult,
    output_dir: Path,
) -> Path:
    """Plot weight-to-height ratio (kg/cm) by sex using Seaborn violin + box plots."""
    output_dir.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(8, 5))

    sns.violinplot(
        data=df_clean,
        x="sex_label",
        y="weight_height_ratio",
        order=SEX_ORDER,
        hue="sex_label",
        hue_order=SEX_ORDER,
        palette=SEX_PALETTE,
        legend=False,
        inner="quartile",
        alpha=0.75,
        ax=ax,
    )
    ax.set_title(
        f"Weight-to-Height Ratio by Sex "
        f"(Welch t = {ratio_comparison.t_stat:.2f}, p = {ratio_comparison.p_value:.2e})"
    )
    ax.set_xlabel("Sex")
    ax.set_ylabel("Weight-to-Height Ratio (kg / cm)")

    # Annotate means directly on the chart
    ax.text(
        0,
        ratio_comparison.mean_a,
        f" Mean: {ratio_comparison.mean_a:.3f}",
        ha="left",
        va="bottom",
        fontsize=9,
        fontweight="bold",
        bbox={"boxstyle": "round,pad=0.2", "facecolor": "white", "alpha": 0.8},
    )
    ax.text(
        1,
        ratio_comparison.mean_b,
        f" Mean: {ratio_comparison.mean_b:.3f}",
        ha="left",
        va="bottom",
        fontsize=9,
        fontweight="bold",
        bbox={"boxstyle": "round,pad=0.2", "facecolor": "white", "alpha": 0.8},
    )

    fig.tight_layout()
    out_path = output_dir / "03_weight_height_ratio_by_sex.png"
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return out_path


def plot_correlation_matrix_and_scatter(
    df_clean: pd.DataFrame,
    corr_result: CorrelationAnalysisResult,
    output_dir: Path,
    seed: int = 42,
) -> Path:
    """Plot Pearson correlation matrix heatmap and exercise vs weight-change trend."""
    output_dir.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(
        1,
        2,
        figsize=(16, 6.5),
        gridspec_kw={"width_ratios": [1.25, 1], "wspace": 0.35},
        layout="constrained",
    )

    # Left panel: Annotated lower-triangle correlation heatmap
    mask = np.triu(np.ones_like(corr_result.pearson_r, dtype=bool), k=1)
    sns.heatmap(
        corr_result.pearson_r,
        mask=mask,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        center=0.0,
        vmin=-1.0,
        vmax=1.0,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.8, "label": "Pearson r"},
        ax=axes[0],
    )
    axes[0].set_title("Pearson Correlation Matrix (Numeric Survey Variables)")
    axes[0].tick_params(axis="x", rotation=35)
    axes[0].tick_params(axis="y", rotation=0)

    # Right panel: Subsampled scatter + regression line for exercise vs weight change
    sample_df = df_clean.sample(n=min(1500, len(df_clean)), random_state=seed)
    r_val, p_val = stats.pearsonr(df_clean["weekly_exercise_hrs"], df_clean["weight_change"])

    sns.regplot(
        data=sample_df,
        x="weekly_exercise_hrs",
        y="weight_change",
        scatter_kws={"alpha": 0.25, "s": 18, "color": "teal"},
        line_kws={"color": "crimson", "linewidth": 2},
        ax=axes[1],
    )
    axes[1].axhline(0, color="grey", linestyle=":", linewidth=1)
    axes[1].set_title(
        f"Exercise Hours vs Weight Change (r = {r_val:.3f}, p = {p_val:.2e})"
    )
    axes[1].set_xlabel("Weekly Exercise (hours)")
    axes[1].set_ylabel("12-Week Weight Change (kg)")

    out_path = output_dir / "04_correlation_matrix_heatmap.png"
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return out_path


def generate_all_visualisations(
    df_clean: pd.DataFrame,
    weight_change_cmp: GroupComparisonResult,
    mc_result: MonteCarloSplitResult,
    ratio_cmp: GroupComparisonResult,
    corr_result: CorrelationAnalysisResult,
    output_dir: Path,
) -> list[Path]:
    """Generate all four Seaborn plots and return their saved file paths."""
    return [
        plot_weight_change_by_sex(df_clean, weight_change_cmp, output_dir),
        plot_random_splits_pvalues(mc_result, output_dir),
        plot_weight_height_ratio_by_sex(df_clean, ratio_cmp, output_dir),
        plot_correlation_matrix_and_scatter(df_clean, corr_result, output_dir),
    ]
