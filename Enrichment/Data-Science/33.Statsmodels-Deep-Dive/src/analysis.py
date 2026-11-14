"""Focused statsmodels demonstrations extending Pandas and SciPy workflows.

Covers four practical upgrades:
  1. DescrStatsW + Q-Q plots: 95% confidence intervals & normality checks
  2. OLS regression (simple & multiple): R², slopes, and structural collinearity
  3. CompareMeans: degrees of freedom & 95% CI for group-mean differences
  4. multipletests (BH FDR & Bonferroni): controlling false positives across 1,000 splits
"""

from dataclasses import dataclass
from pathlib import Path
import matplotlib
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.multitest import multipletests
from statsmodels.stats.weightstats import CompareMeans, DescrStatsW

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid", context="notebook")


@dataclass
class GroupDifferenceCI:
    """SciPy Welch's t-test paired with statsmodels CompareMeans CI and DoF."""

    scipy_t: float
    scipy_p: float
    sm_t: float
    sm_p: float
    dof: float
    male_mean: float
    female_mean: float
    mean_diff: float
    ci_low: float
    ci_high: float


@dataclass
class MultipleTestingSummary:
    """Comparison of raw vs corrected p-values across 1,000 random splits."""

    n_iterations: int
    raw_p_values: np.ndarray
    fdr_bh_p_values: np.ndarray
    bonferroni_p_values: np.ndarray
    raw_rejected_count: int
    fdr_bh_rejected_count: int
    bonferroni_rejected_count: int
    alpha: float


def compute_mean_confidence_intervals(
    df: pd.DataFrame,
    columns: list[str] | None = None,
    alpha: float = 0.05,
) -> pd.DataFrame:
    """Compute mean, std, and 95% confidence intervals using DescrStatsW."""
    if columns is None:
        columns = ["weight2", "wtyrago", "htm3", "weight_change"]

    rows = []
    for col in columns:
        dsw = DescrStatsW(df[col].to_numpy(dtype=float))
        ci_low, ci_high = dsw.tconfint_mean(alpha=alpha)
        rows.append(
            {
                "variable": col,
                "n": int(dsw.nobs),
                "mean": float(dsw.mean),
                "std": float(dsw.std),
                "ci_95_low": float(ci_low),
                "ci_95_high": float(ci_high),
            }
        )
    return pd.DataFrame(rows)


def fit_ols_models(df: pd.DataFrame) -> tuple[object, object]:
    """Fit simple and multiple OLS regression models on weight_change.

    - Simple OLS:   weight_change ~ weight2
    - Multiple OLS: weight_change ~ weight2 + wtyrago + age
      Demonstrates structural collinearity: because weight_change = weight2 - wtyrago,
      including both components drives R² to 1.000, masking weaker biological links.
    """
    simple_model = smf.ols("weight_change ~ weight2", data=df).fit()
    multiple_model = smf.ols("weight_change ~ weight2 + wtyrago + age", data=df).fit()
    return simple_model, multiple_model


def compare_groups_with_ci(
    df: pd.DataFrame,
    metric: str = "weight_change",
    alpha: float = 0.05,
) -> GroupDifferenceCI:
    """Pair scipy.stats.ttest_ind with statsmodels CompareMeans for CIs and DoF."""
    male = df.loc[df["sex"] == 1, metric].to_numpy(dtype=float)
    female = df.loc[df["sex"] == 2, metric].to_numpy(dtype=float)

    # Primary hypothesis test via SciPy
    scipy_res = stats.ttest_ind(male, female, equal_var=False)

    # Supplementary diagnostics via statsmodels CompareMeans
    cm = CompareMeans(DescrStatsW(male), DescrStatsW(female))
    sm_t, sm_p, dof = cm.ttest_ind(usevar="unequal")
    ci_low, ci_high = cm.tconfint_diff(alpha=alpha, usevar="unequal")

    male_mean = float(np.mean(male))
    female_mean = float(np.mean(female))

    return GroupDifferenceCI(
        scipy_t=float(scipy_res.statistic),
        scipy_p=float(scipy_res.pvalue),
        sm_t=float(sm_t),
        sm_p=float(sm_p),
        dof=float(dof),
        male_mean=male_mean,
        female_mean=female_mean,
        mean_diff=male_mean - female_mean,
        ci_low=float(ci_low),
        ci_high=float(ci_high),
    )


def random_splits_with_multitest(
    values: np.ndarray,
    n_iterations: int = 1000,
    seed: int = 42,
    alpha: float = 0.05,
) -> MultipleTestingSummary:
    """Run 1,000 random 50/50 splits and apply BH FDR & Bonferroni corrections."""
    arr = np.asarray(values, dtype=float)
    half = len(arr) // 2
    rng = np.random.default_rng(seed)

    raw_p = np.empty(n_iterations, dtype=float)
    for i in range(n_iterations):
        perm = rng.permutation(len(arr))
        g1 = arr[perm[:half]]
        g2 = arr[perm[half : half * 2]]
        raw_p[i] = stats.ttest_ind(g1, g2, equal_var=False).pvalue

    reject_bh, p_bh, _, _ = multipletests(raw_p, alpha=alpha, method="fdr_bh")
    reject_bonf, p_bonf, _, _ = multipletests(raw_p, alpha=alpha, method="bonferroni")

    return MultipleTestingSummary(
        n_iterations=n_iterations,
        raw_p_values=raw_p,
        fdr_bh_p_values=p_bh,
        bonferroni_p_values=p_bonf,
        raw_rejected_count=int(np.sum(raw_p < alpha)),
        fdr_bh_rejected_count=int(np.sum(reject_bh)),
        bonferroni_rejected_count=int(np.sum(reject_bonf)),
        alpha=alpha,
    )


