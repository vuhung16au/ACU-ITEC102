# Stack and Unstack

This module covers reshaping hierarchical (MultiIndex) DataFrames by rotating levels between row indices and column headers using `DataFrame.stack()` and `DataFrame.unstack()`.

---

## Learning Objectives
- Understand the dimensional duality of hierarchical rows and columns in Pandas.
- Pivot column levels into row index levels using `DataFrame.stack()`.
- Pivot row index levels into column headers using `DataFrame.unstack()`.
- Target specific hierarchical levels by integer position or level name (`level='LevelName'`).
- Handle missing values resulting from incomplete index permutations with `fill_value=0`.
- Understand the symmetry and round-trip invertibility of `.stack()` and `.unstack()`.

---

## Folder Structure
- `docs/`: Conceptual documentation on MultiIndex rotation and hierarchy pivoting.
- `notebooks/`:
  - `01_06.Stack-and-Unstack.ipynb`: Interactive notebook with code and practice exercises.
- `src/`:
  - `StackandUnstack.py`: Runnable Python script illustrating all concepts and solutions.
- `QUICKSTART.md`: Setup and execution guide.
- `Makefile`: Commands to launch Jupyter (`make run`) and clean up (`make clean`).
