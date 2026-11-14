# Exploratory Data Analysis (EDA) Pipeline & Correlation Matrices

This document covers the full EDA workflow used in **Project 32** and shows how `scipy.stats` complements `pandas` and `seaborn` during correlation analysis.

---

## 1. The Full EDA Pipeline

Exploratory Data Analysis is the structured process of understanding and preparing data before modelling:

1. **Data Collection / Generation:** Load raw records (`aus_health_survey_raw.csv`).
2. **Inspection:** Check shapes, data types, missing values (`df.isna().sum()`), and summary distributions (`df.describe()`).
3. **Cleaning:**
   - Remove rows missing essential fields (`htm3`, `weight1`, `weight2`, `sex`).
   - Filter out impossible sentinel values (e.g., `htm3 = 999.0` or `-10.0`, `weight1 = 550.0` or `12.0`).
4. **Feature Engineering:** Create meaningful derived columns:
   - `weight_change = weight2 - weight1` (negative values represent weight loss).
   - `weight_height_ratio = weight2 / htm3` (normalises weight by height in `kg/cm`).
5. **Statistical Testing & Correlation:** Quantify group differences and relationships with `scipy.stats`.
6. **Visualisation & Interpretation:** Plot distributions, heatmaps, and regression lines with `seaborn`, then explain what the numbers actually mean.

---

## 2. Comparing Metrics with Different Units

In this project, we test two different metrics between males and females:

- `weight_change` measured in **kilograms (`kg`)**
- `weight_height_ratio` measured in **kilograms per centimetre (`kg/cm`)**

You **cannot** compare a mean difference of `0.41 kg` directly against `0.062 kg/cm` because their units are completely different. However, SciPy's **t-statistic** and **p-value** are unit-free, letting us evaluate statistical evidence consistently across both tests.

---

## 3. Correlation Matrices with SciPy (`pearsonr` and `spearmanr`)

While `df.corr()` computes a quick correlation table, it does **not** return p-values. By looping over column pairs with `scipy.stats`, we get both strength and significance:

- **Pearson's $r$ (`stats.pearsonr`):** Measures **linear** correlation between two continuous variables (from `-1.0` to `+1.0`). Sensitive to outliers.
- **Spearman's $\rho$ (`stats.spearmanr`):** Measures **monotonic** (rank-order) correlation. More robust when data are skewed or contain outliers.

### Reading a Correlation Matrix Heatmap
- **Diagonal (`1.00`):** Every variable correlates perfectly with itself.
- **Symmetric:** $\text{corr}(A, B) = \text{corr}(B, A)$, so hiding the upper triangle avoids visual clutter.
- **Warm colours ($r > 0$):** Variables move together (e.g., `weekly_exercise_hrs` and `daily_steps`).
- **Cool colours ($r < 0$):** As one increases, the other decreases (e.g., more `weekly_exercise_hrs` correlates with more negative `weight_change`, i.e., greater weight loss).

> **Remember:** Correlation does not automatically imply causation—especially in observational surveys where unmeasured lifestyle factors may also contribute.
