# Writing DataFrames to Files

This module covers exporting processed, transformed, and aggregated Pandas DataFrames into disk files including CSV, JSON, and Excel formats.

---

## Learning Objectives
- Export DataFrames to CSV using `df.to_csv(..., index=False)`.
- Understand why `index=False` is essential to avoid corrupting columns upon reload.
- Export DataFrames to JSON for web applications and REST APIs (`df.to_json(orient='records')`).
- Export summary tables to Microsoft Excel workbooks using `df.to_excel()`.
- Export compressed archives (`.csv.gz`) directly without external tools.

---

## Folder Structure
- `docs/`: Conceptual documentation on export methods, parameters, and verification.
- `notebooks/`:
  - `05-writing-dataframes-to-files.ipynb`: Interactive notebook with code and practice exercises.
  - `sample_weather.csv`: 10-day Australian weather dataset.
- `src/`:
  - `WritingDataFramestoFiles.py`: Runnable Python script illustrating all concepts and solutions.
- `QUICKSTART.md`: Setup and execution instructions.
- `Makefile`: Commands to launch Jupyter (`make run`) and clean up (`make clean`).
