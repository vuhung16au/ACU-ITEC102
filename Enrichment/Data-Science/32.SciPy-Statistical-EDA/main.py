"""End-to-end Exploratory Data Analysis (EDA) & SciPy Statistical Testing Demo.

Run this script to execute the full pipeline:
  1. Generate synthetic Australian health & wellness survey data
  2. Inspect and clean missing values / sentinel outliers
  3. Compute descriptive statistics by group
  4. Apply Levene's test and Welch's independent t-test (t-value & p-value)
  5. Test a single random 50/50 split and 1,000 Monte Carlo random splits
  6. Compare metrics with different units (weight_change vs weight_height_ratio)
  7. Compute Pearson & Spearman correlation matrices with SciPy p-values
  8. Save Seaborn visualisations and print plain-English interpretations
"""

from pathlib import Path
from src.data_generator import DEFAULT_SEED, generate_synthetic_survey
from src.eda_cleaner import inspect_and_clean
from src.stats_analysis import (
    compare_two_groups,
    compute_correlation_analysis,
    format_group_interpretation,
    run_monte_carlo_random_splits,
    run_single_random_split,
)
from src.visualizer import generate_all_visualisations

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
IMAGES_DIR = BASE_DIR / "images"


def print_section(title: str) -> None:
    """Print a clear section banner for terminal readability."""
    print(f"\n{'=' * 72}")
    print(f"  {title}")
    print(f"{'=' * 72}")


def _display_path(path: Path) -> str:
    """Format a path relative to BASE_DIR when inside the project, else full path."""
    return str(path.relative_to(BASE_DIR)) if path.is_relative_to(BASE_DIR) else str(path)


