# Adding Margins and Totals

This module covers adding row, column, and grand totals to summary reports using `margins=True` in `pd.pivot_table()` and `pd.crosstab()`, understanding the mathematical principles of unweighted marginal calculations, and computing normalised frequency distributions.

---

## Learning Objectives
- Add row, column, and grand totals to pivot tables using `margins=True` and `margins_name='Total'`.
- Understand the aggregation nuance: why margins compute the true aggregate of the entire unpartitioned dataset rather than the average of cell averages.
- Generate contingency tables with `pd.crosstab()`.
- Normalise frequency tables across rows (`normalize='index'`), columns (`normalize='columns'`), or the entire dataset (`normalize='all'`).

---

## Folder Structure
- `docs/`: Conceptual documentation on margins, grand totals, and frequency normalisation.
- `notebooks/`:
  - `01_06.Adding-Margins-Totals.ipynb`: Interactive notebook with code and practice exercises.
- `src/`:
  - `AddingMarginsTotals.py`: Runnable Python script illustrating all concepts and solutions.
- `QUICKSTART.md`: Setup and execution guide.
- `Makefile`: Commands to launch Jupyter (`make run`) and clean up (`make clean`).
