# Exploring and Summarising Data

This module covers exploratory data analysis (EDA) techniques using Pandas to inspect, profile, and summarise datasets.

---

## Learning Objectives
- Quickly inspect DataFrame shape, structure, and sample records (`.head()`, `.tail()`, `.shape`).
- Review systemic column metadata and data types using `.info()` and `.dtypes`.
- Generate descriptive statistical summaries using `.describe()`.
- Calculate targeted aggregations (`.mean()`, `.median()`, `.max()`, `.sum()`) and categorical counts (`.value_counts()`).
- Retrieve outlier or extreme records with `.idxmax()` and `.idxmin()`.

---

## Folder Structure
- `docs/`: Conceptual documentation on exploratory functions and summary statistics.
- `notebooks/`:
  - `02-exploring-and-summarising-data.ipynb`: Interactive walkthrough with code examples and exercises.
  - `sample_weather.csv`: 10-day Australian weather dataset.
- `src/`:
  - `ExploringandSummarisingData.py`: Runnable Python script illustrating all concepts and solutions.
- `QUICKSTART.md`: Setup and execution instructions.
- `Makefile`: Commands to launch Jupyter (`make run`) and clean up (`make clean`).
