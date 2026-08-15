# Theoretical Background

## What is Gradient Boosting?

Gradient boosting is a machine learning technique for regression and classification problems, which builds a prediction model in the form of an ensemble of weak prediction models, typically decision trees. 

Unlike Random Forest which builds trees in parallel and averages them, **Gradient Boosting builds trees sequentially**. Each new tree tries to correct the errors (the "residuals" or gradients of the loss function) made by the previously combined trees.

## XGBoost vs LightGBM

Both are state-of-the-art implementations of gradient boosting decision trees (GBDT), but they have different underlying strategies:

### XGBoost (eXtreme Gradient Boosting)
- **Growth Strategy**: Traditionally uses a level-wise (depth-wise) tree growth strategy. It grows all nodes at the same level before moving to the next.
- **Strengths**: Highly robust, excellent regularisation (L1/L2) built-in to prevent overfitting, handles missing values gracefully.
- **When to use**: When accuracy and robustness are paramount and you have time to tune parameters.

### LightGBM (Light Gradient Boosting Machine)
- **Growth Strategy**: Uses a leaf-wise (best-first) tree growth strategy. It chooses the leaf with the maximum delta loss to grow.
- **Strengths**: Extremely fast training speed, uses less memory, and often achieves similar or better accuracy than XGBoost. Excellent for large datasets.
- **When to use**: When you have a very large dataset (>10,000 rows) or when training speed is a priority. (Note: leaf-wise growth can cause overfitting on very small datasets).

## Regression vs Classification

- **Regression**: Predicting a continuous numeric value (e.g., predicting the price of a house). The loss function is typically Mean Squared Error (MSE).
- **Classification**: Predicting a discrete class label (e.g., predicting if a vehicle passes or fails an inspection - binary classification). The loss function is typically Log Loss (Binary Cross-Entropy).

## The Accuracy Paradox & Class Imbalance

When working with real-world classification data (such as road crashes), you will often encounter **class imbalance**. For example, the vast majority of crashes only result in property damage, while a small fraction result in injuries.

If a dataset has 95% "property damage" crashes and 5% "injury" crashes, a "dumb" model that simply predicts "property damage" for every single crash will achieve **95% Accuracy**! However, it fails completely at its actual goal: identifying the dangerous crashes. This is known as the **Accuracy Paradox**.

### Why F1-Score Exposes the Truth
Because accuracy is misleading on imbalanced datasets, we use the **F1-Score**, which is the harmonic mean of **Precision** and **Recall**:
- **Precision**: When the model predicts an "Injury", how often is it actually an injury?
- **Recall**: Out of all the *actual* injuries that happened, how many did the model successfully find?

If a model predicts "property damage" for everything, its Recall for injuries is 0, making the F1-Score 0.

### How to Fix Imbalance
Gradient boosting libraries offer parameters like `scale_pos_weight` (or `is_unbalance=True` in LightGBM) to heavily penalize the model when it makes errors on the minority class. This forces the model to learn the minority class rather than ignoring it.
