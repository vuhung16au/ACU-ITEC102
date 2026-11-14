"""Short and sharp statsmodels enrichment walkthrough.

Demonstrates how statsmodels complements Pandas and SciPy across four stages:
  1. Richer Summary Stats & Normality Diagnostics (DescrStatsW + qqplot)
  2. Explaining Correlations via OLS Regression (simple & multiple OLS)
  3. Group-Difference Confidence Intervals (CompareMeans vs scipy.stats.ttest_ind)
  4. Multiple-Testing Correction Across 1,000 Random Splits (multipletests)
"""

from pathlib import Path
from src.analysis import (
    compare_groups_with_ci,
    compute_mean_confidence_intervals,
    fit_ols_models,
    generate_charts,
    random_splits_with_multitest,
)
from src.dataset import DEFAULT_SEED, generate_survey_data

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
IMAGES_DIR = BASE_DIR / "images"


def _banner(title: str) -> None:
    print(f"\n{'=' * 70}\n  {title}\n{'=' * 70}")


def _display_path(path: Path) -> str:
    return str(path.relative_to(BASE_DIR)) if path.is_relative_to(BASE_DIR) else str(path)


def run_demo(n_rows: int = 15_000, seed: int = DEFAULT_SEED) -> None:
    """Execute the four-part statsmodels demonstration."""
    raw_path = DATA_DIR / "aus_wellness_survey.csv"
    df = generate_survey_data(n_rows=n_rows, seed=seed, output_path=raw_path)

    # 1. Summary Stats + 95% CIs + Q-Q Normality Diagnostic
    _banner("1. RICHER SUMMARY STATS (DescrStatsW) & NORMALITY CHECK")
    ci_df = compute_mean_confidence_intervals(df)
    print(ci_df.to_string(index=False, float_format=lambda x: f"{x:.4f}"))
    print(
        "\nTakeaway: DescrStatsW adds 95% confidence intervals around each mean, "
        "while sm.qqplot (Chart 1) reveals heavy tails in weight_change."
    )

    # 2. Explaining Correlations via OLS Regression
    _banner("2. EXPLAINING CORRELATIONS VIA OLS REGRESSION")
    simple_ols, multiple_ols = fit_ols_models(df)
    print(
        f"Simple OLS   (weight_change ~ weight2):               "
        f"R² = {simple_ols.rsquared:.4f} | slope(weight2) = {simple_ols.params['weight2']:+.4f} "
        f"(p = {simple_ols.pvalues['weight2']:.2e})"
    )
    print(
        f"Multiple OLS (weight_change ~ weight2 + wtyrago + age): "
        f"R² = {multiple_ols.rsquared:.4f} | "
        f"weight2 = {multiple_ols.params['weight2']:+.4f}, "
        f"wtyrago = {multiple_ols.params['wtyrago']:+.4f}, "
        f"age = {multiple_ols.params['age']:+.4f}"
    )
    print(
        "\nTakeaway: Because weight_change = weight2 - wtyrago, including both "
        "components creates structural collinearity (R² = 1.000), unlike age."
    )

    # 3. SciPy ttest_ind + statsmodels CompareMeans Confidence Interval
    _banner("3. GROUP DIFFERENCE CONFIDENCE INTERVALS (CompareMeans)")
    grp_ci = compare_groups_with_ci(df, metric="weight_change")
    print(f"Male mean: {grp_ci.male_mean:.4f} kg | Female mean: {grp_ci.female_mean:.4f} kg")
    print(f"SciPy Welch ttest_ind:      t = {grp_ci.scipy_t:.4f}, p = {grp_ci.scipy_p:.3e}")
    print(
        f"statsmodels CompareMeans:   t = {grp_ci.sm_t:.4f}, p = {grp_ci.sm_p:.3e}, "
        f"df = {grp_ci.dof:.1f}"
    )
    print(
        f"95% CI for mean difference: {grp_ci.mean_diff:.4f} kg "
        f"[{grp_ci.ci_low:.4f}, {grp_ci.ci_high:.4f}]"
    )
    print(
        "\nTakeaway: With large N, even a small ~0.3 kg difference gives a tiny p-value. "
        "Reporting the 95% CI clarifies practical vs statistical significance."
    )

    # 4. Multiple-Testing Correction Across 1,000 Random Splits
    _banner("4. MULTIPLE-TESTING CORRECTION (1,000 RANDOM SPLITS)")
    mt_res = random_splits_with_multitest(df["weight_change"].to_numpy(), n_iterations=1000, seed=seed)
    print(f"Uncorrected (raw p < 0.05):  {mt_res.raw_rejected_count:,} / {mt_res.n_iterations:,}")
    print(f"Benjamini-Hochberg (fdr_bh): {mt_res.fdr_bh_rejected_count:,} / {mt_res.n_iterations:,}")
    print(f"Bonferroni (bonferroni):     {mt_res.bonferroni_rejected_count:,} / {mt_res.n_iterations:,}")
    print(
        "\nTakeaway: Random 50/50 splits produce ~5% false positives by chance; "
        "multipletests() controls Type I error across repeated tests."
    )

    # 5. Save Diagnostics & Visualisations
    _banner("5. SAVING DIAGNOSTIC CHARTS")
    for chart in generate_charts(df, grp_ci, simple_ols, mt_res, IMAGES_DIR, seed=seed):
        print(f"Saved -> {_display_path(chart)}")
    print(f"Saved -> {_display_path(raw_path)}")


if __name__ == "__main__":
    run_demo()
