# Exploratory Data Analysis (EDA): A Systematic Framework

This module teaches students how to systematically audit, explore, and extract meaningful patterns from real-world datasets before fitting statistical or machine learning models.

---

## Learning Objectives
- Master the **5-Step EDA Framework**: Structural Audit -> Distribution & Outliers -> Categorical Breakdown -> Bivariate Analysis -> Insights.
- Detect extreme values and errors using Tukey's Fences ($1.5 \times \text{IQR}$ rule) and boxplots.
- Compute descriptive statistics (mean, median, standard deviation, percentiles) and evaluate skewness.
- Analyse bivariate correlations using Pearson's $r$ and multi-variable group aggregations.
- Visualise multi-dimensional distributions using Matplotlib boxplots and scatter plots.

---

## Folder Structure
- `docs/`: Conceptual documentation on the 5-step EDA workflow and outlier detection theory.
- `notebooks/`:
  - `01_02.Exploratory-Data-Analysis.ipynb`: Interactive Jupyter notebook with graduate cohort data and exercises.
- `src/`:
  - `ExploratoryDataAnalysis.py`: Production-style Python script executing the complete EDA pipeline.
- `QUICKSTART.md`: Commands to run scripts and launch notebooks.
- `Makefile`: Convenience automation (`make run`, `make test`, `make clean`).
