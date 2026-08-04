# Quickstart Guide

## Environment Setup
This directory uses `uv` for dependency management. To set up the environment, run:

```bash
uv sync
```

## Running the Notebook
To launch the Jupyter Notebook server, you can use the provided Makefile command:
```bash
make run
```
Alternatively, you can manually run:
```bash
uv run jupyter notebook notebooks/
```

## Cleaning up
To remove the generated artifacts, use:
```bash
make clean
```
