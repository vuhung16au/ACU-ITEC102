# Custom Aggregation Functions

This module covers authoring and applying custom Python functions and lambda expressions inside Pandas `.agg()`, allowing data analysts to compute domain-specific statistical metrics across cohorts.

---

## Learning Objectives
- Author robust custom statistical functions that accept a `pd.Series` and return a scalar value.
- Compute domain metrics including data range (`max - min`), Interquartile Range (`IQR`), trimmed means, and pass rate percentages.
- Label custom aggregated columns cleanly using `('Column_Name', function)` tuples.
- Use inline anonymous `lambda` functions for concise, on-the-fly group statistics.
- Handle missing values and edge cases safely inside custom aggregators.

---

## Folder Structure
- `docs/`: Conceptual documentation on custom aggregation functions and best practices.
- `notebooks/`:
  - `01_04.Custom-Aggregation-Functions.ipynb`: Interactive notebook with code and practice exercises.
- `src/`:
  - `CustomAggregationFunctions.py`: Runnable Python script illustrating all concepts and solutions.
- `QUICKSTART.md`: Setup and execution guide.
- `Makefile`: Commands to launch Jupyter (`make run`) and clean up (`make clean`).
