# Handling Missing Values Before Exporting

This module covers inspecting, detecting, dropping, and imputing missing data in Pandas, and applying validation assertions to guarantee clean exports.

---

## Learning Objectives
- Detect missing values using `df.isna()` / `df.isnull()` and quantify null counts and percentages.
- Evaluate the trade-offs of dropping rows (`df.dropna()`) vs. imputing missing data (`df.fillna()`).
- Apply statistical imputation (column mean, median) and forward filling (`.ffill()`).
- Validate data hygiene using assertions before writing to disk.
- Export clean datasets reliably with `index=False`.

---

## Folder Structure
- `docs/`: Conceptual documentation on missing value mechanics, imputation strategies, and assertions.
- `notebooks/`:
  - `06-handling-missing-values-before-exporting.ipynb`: Interactive notebook with code and practice exercises.
  - `sample_weather.csv`: 10-day Australian weather dataset with missing observations.
- `src/`:
  - `HandlingMissingValuesBeforeExporting.py`: Runnable Python script illustrating all concepts and solutions.
- `QUICKSTART.md`: Setup and execution instructions.
- `Makefile`: Commands to launch Jupyter (`make run`) and clean up (`make clean`).
