# Multi-Level Grouping

This module covers grouping datasets across multiple categorical keys simultaneously, navigating and slicing hierarchical MultiIndex rows, pivoting grouped dimensions with `.unstack()`, and calculating cohort proportions.

---

## Learning Objectives
- Group DataFrames by composite keys using `df.groupby(['Key1', 'Key2'])`.
- Inspect and navigate hierarchical MultiIndex row structures.
- Slice multi-level grouped data using `.loc[]` by top-level groups or exact composite tuples.
- Transform hierarchical grouped outputs into side-by-side comparison tables using `.unstack()`.
- Broadcast group summaries across individual observations using `.transform()` to compute within-cohort percentages.

---

## Folder Structure
- `docs/`: Conceptual documentation on multi-level grouping and hierarchical index navigation.
- `notebooks/`:
  - `01_02.Multi-Level-Grouping.ipynb`: Interactive notebook with code and practice exercises.
- `src/`:
  - `MultiLevelGrouping.py`: Runnable Python script illustrating all concepts and solutions.
- `QUICKSTART.md`: Setup and execution guide.
- `Makefile`: Commands to launch Jupyter (`make run`) and clean up (`make clean`).
