# Quickstart Guide

Run **33. Statsmodels Deep Dive** in four quick steps.

## 1. Prerequisites

- **Python 3.14+**
- **[uv](https://docs.astral.sh/uv/)**

## 2. Navigate & Install Dependencies

```bash
cd Enrichment/Data-Science/33.Statsmodels-Deep-Dive
make setup
```

*(Equivalent to `uv sync`.)*

## 3. Run the Demo

```bash
make run
```

*(Equivalent to `uv run python main.py`.)*

This generates the synthetic dataset (`data/aus_wellness_survey.csv`), prints all four `statsmodels` analytical comparisons, and saves two diagnostic charts in `images/`.

## 4. Run Tests & Clean Up

```bash
make test
make clean
```
