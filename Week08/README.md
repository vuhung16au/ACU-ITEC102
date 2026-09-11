# Week 08: Data Cleaning and Preprocessing with Pandas

Welcome to **Week 08** of **ITEC102**. In real-world data science, raw data is rarely ready for immediate analysis. It often contains missing entries, duplicates, erroneous values, continuous variables that need categorization, and massive volumes that need sensible sampling.

This week focuses on foundational **data cleaning and preprocessing** techniques using Pandas.

---

## Weekly Learning Objectives

By the end of this week, students will be able to:
1. **Audit Data Hygiene**: Inspect data health, detect and remove duplicate entries, fix inconsistent types, and identify outlier records.
2. **Handle Missing Data**: Locate `NaN` and `None` entries, evaluate dropping strategies (`how='any'`, `how='all'`, `subset`), and measure data loss.
3. **Apply Statistical Imputation**: Replace missing values using mean, median, mode, and cohort/group-specific estimates.
4. **Discretize Continuous Data (Binning)**: Segment numerical ranges into discrete categories using `pd.cut()` (custom boundaries) and `pd.qcut()` (equal-frequency quantiles).
5. **Sample Datasets Reliably**: Draw random, reproducible samples using `df.sample()`, set random seeds (`random_state`), and perform stratified sampling.

---

## Topic Structure

| # | Topic Folder | Focus Area | Key Functions | Sample Dataset |
|---|---|---|---|---|
| **01** | [`01.Introduction-to-Data-Cleaning`](./01.Introduction-to-Data-Cleaning/) | Auditing dataset health, types, duplicates, and outliers | `df.isna()`, `df.duplicated()`, `df.drop_duplicates()` | `messy_student_data.csv` |
| **02** | [`02.Handling-Missing-Data`](./02.Handling-Missing-Data/) | Detecting and dropping null observations | `df.isna()`, `df.dropna(how='any')`, `subset=[...]` | `messy_student_data.csv` |
| **03** | [`03.Statistical-Filling`](./03.Statistical-Filling/) | Imputing missing data with central tendency & grouped metrics | `df.fillna()`, `mean()`, `median()`, `transform()` | `messy_student_data.csv` |
| **04** | [`04.Binning`](./04.Binning/) | Segmenting continuous values into categorical grades/brackets | `pd.cut()`, `pd.qcut()`, `value_counts()` | `messy_student_data.csv` |
| **05** | [`05.Sampling`](./05.Sampling/) | Random row sampling, reproducibility, and stratified draws | `df.sample()`, `random_state`, `groupby().sample()` | `messy_student_data.csv` |

---

## Folder Organization

Each topic folder follows a standard modular layout:
```text
Topic-Folder/
├── docs/             # Conceptual guides detailing theoretical foundations
├── notebooks/        # Interactive Jupyter notebook (.ipynb) and sample data
├── src/              # Standalone, runnable Python script (.py)
├── Makefile          # Commands to run jupyter and clean caches
├── pyproject.toml    # Dependencies managed with uv
├── QUICKSTART.md     # Step-by-step setup and execution guide
└── README.md         # Topic overview and learning outcomes
```

---

## Getting Started

Refer to [QUICKSTART.md](./QUICKSTART.md) for full instructions on running the notebooks and scripts using `uv` and `make`.
