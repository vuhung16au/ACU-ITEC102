# Reading Excel and JSON Files

This module introduces loading non-CSV data formats—specifically Microsoft Excel workbooks (`.xlsx`) and structured JSON files (`.json`)—into Pandas DataFrames.

---

## Learning Objectives
- Ingest spreadsheet data with `pd.read_excel()` using `sheet_name`.
- Discover sheets within workbooks using `pd.ExcelFile`.
- Load tabular API payloads using `pd.read_json()`.
- Flatten nested, hierarchical JSON responses into tabular columns using `pd.json_normalize()`.
- Compare performance, hierarchical support, and suitability across CSV, Excel, and JSON formats.

---

## Folder Structure
- `docs/`: Conceptual documentation on Excel engines, sheets, and JSON schemas.
- `notebooks/`:
  - `03-reading-excel-and-json-files.ipynb`: Interactive notebook with code and practice exercises.
  - `energy_stats.xlsx`: Sample Excel file containing NSW clean energy statistics.
  - `sydney_airbnb.json`: Sample JSON file of Sydney holiday listings.
- `src/`:
  - `ReadingExcelandJSONFiles.py`: Runnable Python script illustrating all concepts and solutions.
- `QUICKSTART.md`: Setup and execution instructions.
- `Makefile`: Commands to launch Jupyter (`make run`) and clean up (`make clean`).
