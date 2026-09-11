# Inner vs Left Join

This module covers understanding and contrasting relational join types in Pandas, emphasizing the operational differences between `how='inner'`, `how='left'`, `how='right'`, and `how='outer'`.

---

## Learning Objectives
- Master `pd.merge()` join parameters (`how='inner'`, `'left'`, `'right'`, `'outer'`).
- Recognize why Left Joins are favored in business intelligence to preserve core entities.
- Identify missing/unmatched cohorts using Left Joins with null filtering.
- Prevent row multiplication bugs using key validation (`validate='one_to_one'`).

---

## Folder Structure
- `docs/`: Conceptual documentation on join behaviors and cardinality.
- `notebooks/`:
  - `01_03.Inner-vs-Left-Join.ipynb`: Interactive notebook with code and practice exercises.
- `src/`:
  - `InnervsLeftJoin.py`: Runnable Python script illustrating all concepts and solutions.
- `QUICKSTART.md`: Setup and execution guide.
- `Makefile`: Commands to launch Jupyter (`make run`) and clean up (`make clean`).
