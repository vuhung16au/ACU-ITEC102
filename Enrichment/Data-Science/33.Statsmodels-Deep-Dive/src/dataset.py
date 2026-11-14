"""Offline synthetic Australian health survey dataset for statsmodels analysis."""

from pathlib import Path
import numpy as np
import pandas as pd

DEFAULT_SEED = 42

AUSTRALIAN_CITIES = [
    ("Sydney", "NSW"),
    ("Melbourne", "VIC"),
    ("Brisbane", "QLD"),
    ("Perth", "WA"),
    ("Adelaide", "SA"),
    ("Canberra", "ACT"),
    ("Hobart", "TAS"),
    ("Darwin", "NT"),
]


def generate_survey_data(
    n_rows: int = 15_000,
    seed: int = DEFAULT_SEED,
    output_path: Path | None = None,
) -> pd.DataFrame:
    """Generate a clean synthetic Australian health survey dataset.

    Columns:
      - participant_id: unique ID (e.g. AU-00001)
      - city, state: Australian city and state/territory
      - sex: 1 = Male, 2 = Female
      - age: age in years (18–75)
      - htm3: height in centimetres
      - wtyrago: weight one year ago (kg)
      - weight2: current weight (kg)
      - weight_change: weight2 - wtyrago (kg; negative means weight loss)
    """
    rng = np.random.default_rng(seed)

    loc_idx = rng.integers(0, len(AUSTRALIAN_CITIES), size=n_rows)
    cities = [AUSTRALIAN_CITIES[i][0] for i in loc_idx]
    states = [AUSTRALIAN_CITIES[i][1] for i in loc_idx]

    # Sex coding: 1 = Male (~40%), 2 = Female (~60%)
    sex = rng.choice([1, 2], size=n_rows, p=[0.40, 0.60])
    age = rng.integers(18, 76, size=n_rows)

    htm3 = np.where(
        sex == 1,
        rng.normal(loc=177.5, scale=7.2, size=n_rows),
        rng.normal(loc=163.8, scale=6.8, size=n_rows),
    )

    # Weight one year ago (wtyrago) correlates with height, sex, and age
    wtyrago = np.clip(
        0.84 * htm3
        - 67.0
        + np.where(sex == 1, 6.2, 0.0)
        + 0.09 * (age - 35)
        + rng.normal(loc=0.0, scale=11.0, size=n_rows),
        42.0,
        185.0,
    )

    # Annual weight change includes a small heavy-tailed component (3% of participants)
    # so a Q-Q plot visibly highlights slight non-normality in the tails.
    base_noise = np.where(
        sex == 1,
        rng.normal(loc=0.0, scale=4.2, size=n_rows),
        rng.normal(loc=0.0, scale=3.7, size=n_rows),
    )
    is_tail = rng.random(n_rows) < 0.03
    tail_noise = rng.normal(loc=0.0, scale=11.5, size=n_rows)
    noise = np.where(is_tail, tail_noise, base_noise)

    weight_change = np.where(sex == 1, -0.85, -0.55) - 0.015 * (age - 40) + noise
    weight2 = np.clip(wtyrago + weight_change, 38.0, 195.0)
    actual_change = weight2 - wtyrago

    df = pd.DataFrame(
        {
            "participant_id": [f"AU-{i:05d}" for i in range(1, n_rows + 1)],
            "city": cities,
            "state": states,
            "sex": sex,
            "sex_label": np.where(sex == 1, "Male", "Female"),
            "age": age,
            "htm3": np.round(htm3, 1),
            "wtyrago": np.round(wtyrago, 2),
            "weight2": np.round(weight2, 2),
            "weight_change": np.round(actual_change, 3),
        }
    )

    if output_path is not None:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(output_path, index=False)

    return df