def run_pipeline(n_rows: int = 12_000, seed: int = DEFAULT_SEED) -> None:
    """Execute the full EDA and SciPy statistical workflow."""
    # ------------------------------------------------------------------
    # 1. Generate Synthetic Australian Survey Data
    # ------------------------------------------------------------------
    print_section("1. SYNTHETIC DATA GENERATION (AUSTRALIAN WELLNESS SURVEY)")
    raw_path = DATA_DIR / "aus_health_survey_raw.csv"
    df_raw = generate_synthetic_survey(n_rows=n_rows, seed=seed, output_path=raw_path)
    print(f"Generated {len(df_raw):,} raw records -> {_display_path(raw_path)}")
    print(df_raw.head(5).to_string(index=False))

    # ------------------------------------------------------------------
    # 2. Exploratory Data Analysis (EDA) & Data Cleaning
    # ------------------------------------------------------------------
    print_section("2. EDA INSPECTION & DATA CLEANING")
    clean_path = DATA_DIR / "aus_health_survey_clean.csv"
    df_clean, report = inspect_and_clean(df_raw, output_path=clean_path)

    print(f"Raw row count:              {report.raw_rows:,}")
    print(f"Missing values detected:    {report.missing_counts_by_column}")
    print(f"Rows dropped (missing):     {report.missing_values_removed:,}")
    print(f"Rows dropped (out-of-range):{report.invalid_range_removed:,}")
    print(f"Clean row count:            {report.clean_rows:,} -> {_display_path(clean_path)}")

    print("\nSummary statistics of key cleaned numeric variables:")
    summary_cols = ["age", "htm3", "weight1", "weight2", "weight_change", "weight_height_ratio"]
    print(df_clean[summary_cols].describe().round(3).to_string())

    # ------------------------------------------------------------------
    # 3. Hypothesis Testing: Weight Change by Sex (Levene + Welch t-test)
    # ------------------------------------------------------------------
    print_section("3. HYPOTHESIS TESTING: MALE vs FEMALE WEIGHT CHANGE")
    male_wc = df_clean.loc[df_clean["sex"] == 1, "weight_change"]
    female_wc = df_clean.loc[df_clean["sex"] == 2, "weight_change"]

    wc_comparison = compare_two_groups(
        group_a=male_wc,
        group_b=female_wc,
        metric_name="weight_change",
        unit="kg",
    )
    print(format_group_interpretation(wc_comparison))

    # ------------------------------------------------------------------
    # 4. Single Random 50/50 Split Sanity Check
    # ------------------------------------------------------------------
    print_section("4. RANDOM SPLIT SANITY CHECK (SINGLE 50/50 SPLIT)")
    weight_values = df_clean["weight_change"].to_numpy()
    single_split = run_single_random_split(weight_values, seed=seed)

    print(f"Group 1 size: {single_split.group1_size:,} | Mean: {single_split.group1_mean:.4f} kg")
    print(f"Group 2 size: {single_split.group2_size:,} | Mean: {single_split.group2_mean:.4f} kg")
    print(f"Welch's t-statistic: {single_split.t_stat:.4f}")
    print(f"P-value:             {single_split.p_value:.4f}")
    print("\nInterpretation:")
    if single_split.is_significant:
        print(
            "  By rare random chance (5% probability), this split gave p < 0.05 even though "
            "both halves come from the same population (a false positive / Type I error)."
        )
    else:
        print(
            "  Since p >= 0.05, the result is NOT statistically significant and we do not "
            "reject H0. This is expected because both halves were drawn randomly from the "
            "same cleaned dataset."
        )

    # ------------------------------------------------------------------
    # 5. Monte Carlo Experiment: 1,000 Random Splits
    # ------------------------------------------------------------------
    print_section("5. MONTE CARLO EXPERIMENT: 1,000 RANDOM SPLITS")
    mc_result = run_monte_carlo_random_splits(weight_values, n_iterations=1000, seed=seed)

    print(f"Number of random split tests: {mc_result.n_iterations:,}")
    print(
        f"Proportion with p < 0.05:     {mc_result.proportion_below_alpha:.3f} "
        f"({mc_result.proportion_below_alpha * 100:.1f}%)"
    )
    print(f"Smallest p-value observed:    {mc_result.smallest_p_value:.5f}")
    print("\nDiscussion:")
    print(
        "  When the null hypothesis is true (random splits of the same dataset), roughly 5%\n"
        "  of tests still produce p < 0.05 purely by chance. This demonstrates why alpha = 0.05\n"
        "  represents our accepted Type I error (false-positive) rate."
    )

    # ------------------------------------------------------------------
    # 6. Comparing Metrics with Different Units (Weight-to-Height Ratio)
    # ------------------------------------------------------------------
    print_section("6. UNIT SCALE COMPARISON: WEIGHT-TO-HEIGHT RATIO (kg/cm)")
    male_ratio = df_clean.loc[df_clean["sex"] == 1, "weight_height_ratio"]
    female_ratio = df_clean.loc[df_clean["sex"] == 2, "weight_height_ratio"]

    ratio_comparison = compare_two_groups(
        group_a=male_ratio,
        group_b=female_ratio,
        metric_name="weight_height_ratio",
        unit="kg/cm",
    )
    print(format_group_interpretation(ratio_comparison))

    print("\nDiscussion (Comparing Different Units):")
    print(
        f"  - Weight change difference:       {abs(wc_comparison.mean_diff):.4f} kg "
        f"(t = {wc_comparison.t_stat:.2f}, p = {wc_comparison.p_value:.2e})\n"
        f"  - Weight-height ratio difference: {abs(ratio_comparison.mean_diff):.4f} kg/cm "
        f"(t = {ratio_comparison.t_stat:.2f}, p = {ratio_comparison.p_value:.2e})\n"
        "  Because kg and kg/cm use different units, their raw mean differences should NOT be\n"
        "  compared directly. Instead, dimensionless t-statistics and p-values let us evaluate\n"
        "  evidence against H0 consistently—while remembering that large sample sizes can make\n"
        "  even modest practical differences highly statistically significant."
    )

    # ------------------------------------------------------------------
    # 7. Correlation Matrix & SciPy Significance Testing
    # ------------------------------------------------------------------
    print_section("7. CORRELATION MATRIX & SCIPY P-VALUES")
    corr_result = compute_correlation_analysis(df_clean)

    print("Pearson correlation matrix (r):")
    print(corr_result.pearson_r.round(3).to_string())

    print("\nTop 6 strongest correlations (Pearson r and Spearman rho with p-values):")
    for pair in corr_result.notable_pairs[:6]:
        print(
            f"  - {pair['var_1']:<20} vs {pair['var_2']:<20} | "
            f"r = {pair['pearson_r']:+.3f} (p = {pair['pearson_p']:.2e}) | "
            f"rho = {pair['spearman_r']:+.3f} (p = {pair['spearman_p']:.2e})"
        )

    print("\nInterpretation:")
    print(
        "  - weight1 vs weight2 shows a very strong positive correlation (participants who\n"
        "    started heavier generally remained heavier after 12 weeks).\n"
        "  - weekly_exercise_hrs vs daily_steps shows a strong positive correlation.\n"
        "  - weekly_exercise_hrs vs weight_change shows a negative correlation (more exercise\n"
        "    is associated with greater weight loss, i.e. more negative weight_change)."
    )

    # ------------------------------------------------------------------
    # 8. Seaborn Visualisations
    # ------------------------------------------------------------------
    print_section("8. GENERATING SEABORN VISUALISATIONS")
    plot_paths = generate_all_visualisations(
        df_clean=df_clean,
        weight_change_cmp=wc_comparison,
        mc_result=mc_result,
        ratio_cmp=ratio_comparison,
        corr_result=corr_result,
        output_dir=IMAGES_DIR,
    )
    for path in plot_paths:
        print(f"Saved chart -> {_display_path(path)}")

    print("\nPipeline complete!")


if __name__ == "__main__":
    run_pipeline()
