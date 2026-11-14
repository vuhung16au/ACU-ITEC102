"""Exploratory Data Analysis (EDA) inspection and data-cleaning pipeline."""

from dataclasses import dataclass
from pathlib import Path
import pandas as pd


@dataclass
class CleaningReport:
    """Summary of rows inspected and removed during the EDA cleaning stage."""

    raw_rows: int
    missing_values_removed: int
    invalid_range_removed: int
    clean_rows: int
    missing_counts_by_column: dict[str, int]


def inspect_and_clean(
    df_raw: pd.DataFrame,
    output_path: Path | None = None,
) -> tuple[pd.DataFrame, CleaningReport]:
    """Inspect raw survey data, remove invalid records, and engineer features.

    Cleaning rules applied:
      1. Drop rows with missing values in essential numeric measurements
         (``htm3``, ``weight1``, ``weight2``, ``sex``).
      2. Remove physically implausible sentinel/outlier values:
         - Height (``htm3``) outside [120, 230] cm
         - Baseline or follow-up weight outside [35, 250] kg
      3. Engineer analysis columns:
         - ``sex_label``: readable label ("Male" for 1, "Female" for 2)
         - ``weight_change``: ``weight2 - weight1`` (kg; negative = weight loss)
         - ``weight_height_ratio``: ``weight2 / htm3`` (kg/cm)

    Args:
        df_raw: Raw synthetic or loaded survey DataFrame.
        output_path: Optional CSV path to persist the cleaned dataset.

    Returns:
        A tuple of ``(df_clean, cleaning_report)``.
    """
    raw_rows = len(df_raw)
    missing_counts = {col: int(cnt) for col, cnt in df_raw.isna().sum().items() if cnt > 0}

    # Step 1: Drop rows missing essential measurements
    essential_cols = ["sex", "htm3", "weight1", "weight2"]
    df_non_null = df_raw.dropna(subset=essential_cols).copy()
    missing_removed = raw_rows - len(df_non_null)

    # Step 2: Filter out sentinel values (e.g., 999, -10) and impossible weights
    valid_mask = (
        df_non_null["sex"].isin([1, 2])
        & df_non_null["htm3"].between(120.0, 230.0)
        & df_non_null["weight1"].between(35.0, 250.0)
        & df_non_null["weight2"].between(35.0, 250.0)
    )
    df_clean = df_non_null.loc[valid_mask].copy()
    invalid_range_removed = len(df_non_null) - len(df_clean)

    # Step 3: Feature engineering for statistical testing
    df_clean["sex_label"] = df_clean["sex"].map({1: "Male", 2: "Female"})
    df_clean["weight_change"] = (df_clean["weight2"] - df_clean["weight1"]).round(3)
    df_clean["weight_height_ratio"] = (df_clean["weight2"] / df_clean["htm3"]).round(5)

    # Reset index cleanly after filtering
    df_clean = df_clean.reset_index(drop=True)

    if output_path is not None:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        df_clean.to_csv(output_path, index=False)

    report = CleaningReport(
        raw_rows=raw_rows,
        missing_values_removed=missing_removed,
        invalid_range_removed=invalid_range_removed,
        clean_rows=len(df_clean),
        missing_counts_by_column=missing_counts,
    )
    return df_clean, report
