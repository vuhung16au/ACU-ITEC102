# Quickstart: Gradient Boosting

Follow these steps to set up the environment and run the training scripts for both Regression (Housing Prices) and Classification (Vehicle Inspections).

## 1. Prerequisites

Ensure you have `uv` (the fast Python package installer and resolver) installed.

## 2. Setup the Environment

We use a `Makefile` to manage the lifecycle commands. To install all dependencies defined in `pyproject.toml`, run:

```bash
make setup
```

## 3. Run the Models

You can run both the regression and classification models sequentially by running:

```bash
make run
```

This will:
1. Automatically fetch or generate the datasets via `src/data_fetcher.py`.
2. Execute `src/train_regression.py` to compare XGBoost and LightGBM on predicting Australian house prices.
3. Execute `src/train_classification.py` to compare them on predicting vehicle inspection outcomes.

## 4. Run Tests

To verify that the code and data pipeline work correctly, run the end-to-end tests:

```bash
make test
```

## 5. Cleanup

To remove the virtual environment and cached files:

```bash
make clean
```
