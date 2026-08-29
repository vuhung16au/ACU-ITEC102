# Quickstart Guide

Follow these steps to run the Energy Rating Data Cleaner pipeline on your local machine.

## Prerequisites
- `uv` (Fast Python package and project manager)
- Python 3.10+

## 1. Setup and Run
This project uses `uv` to manage dependencies. You don't need to manually create a virtual environment; `uv run` handles it automatically based on the `pyproject.toml` file.

Open your terminal, navigate to this project folder, and run:

```bash
make run
```
*(This executes `uv run streamlit run app.py` behind the scenes).*

Streamlit will automatically open your default web browser and navigate to `http://localhost:8501`.

## 2. Running Tests
To run the automated tests that verify data handling logic against the local mock data:

```bash
make test
```

## 3. Cleaning Up
To remove the generated virtual environment and cache files:

```bash
make clean
```
