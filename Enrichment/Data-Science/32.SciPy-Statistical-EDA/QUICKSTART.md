# Quickstart Guide

Follow these steps to set up, run, and test **32. SciPy Statistical EDA** on your machine.

---

## 1. Prerequisites

- **Python 3.14+**
- **[uv](https://docs.astral.sh/uv/)** (fast Python package and virtual environment manager)

Verify both tools are installed:

```bash
python3 --version
uv --version
```

---

## 2. Navigate to the Project Folder

```bash
cd Enrichment/Data-Science/32.SciPy-Statistical-EDA
```

---

## 3. Install Dependencies

Using `make` (recommended):

```bash
make setup
```

Or directly with `uv`:

```bash
uv sync
```

This creates a local `.venv` and installs `scipy`, `seaborn`, `pandas`, `numpy`, `matplotlib`, and `pytest`.

---

## 4. Run the Full EDA & SciPy Pipeline

```bash
make run
```

*(Equivalent to `uv run python main.py`.)*

### What happens when you run it?
1. Generates synthetic Australian survey data into `data/aus_health_survey_raw.csv`.
2. Cleans missing/invalid records and saves `data/aus_health_survey_clean.csv`.
3. Prints step-by-step descriptive statistics, Levene's test, Welch's t-test, single & 1,000-iteration random splits, unit comparison, and Pearson/Spearman correlation matrices directly to your terminal—each accompanied by a plain-English interpretation.
4. Saves four Seaborn charts into `images/`:
   - `images/01_weight_change_by_sex.png`
   - `images/02_random_splits_neg_log10_p.png`
   - `images/03_weight_height_ratio_by_sex.png`
   - `images/04_correlation_matrix_heatmap.png`

---

## 5. Run the Automated Tests

To verify data generation, cleaning, SciPy statistical calculations, correlation symmetry, and chart creation:

```bash
make test
```

*(Equivalent to `PYTHONPATH=. uv run pytest tests/ -v`.)*

---

## 6. Clean Up Environment Files (Optional)

To remove `.venv`, `__pycache__`, and `.pytest_cache`:

```bash
make clean
```

> **Note:** This project runs purely in Python and generates local CSV/PNG files offline—no Docker containers or external databases are required.
