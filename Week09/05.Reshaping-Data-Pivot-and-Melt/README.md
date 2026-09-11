# Reshaping Data: Pivot and Melt

This module covers reshaping datasets between "wide" and "long" (tidy) formats in Pandas using `pd.melt()`, `DataFrame.pivot()`, and `DataFrame.pivot_table()`.

---

## Learning Objectives
- Understand the principles of "tidy data" and the trade-offs between wide and long representations.
- Transform wide tables into long datasets using `pd.melt(id_vars, value_vars, var_name, value_name)`.
- Reshape long datasets into wide matrices using `DataFrame.pivot(index, columns, values)`.
- Aggregate duplicate key observations using `DataFrame.pivot_table(aggfunc, fill_value, margins=True)`.
- Select the optimal tabular layout for data analysis, grouping, and visualisation.

---

## Folder Structure
- `docs/`: Conceptual documentation on wide vs long data structures and pivot operations.
- `notebooks/`:
  - `01_05.Reshaping-Data-Pivot-and-Melt.ipynb`: Interactive notebook with code and practice exercises.
- `src/`:
  - `ReshapingDataPivotandMelt.py`: Runnable Python script illustrating all concepts and solutions.
- `QUICKSTART.md`: Setup and execution guide.
- `Makefile`: Commands to launch Jupyter (`make run`) and clean up (`make clean`).
