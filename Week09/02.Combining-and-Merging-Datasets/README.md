# Combining and Merging Datasets

This module covers joining, concatenating, and merging disparate datasets in Pandas using `pd.concat()` and `pd.merge()`.

---

## Learning Objectives
- Append datasets vertically along rows using `pd.concat(axis=0, ignore_index=True)`.
- Concatenate datasets horizontally along columns using `pd.concat(axis=1)`.
- Perform relational merges on common key attributes with `pd.merge()`.
- Audit dataset overlap and key match rates using `indicator=True`.

---

## Folder Structure
- `docs/`: Conceptual documentation comparing concatenation and relational merges.
- `notebooks/`:
  - `01_02.Combining-and-Merging-Datasets.ipynb`: Interactive notebook with code and practice exercises.
- `src/`:
  - `CombiningandMergingDatasets.py`: Runnable Python script illustrating all concepts and solutions.
- `QUICKSTART.md`: Setup and execution guide.
- `Makefile`: Commands to launch Jupyter (`make run`) and clean up (`make clean`).
