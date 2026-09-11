# Real-World Data Wrangling: Building an End-to-End Pipeline

This module teaches students how to transition from clean textbook datasets to messy, real-world data pipelines. Students learn to handle whitespace defects, inconsistent casing, currency formatting, mixed date representations, missing values, and auxiliary lookup joins.

---

## Learning Objectives
- Identify and audit common data quality defects in raw real-world tabular data.
- Sanitise text columns using vectorized string operations (`.str.strip()`, `.str.title()`, `.str.lower()`).
- Parse inconsistent mixed date formats using `pd.to_datetime(..., format='mixed')`.
- Clean financial and currency strings into numerical floats using regular expressions.
- Impute missing values with context-appropriate fallbacks (`.fillna()`).
- Merge auxiliary reference data (`pd.merge(..., how='left')`) and perform feature engineering.

---

## Folder Structure
- `docs/`: Conceptual documentation on data wrangling stages and error prevention.
- `notebooks/`:
  - `01_01.Real-World-Data-Wrangling.ipynb`: Interactive Jupyter notebook with live cleaning pipeline and practice exercises.
- `src/`:
  - `RealWorldDataWrangling.py`: Complete executable Python pipeline script.
- `QUICKSTART.md`: Step-by-step instructions to run scripts and launch notebooks.
- `Makefile`: Convenience targets (`make run`, `make test`, `make clean`).
