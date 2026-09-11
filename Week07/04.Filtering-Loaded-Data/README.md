# Filtering Loaded Data

This module covers filtering and subsetting Pandas DataFrames using conditional logic, boolean masks, set membership (`.isin()`), string methods, and `.query()`.

---

## Learning Objectives
- Create boolean masks using comparison operators (`>`, `<`, `==`, `!=`).
- Combine multiple conditions using bitwise operators (`&`, `|`, `~`) with correct parenthesis grouping.
- Filter categorical columns efficiently using `.isin()`.
- Filter string/text columns using vectorized `.str` accessors.
- Write readable, expressive queries using `df.query()`.

---

## Folder Structure
- `docs/`: Conceptual documentation on boolean indexing and operator precedence.
- `notebooks/`:
  - `04-filtering-loaded-data.ipynb`: Interactive notebook with code and practice exercises.
  - `sample_weather.csv`: 10-day Australian weather dataset.
- `src/`:
  - `FilteringLoadedData.py`: Runnable Python script illustrating all concepts and solutions.
- `QUICKSTART.md`: Setup and execution instructions.
- `Makefile`: Commands to launch Jupyter (`make run`) and clean up (`make clean`).
