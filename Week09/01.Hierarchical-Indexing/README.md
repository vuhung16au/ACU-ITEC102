# Hierarchical Indexing (MultiIndex)

This module covers creating, slicing, aggregating, and reshaping higher-dimensional data in Pandas using hierarchical row and column indices (`pd.MultiIndex`).

---

## Learning Objectives
- Construct MultiIndex objects using `pd.MultiIndex.from_arrays()` and `from_tuples()`.
- Access and subset records via `.loc[]` and cross-section slicing with `.xs()`.
- Perform level-aware aggregations using `df.groupby(level='LevelName')`.
- Convert back and forth between flat tables and hierarchical indexes with `reset_index()` and `set_index()`.

---

## Folder Structure
- `docs/`: Conceptual documentation on MultiIndex mechanics and dimension slicing.
- `notebooks/`:
  - `01_01.Hierarchical-Indexing.ipynb`: Interactive notebook with code and practice exercises.
- `src/`:
  - `HierarchicalIndexing.py`: Runnable Python script illustrating all concepts and solutions.
- `QUICKSTART.md`: Setup and execution guide.
- `Makefile`: Commands to launch Jupyter (`make run`) and clean up (`make clean`).
