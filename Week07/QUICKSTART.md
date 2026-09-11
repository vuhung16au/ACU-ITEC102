# Week 07: Quickstart Guide

This guide describes how to run and test the interactive notebooks and Python scripts across all topics in Week 07.

---

## Prerequisites

Ensure you have installed:
- **Python 3.14** (or Python 3.10+)
- **uv** (ultra-fast Python package manager)
- **make** (command runner)

Verify your installations:
```bash
python3 --version
uv --version
make --version
```

---

## Running a Topic

Navigate to any topic folder, for example `01.Reading-CSV-Files`:
```bash
cd 01.Reading-CSV-Files
```

### Option A: Interactive Jupyter Notebook
To start Jupyter Notebook with the virtual environment automatically configured by `uv`:
```bash
make run
```
Or directly:
```bash
uv run jupyter notebook notebooks/
```
Once opened, click on the notebook file (e.g., `01-reading-csv-files.ipynb`) and run the cells sequentially using `Shift + Enter`.

### Option B: Standalone Python Script
To run the equivalent command-line Python script from the topic folder:
```bash
uv run src/ReadingCSVFiles.py
```
*(Replace `ReadingCSVFiles.py` with the corresponding script name for other topics, e.g., `src/ExploringandSummarisingData.py`)*

---

## Running Automated Notebook Checks
To verify that all notebook cells run top-to-bottom without throwing errors:
```bash
uv run jupyter nbconvert --execute --to notebook --inplace notebooks/*.ipynb
```

---

## Cleaning Up Temporary Files
To remove the local `.venv`, `__pycache__`, and checkpoint directories:
```bash
make clean
```
*(Or run `rm -rf .venv .ipynb_checkpoints __pycache__ uv.lock`)*
