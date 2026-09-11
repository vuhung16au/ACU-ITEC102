# Pivot Tables

This module covers creating two-dimensional aggregation matrices using `pd.pivot_table()`, contrasting pivot tables with standard `.groupby()`, handling sparse data with `fill_value`, and building multi-level summary grids.

---

## Learning Objectives
- Construct two-dimensional summary tables using `pd.pivot_table()`.
- Compare and contrast the output structure of `.groupby()` (hierarchical 1D) vs `pd.pivot_table()` (2D matrix).
- Configure key parameters: `values`, `index`, `columns`, and `aggfunc`.
- Substitute missing cell combinations cleanly using `fill_value=0`.
- Construct multi-level row and column pivot tables with multiple aggregation functions.

---

## Folder Structure
- `docs/`: Conceptual documentation on pivot tables and dimensional summarisation.
- `notebooks/`:
  - `01_05.Pivot-Tables.ipynb`: Interactive notebook with code and practice exercises.
- `src/`:
  - `PivotTables.py`: Runnable Python script illustrating all concepts and solutions.
- `QUICKSTART.md`: Setup and execution guide.
- `Makefile`: Commands to launch Jupyter (`make run`) and clean up (`make clean`).
