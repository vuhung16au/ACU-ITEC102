# GroupBy Basics

This module covers the core Split-Apply-Combine paradigm in Pandas using `df.groupby()`, demonstrating how to partition tabular datasets into cohorts, compute descriptive statistics, and control output indexing.

---

## Learning Objectives
- Master the three phases of Hadley Wickham's Split-Apply-Combine workflow.
- Create and inspect `DataFrameGroupBy` objects (`.ngroups`, `.groups`, `.size()`).
- Extract specific sub-cohorts using `.get_group()`.
- Apply aggregate functions (`.mean()`, `.sum()`, `.count()`, `.min()`, `.max()`) on single and multiple columns.
- Prevent grouping keys from becoming the row index using `as_index=False`.

---

## Folder Structure
- `docs/`: Conceptual documentation on the Split-Apply-Combine paradigm and syntax.
- `notebooks/`:
  - `01_01.GroupBy-Basics.ipynb`: Interactive notebook with code and practice exercises.
- `src/`:
  - `GroupByBasics.py`: Runnable Python script illustrating all concepts and solutions.
- `QUICKSTART.md`: Setup and execution guide.
- `Makefile`: Commands to launch Jupyter (`make run`) and clean up (`make clean`).
