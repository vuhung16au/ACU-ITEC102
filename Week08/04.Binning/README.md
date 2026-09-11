# Data Binning (Discretisation)

This module covers converting continuous numerical variables into discrete, categorical intervals using `pd.cut()` and `pd.qcut()`.

---

## Learning Objectives
- Understand the role of discretisation and binning in data preprocessing.
- Construct custom, non-uniform intervals using `pd.cut()` (e.g. Australian academic grades).
- Generate automatic equal-width bins using `pd.cut(..., bins=k)`.
- Create balanced, equal-frequency quantile bins using `pd.qcut()`.
- Evaluate categorical distributions using `.value_counts()` and `pd.crosstab()`.

---

## Folder Structure
- `docs/`: Conceptual documentation on binning mechanics, intervals, and quantile binning.
- `notebooks/`:
  - `04-binning.ipynb`: Interactive notebook with code and practice exercises.
  - `messy_student_data.csv`: Sample student performance dataset.
- `src/`:
  - `Binning.py`: Runnable Python script illustrating all concepts and solutions.
- `QUICKSTART.md`: Setup and execution guide.
- `Makefile`: Commands to launch Jupyter (`make run`) and clean up (`make clean`).
