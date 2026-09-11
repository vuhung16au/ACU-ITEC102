# Reading a CSV File

This module introduces importing tabular data from Comma-Separated Values (`.csv`) files into Pandas DataFrames using `pd.read_csv()`.

---

## Learning Objectives
- Master `pd.read_csv()` and its most vital parameters (`parse_dates`, `index_col`, `usecols`, `nrows`).
- Understand data types (`dtypes`) after loading and why date parsing matters.
- Learn memory-saving techniques for large tabular files.

---

## Folder Structure
- `docs/`: Conceptual documentation on CSV specifications and Pandas ingestion options.
- `notebooks/`:
  - `01-reading-csv-files.ipynb`: Interactive walkthrough with code examples and exercises.
  - `sample_weather.csv`: 10-day Australian weather dataset (Sydney, Melbourne, Brisbane, Perth, Adelaide).
- `src/`:
  - `ReadingCSVFiles.py`: Runnable Python script illustrating all concepts and solutions.
- `QUICKSTART.md`: Step-by-step instructions to launch and run.
- `Makefile`: Commands to launch Jupyter (`make run`) and clean up (`make clean`).
