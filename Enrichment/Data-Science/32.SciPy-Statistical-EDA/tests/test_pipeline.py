"""End-to-end and unit tests for the SciPy Statistical EDA project."""

from pathlib import Path
import numpy as np

from main import run_pipeline
from src.data_generator import generate_synthetic_survey
from src.eda_cleaner import inspect_and_clean
from src.stats_analysis import (
    compare_two_groups,
    compute_correlation_analysis,
    run_monte_carlo_random_splits,
    run_single_random_split,
)
from src.visualizer import generate_all_visualisations


def test_data_generation_and_cleaning(tmp_path: Path) -> None:
    """Verify synthetic data includes anomalies and cleaning removes them."""
    raw_csv = tmp_path / "raw.csv"
    clean_csv = tmp_path / "clean.csv"

    df_raw = generate_synthetic_survey(n_rows=2000, seed=42, output_path=raw_csv)
    assert raw_csv.exists()
    assert len(df_raw) == 2000
    assert df_raw.isna().sum().sum() > 0

    df_clean, report = inspect_and_clean(df_raw, output_path=clean_csv)
    assert clean_csv.exists()
    assert report.raw_rows == 2000
    assert report.missing_values_removed > 0
    assert report.invalid_range_removed > 0
    assert report.clean_rows < report.raw_rows
    assert df_clean["htm3"].between(120.0, 230.0).all()
    assert df_clean["weight1"].between(35.0, 250.0).all()
    assert df_clean["weight2"].between(35.0, 250.0).all()
    assert "weight_change" in df_clean.columns
    assert "weight_height_ratio" in df_clean.columns


def test_welch_t_test_and_levene() -> None:
    """Verify Levene's test and Welch's t-test detect group differences."""
    df_raw = generate_synthetic_survey(n_rows=6000, seed=42)
    df_clean, _ = inspect_and_clean(df_raw)

    male_wc = df_clean.loc[df_clean["sex"] == 1, "weight_change"]
    female_wc = df_clean.loc[df_clean["sex"] == 2, "weight_change"]
    wc_cmp = compare_two_groups(male_wc, female_wc, metric_name="weight_change", unit="kg")

    assert wc_cmp.n_a > 0 and wc_cmp.n_b > 0
    assert wc_cmp.levene_pvalue < 0.05
    assert wc_cmp.is_significant
    assert wc_cmp.p_value < 0.05
    assert wc_cmp.mean_a < wc_cmp.mean_b  # Males lose slightly more weight on average


def test_random_splits_behave_as_expected() -> None:
    """Verify single split and 1,000-iteration Monte Carlo false-positive rate."""
    df_raw = generate_synthetic_survey(n_rows=4000, seed=42)
    df_clean, _ = inspect_and_clean(df_raw)
    values = df_clean["weight_change"].to_numpy()

    single = run_single_random_split(values, seed=42)
    assert single.group1_size == single.group2_size
    assert 0.0 <= single.p_value <= 1.0

    mc = run_monte_carlo_random_splits(values, n_iterations=500, seed=42)
    assert len(mc.p_values) == 500
    assert len(mc.negative_log10_p) == 500
    # Under true H0, proportion below alpha=0.05 should be close to 0.05
    assert 0.01 <= mc.proportion_below_alpha <= 0.10
    assert np.isfinite(mc.negative_log10_p).all()


def test_correlation_matrix_and_visualisations(tmp_path: Path) -> None:
    """Verify Pearson/Spearman correlation matrices and Seaborn PNG generation."""
    df_raw = generate_synthetic_survey(n_rows=3000, seed=42)
    df_clean, _ = inspect_and_clean(df_raw)

    male_wc = df_clean.loc[df_clean["sex"] == 1, "weight_change"]
    female_wc = df_clean.loc[df_clean["sex"] == 2, "weight_change"]
    wc_cmp = compare_two_groups(male_wc, female_wc, "weight_change", "kg")

    male_ratio = df_clean.loc[df_clean["sex"] == 1, "weight_height_ratio"]
    female_ratio = df_clean.loc[df_clean["sex"] == 2, "weight_height_ratio"]
    ratio_cmp = compare_two_groups(male_ratio, female_ratio, "weight_height_ratio", "kg/cm")

    mc = run_monte_carlo_random_splits(df_clean["weight_change"].to_numpy(), n_iterations=200, seed=42)
    corr = compute_correlation_analysis(df_clean)

    # Diagonal should be 1.0 and matrix should be symmetric
    assert np.allclose(np.diag(corr.pearson_r), 1.0)
    assert np.allclose(corr.pearson_r.to_numpy(), corr.pearson_r.to_numpy().T)
    assert corr.pearson_r.loc["weekly_exercise_hrs", "daily_steps"] > 0.7
    assert corr.pearson_r.loc["weekly_exercise_hrs", "weight_change"] < 0.0

    plot_paths = generate_all_visualisations(
        df_clean=df_clean,
        weight_change_cmp=wc_cmp,
        mc_result=mc,
        ratio_cmp=ratio_cmp,
        corr_result=corr,
        output_dir=tmp_path,
    )
    assert len(plot_paths) == 4
    for path in plot_paths:
        assert path.exists()
        assert path.stat().st_size > 10_000


def test_end_to_end_pipeline(tmp_path: Path, monkeypatch) -> None:
    """Run the full pipeline end-to-end into temporary directories."""
    import main

    monkeypatch.setattr(main, "DATA_DIR", tmp_path / "data")
    monkeypatch.setattr(main, "IMAGES_DIR", tmp_path / "images")
    main.run_pipeline(n_rows=3000, seed=42)

    assert (tmp_path / "data" / "aus_health_survey_raw.csv").exists()
    assert (tmp_path / "data" / "aus_health_survey_clean.csv").exists()
    assert len(list((tmp_path / "images").glob("*.png"))) == 4
