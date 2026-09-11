# Handling Missing Data

This module covers inspecting and dropping missing data in Pandas using various options of `df.dropna()`.

---

## Learning Objectives
- Identify rows and columns with missing values using `.isna()`.
- Compare dropping criteria: `how='any'` (default) vs. `how='all'`.
- Perform targeted row dropping using `subset=['ColName']` to protect non-critical fields.
- Use threshold-based dropping (`thresh=k`) to retain dense records.
- Calculate and evaluate sample loss percentage and selection bias.

---

## Folder Structure
- `docs/`: Conceptual documentation on missing data mechanics and dropping strategies.
- `notebooks/`:
  - `02-handling-missing-data.ipynb`: Interactive notebook with code and practice exercises.
  - `messy_student_data.csv`: Sample dataset of 100 student records with missing values.
- `src/`:
  - `HandlingMissingData.py`: Runnable Python script illustrating all concepts and solutions.
- `QUICKSTART.md`: Setup and execution instructions.
- `Makefile`: Commands to launch Jupyter (`make run`) and clean up (`make clean`).
