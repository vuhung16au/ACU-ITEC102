# 28. Gradient Boosting (XGBoost vs LightGBM)

This enrichment project introduces students to **Gradient Boosting Decision Trees (GBDT)**, a powerful ensemble machine learning technique. It compares the two most popular libraries: **XGBoost** and **LightGBM**.

## Screenshot(s) & Example Run 

```bash 
make setup         
uv sync
Resolved 25 packages in 24ms
Checked 21 packages in 10ms
```

```bash 

make run 
uv sync
Resolved 25 packages in 25ms
Checked 21 packages in 9ms
--- Running Regression Training ---
uv run python src/train_regression.py
Fetching Housing Data (Regression)...

Training on 255 samples, testing on 64 samples.
Note: The dataset only has 'sale_year', 'small_area', and 'type'.
Without features like bedrooms or land size, the model's R2 score will naturally be very low!

Training XGBoost Regressor...
XGBoost RMSE: $1,667,359.46
XGBoost R2 Score: 0.1298

Training LightGBM Regressor...
LightGBM RMSE: $1,654,970.90
LightGBM R2 Score: 0.1427

Regression training complete.

--- Running Classification Training ---
uv run python src/train_classification.py
Fetching Crash Data (Classification)...

Training on 8000 samples, testing on 2000 samples.
Class Distribution: 7289 Property Damage (0) vs 711 Injuries (1). Ratio: 10.25

Training XGBoost Classifier (with scale_pos_weight)...
XGBoost Accuracy: 0.6685
XGBoost F1-Score: 0.1445

Training LightGBM Classifier (with scale_pos_weight)...
LightGBM Accuracy: 0.6730
LightGBM F1-Score: 0.1906

Classification training complete.

```

```bash 
make test
uv sync
Resolved 25 packages in 7ms
Checked 21 packages in 0.82ms
uv run pytest tests/ -v
=========================================== test session starts ============================================
platform darwin -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0 -- /Users/vuhung/00.Work/00.Workspace/ACU-ITEC102/Enrichment/Machine-Learning/28.Gradient-Boosting/.venv/bin/python3
cachedir: .pytest_cache
rootdir: /Users/vuhung/00.Work/00.Workspace/ACU-ITEC102/Enrichment/Machine-Learning/28.Gradient-Boosting
configfile: pyproject.toml
collected 2 items                                                                                          

tests/test_model.py::test_housing_data_generation PASSED                                             [ 50%]
tests/test_model.py::test_inspection_data_generation PASSED                                          [100%]

============================================ 2 passed in 0.30s =============================================
```

```bash 
make clean 
```

## Learning Outcomes

In this project, you will learn how to:
- Understand the difference between regression and classification tasks.
- Train machine learning models using `XGBoost` and `LightGBM`.
- Compare the `scikit-learn` compatible APIs for both libraries.
- Fetch data from data.gov.au via CKAN, or use fallback synthetic Australian datasets.
- Evaluate model performance using standard metrics (RMSE, R2, Accuracy, F1-Score).

## Project Structure

- `src/data_fetcher.py`: Fetches real data from the CKAN API or generates synthetic mock data for Australian house prices and vehicle inspections.
- `src/train_regression.py`: Trains regressors to predict house prices.
- `src/train_classification.py`: Trains classifiers to predict vehicle inspection outcomes.
- `docs/theory.md`: Theoretical background on decision trees, boosting, and the differences between XGBoost and LightGBM.

## Get Started

Check out the [QUICKSTART.md](QUICKSTART.md) file for instructions on how to set up the environment and run the models!

## Future Works / Challenges for Students

Now that you've got the basics down, here are some challenges to deepen your understanding:
1. **The Class Imbalance Problem:** The ACT crash dataset is highly imbalanced (few injuries, many property damage crashes). We used `scale_pos_weight` to fix the F1-Score. Can you try using **SMOTE** (from the `imbalanced-learn` library) to artificially oversample the injury cases instead? Which approach works better?
2. **Feature Engineering (Regression):** The Melbourne housing dataset currently gives a very low $R^2$ score because it only provides the year of sale and the suburb. Try finding a more detailed dataset on `data.gov.au` that includes the number of bedrooms, bathrooms, and land size to drastically improve the regression model's predictive power!
3. **Hyperparameter Tuning:** We used hardcoded parameters (e.g., `max_depth=4`, `learning_rate=0.1`). Try using `GridSearchCV` or `RandomizedSearchCV` from `scikit-learn` to programmatically find the absolute best combination of hyperparameters!