def generate_charts(
    df: pd.DataFrame,
    group_ci: GroupDifferenceCI,
    simple_ols: object,
    multitest_res: MultipleTestingSummary,
    output_dir: Path,
    seed: int = 42,
) -> list[Path]:
    """Generate two focused multi-panel PNG figures illustrating statsmodels outputs."""
    output_dir.mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------------
    # Chart 1: Normality Q-Q Plot + Group Mean 95% Confidence Intervals
    # ------------------------------------------------------------------
    fig, axes = plt.subplots(1, 2, figsize=(13, 5), layout="constrained")

    sm.qqplot(
        df["weight_change"],
        line="s",
        ax=axes[0],
        markersize=2.5,
        alpha=0.45,
        color="#4c72b0",
    )
    axes[0].set_title("Q-Q Plot: Weight Change Normality Check")
    axes[0].set_xlabel("Theoretical Normal Quantiles")
    axes[0].set_ylabel("Sample Quantiles (kg)")

    # Right panel: Male vs Female mean + 95% CI via DescrStatsW
    male_dsw = DescrStatsW(df.loc[df["sex"] == 1, "weight_change"].to_numpy())
    female_dsw = DescrStatsW(df.loc[df["sex"] == 2, "weight_change"].to_numpy())
    m_low, m_high = male_dsw.tconfint_mean()
    f_low, f_high = female_dsw.tconfint_mean()

    labels = ["Male (sex=1)", "Female (sex=2)"]
    means = [float(male_dsw.mean), float(female_dsw.mean)]
    yerr = [
        [means[0] - m_low, means[1] - f_low],
        [m_high - means[0], f_high - means[1]],
    ]
    axes[1].errorbar(
        x=labels,
        y=means,
        yerr=yerr,
        fmt="o",
        capsize=8,
        markersize=9,
        linewidth=2.5,
        color="#dd8452",
    )
    axes[1].axhline(0, color="grey", linestyle=":", linewidth=1)
    axes[1].set_xlim(-0.5, 1.5)
    axes[1].set_title(
        f"Group Means & 95% CIs (Diff: {group_ci.mean_diff:.2f} kg, "
        f"95% CI [{group_ci.ci_low:.2f}, {group_ci.ci_high:.2f}])"
    )
    axes[1].set_ylabel("Mean Annual Weight Change (kg)")

    chart1 = output_dir / "01_qqplot_and_mean_ci.png"
    fig.savefig(chart1, dpi=150, bbox_inches="tight")
    plt.close(fig)

    # ------------------------------------------------------------------
    # Chart 2: Simple OLS Regression + Multiple Testing Correction
    # ------------------------------------------------------------------
    fig, axes = plt.subplots(1, 2, figsize=(13, 5), layout="constrained")

    sample_df = df.sample(n=min(1500, len(df)), random_state=seed)
    sns.regplot(
        data=sample_df,
        x="weight2",
        y="weight_change",
        scatter_kws={"alpha": 0.25, "s": 16, "color": "teal"},
        line_kws={"color": "crimson", "linewidth": 2},
        ax=axes[0],
    )
    axes[0].set_title(
        f"Simple OLS: weight_change ~ weight2 "
        f"(R² = {simple_ols.rsquared:.3f}, slope = {simple_ols.params['weight2']:.3f})"
    )
    axes[0].set_xlabel("Current Weight: weight2 (kg)")
    axes[0].set_ylabel("Annual Weight Change (kg)")

    # Right panel: False positives before vs after multiple testing correction
    methods = ["Raw p < 0.05\n(Uncorrected)", "BH FDR\n(fdr_bh)", "Bonferroni\n(bonferroni)"]
    counts = [
        multitest_res.raw_rejected_count,
        multitest_res.fdr_bh_rejected_count,
        multitest_res.bonferroni_rejected_count,
    ]
    colors = ["#c44e52", "#4c72b0", "#55a868"]
    bars = axes[1].bar(methods, counts, color=colors, width=0.5)
    for bar, count in zip(bars, counts):
        axes[1].text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.8,
            f"{count} / {multitest_res.n_iterations}",
            ha="center",
            va="bottom",
            fontweight="bold",
        )
    axes[1].set_ylim(0, max(counts) + 12)
    axes[1].set_title("False Positives Across 1,000 Random Splits")
    axes[1].set_ylabel("Number of Tests Flagged Significant (p < 0.05)")

    chart2 = output_dir / "02_ols_and_multiple_testing.png"
    fig.savefig(chart2, dpi=150, bbox_inches="tight")
    plt.close(fig)

    return [chart1, chart2]
