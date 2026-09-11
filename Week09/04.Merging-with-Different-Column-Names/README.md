# Merging with Different Column Names

This module covers handling mismatched join keys, overlapping non-key column names with custom suffixes, and merging across DataFrames that use different naming conventions or index keys.

---

## Learning Objectives
- Merge DataFrames with mismatched key column names using `left_on` and `right_on`.
- Clean up redundant key columns after merging using `.drop(columns=...)`.
- Disambiguate overlapping column names using explicit `suffixes=('_left', '_right')`.
- Join DataFrames on an Index using `left_index=True` or `right_index=True`.
- Identify and prevent schema mismatches in multi-source data ingestion pipelines.

---

## Folder Structure
- `docs/`: Conceptual documentation on handling schema variations and key mapping.
- `notebooks/`:
  - `01_04.Merging-with-Different-Column-Names.ipynb`: Interactive notebook with code and practice exercises.
- `src/`:
  - `MergingwithDifferentColumnNames.py`: Runnable Python script illustrating all concepts and solutions.
- `QUICKSTART.md`: Setup and execution guide.
- `Makefile`: Commands to launch Jupyter (`make run`) and clean up (`make clean`).
