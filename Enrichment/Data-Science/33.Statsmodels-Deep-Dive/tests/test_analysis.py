"""Focused unit and end-to-end tests for the statsmodels enrichment project."""

from pathlib import Path
import numpy as np

from src.analysis import (
    compare_groups_with_ci,
    compute_mean_confidence_intervals,
    fit_ols_models,
    generate_charts,
    random_splits_with_multitest,
)
from src.dataset import generate_survey_data


def test_descrstatsw_confidence_intervals() -> None:
    """Verify DescrStatsW computes valid 95% confidence intervals bracketing the mean."""
    df = generate_survey_data(n_rows=3000, seed=42)
    ci_df = compute_mean_confidence_intervals(df)

    assert len(ci_df) == 4
    for _, row in ci_df.iterrows():
        assert row["ci_95_low"] < row["mean"] < row["ci_95_high"]


def test_ols_collinearity_and_compare_means() -> None:
    """Verify multiple OLS shows structural collinearity and CompareMeans matches SciPy."""
    df = generate_survey_data(n_rows=4000, seed=42)
    simple_ols, multiple_ols = fit_ols_models(df)

    assert simple_ols.rsquared < 0.25
    assert multiple_ols.rsquared > 0.999
    assert np.isclose(multiple_ols.params["weight2"], 1.0, atol=0.05)
    assert np.isclose(multiple_ols.params["wtyrago"], -1.0, atol=0.05)

    grp_ci = compare_groups_with_ci(df)
    assert np.isclose(grp_ci.scipy_t, grp_ci.sm_t, atol=1e-6)
    assert np.isclose(grp_ci.scipy_p, grp_ci.sm_p, atol=1e-6)
    assert grp_ci.ci_low < grp_ci.mean_diff < grp_ci.ci_high


def test_multiple_testing_eliminates_random_false_positives(tmp_path: Path) -> None:
    """Verify BH FDR and Bonferroni remove false positives in random splits."""
    df = generate_survey_data(n_rows=3000, seed=42)
    mt = random_splits_with_multitest(df["weight_change"].to_numpy(), n_iterations=300, seed=42)

    assert mt.raw_rejected_count > 0
    assert mt.fdr_bh_rejected_count <= mt.raw_rejected_count
    assert mt.bonferroni_rejected_count == 0

    simple_ols, _ = fit_ols_models(df)
    grp_ci = compare_groups_with_ci(df)
    charts = generate_charts(df, grp_ci, simple_ols, mt, tmp_path)
    assert len(charts) == 2
    assert all(p.exists() and p.stat().st_size > 10_000 for p in charts)


def test_end_to_end_demo(tmp_path: Path, monkeypatch) -> None:
    """Run main.run_demo end-to-end into temporary folders."""
    import main

    monkeypatch.setattr(main, "DATA_DIR", tmp_path / "data")
    monkeypatch.setattr(main, "IMAGES_DIR", tmp_path / "images")
    main.run_demo(n_rows=2000, seed=42)

    assert (tmp_path / "data" / "aus_wellness_survey.csv").exists()
    assert len(list((tmp_path / "images").glob("*.png"))) == 2
