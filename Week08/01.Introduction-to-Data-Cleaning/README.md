# Introduction to Data Cleaning

This module introduces the end-to-end data cleaning workflow in Pandas, focusing on auditing dataset health, identifying missing data, detecting duplicates, and enforcing data type and domain validity.

---

## Learning Objectives
- Conduct systematic dataset audits using `.info()`, `.isna().sum()`, and `.shape`.
- Detect and remove duplicate observations using `.duplicated()` and `.drop_duplicates()`.
- Use nullable data types such as `'Int64'` to safely store integer columns with nulls.
- Identify impossible or out-of-range numerical values.
- Clean text fields using `.str.strip()` and casing methods.

---

## Folder Structure
- `docs/`: Conceptual documentation on data hygiene and cleaning workflows.
- `notebooks/`:
  - `01-introduction-to-data-cleaning.ipynb`: Interactive walkthrough with code and exercises.
  - `messy_student_data.csv`: Sample dataset of 100 student records with missing entries.
- `src/`:
  - `IntroductiontoDataCleaning.py`: Runnable Python script illustrating all concepts and solutions.
- `QUICKSTART.md`: Setup and execution guide.
- `Makefile`: Commands to launch Jupyter (`make run`) and clean up (`make clean`).
