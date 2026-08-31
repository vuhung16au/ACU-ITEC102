# Quickstart

This folder uses `uv` for dependency management and `make` for executing common tasks.

## Running the Notebook
To launch the Jupyter notebook locally:
```bash
make run
```
*(This runs `uv run jupyter notebook notebooks/` to start the environment)*

## Testing the Notebook
To execute all cells in the notebook headlessly and ensure there are no errors:
```bash
uv run jupyter nbconvert --execute --to notebook --inplace notebooks/*.ipynb
```
*(This is useful for verifying your code works before submitting)*

## Cleaning up
To remove the virtual environment (`.venv`), Jupyter checkpoints, lock files, and caches:
```bash
make clean
```

## Running the Python Script
From this folder, run:
```bash
uv run src/VariableScope.py
```
`uv` creates the project environment and installs the required dependencies automatically when needed.
