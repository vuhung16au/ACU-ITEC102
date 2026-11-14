"""Synthetic Australian health survey data generator.

Generates an offline, Australian-themed wellness survey dataset with
realistic anthropometric measurements, exercise habits, and intentional
data-quality anomalies (missing values and sentinel outliers) so students
can practise a complete Exploratory Data Analysis (EDA) pipeline.
"""

from pathlib import Path
import numpy as np
import pandas as pd

# Fixed seed ensures every student sees the exact same reproducible dataset.
DEFAULT_SEED = 42

# Australian cities and their corresponding states/territories.
AUSTRALIAN_LOCATIONS = [
    ("Sydney", "NSW"),
    ("Melbourne", "VIC"),
    ("Brisbane", "QLD"),
    ("Perth", "WA"),
    ("Adelaide", "SA"),
    ("Canberra", "ACT"),
    ("Hobart", "TAS"),
    ("Darwin", "NT"),
]

# Population weights roughly reflecting major Australian urban centres.
LOCATION_PROBS = [0.26, 0.25, 0.14, 0.11, 0.08, 0.06, 0.05, 0.05]

FIRST_NAMES = [
    "Liam", "Olivia", "Noah", "Charlotte", "Oliver", "Amelia", "Jack", "Isla",
    "Lucas", "Mia", "Ethan", "Chloe", "Lachlan", "Grace", "Minh", "Linh",
    "An", "Tuan", "Priya", "Aarav",
]

LAST_NAMES = [
    "Nguyen", "Vu", "Tran", "Smith", "Jones", "Williams", "O'Connor",
    "Patel", "Chen", "Brown", "Taylor", "Wilson", "Pham", "Le",
]


def generate_synthetic_survey(
    n_rows: int = 12_000,
    seed: int = DEFAULT_SEED,
    output_path: Path | None = None,
) -> pd.DataFrame:
    """Create a synthetic Australian health and weight-change dataset.

    In this dataset (matching standard survey coding):
      - sex == 1 represents Male participants
      - sex == 2 represents Female participants
      - htm3 represents height in centimetres
      - weight1 represents baseline weight in kilograms
      - weight2 represents follow-up weight in kilograms after 12 weeks

    Args:
        n_rows: Number of participant records to generate.
        seed: Random seed for reproducibility.
        output_path: Optional CSV path to save the raw dataset.

    Returns:
        A pandas DataFrame containing the raw synthetic survey records.
    """
    rng = np.random.default_rng(seed)

    participant_ids = [f"AU-{idx:05d}" for idx in range(1, n_rows + 1)]
    first_choices = rng.choice(FIRST_NAMES, size=n_rows)
    last_choices = rng.choice(LAST_NAMES, size=n_rows)
    full_names = [f"{first} {last}" for first, last in zip(first_choices, last_choices)]

    loc_indices = rng.choice(len(AUSTRALIAN_LOCATIONS), size=n_rows, p=LOCATION_PROBS)
    cities = [AUSTRALIAN_LOCATIONS[i][0] for i in loc_indices]
    states = [AUSTRALIAN_LOCATIONS[i][1] for i in loc_indices]

    # Sex coding: 1 = Male (~39%), 2 = Female (~61%)
    sex = rng.choice([1, 2], size=n_rows, p=[0.39, 0.61])
    age = rng.integers(18, 76, size=n_rows)

    # Height in centimetres (htm3): realistic sex-specific distributions
    htm3 = np.where(
        sex == 1,
        rng.normal(loc=177.5, scale=7.2, size=n_rows),
        rng.normal(loc=163.8, scale=6.8, size=n_rows),
    )

    # Weekly exercise hours and correlated daily step counts
    weekly_exercise_hrs = np.clip(rng.normal(loc=4.0, scale=2.4, size=n_rows), 0.0, 14.0)
    daily_steps = np.clip(
        2800 + 850 * weekly_exercise_hrs + rng.normal(loc=0.0, scale=1100.0, size=n_rows),
        1000,
        22000,
    ).round(0)

    # Baseline weight (weight1) increases with height and varies slightly by sex/exercise
    weight1 = (
        0.85 * htm3
        - 68.0
        + np.where(sex == 1, 6.0, 0.0)
        + 0.08 * (age - 35)
        - 0.55 * weekly_exercise_hrs
        + rng.normal(loc=0.0, scale=10.5, size=n_rows)
    )
    weight1 = np.clip(weight1, 42.0, 185.0)

    # 12-week weight change (kg): negative means weight loss.
    # Males have a slightly greater mean weight loss AND a larger standard deviation,
    # so Levene's test will detect unequal variances and favour Welch's t-test.
    # Subtracting 4.0 centres the exercise effect so group means stay near -0.95 / -0.65 kg
    # while producing a clearly visible negative correlation with exercise hours.
    true_weight_change = np.where(
        sex == 1,
        -0.95 - 0.35 * (weekly_exercise_hrs - 4.0) + rng.normal(loc=0.0, scale=4.4, size=n_rows),
        -0.65 - 0.35 * (weekly_exercise_hrs - 4.0) + rng.normal(loc=0.0, scale=3.9, size=n_rows),
    )
    weight2 = weight1 + true_weight_change

    df = pd.DataFrame(
        {
            "participant_id": participant_ids,
            "full_name": full_names,
            "city": cities,
            "state": states,
            "sex": sex,
            "age": age,
            "htm3": np.round(htm3, 1),
            "weight1": np.round(weight1, 2),
            "weight2": np.round(weight2, 2),
            "weekly_exercise_hrs": np.round(weekly_exercise_hrs, 2),
            "daily_steps": daily_steps.astype(int),
        }
    )

    # Inject realistic data-quality problems (~2.5% of rows) for the EDA cleaning stage
    missing_weight2_idx = rng.choice(n_rows, size=int(n_rows * 0.012), replace=False)
    df.loc[missing_weight2_idx, "weight2"] = np.nan

    missing_height_idx = rng.choice(n_rows, size=int(n_rows * 0.005), replace=False)
    df.loc[missing_height_idx, "htm3"] = np.nan

    sentinel_height_idx = rng.choice(n_rows, size=int(n_rows * 0.004), replace=False)
    df.loc[sentinel_height_idx[: len(sentinel_height_idx) // 2], "htm3"] = 999.0
    df.loc[sentinel_height_idx[len(sentinel_height_idx) // 2 :], "htm3"] = -10.0

    outlier_weight_idx = rng.choice(n_rows, size=int(n_rows * 0.004), replace=False)
    df.loc[outlier_weight_idx[: len(outlier_weight_idx) // 2], "weight1"] = 550.0
    df.loc[outlier_weight_idx[len(outlier_weight_idx) // 2 :], "weight1"] = 12.0

    if output_path is not None:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(output_path, index=False)

    return df
