# Statistical Filling (Imputation)

This module covers imputing missing data using statistical measures of central tendency (mean, median, mode) and cohort-based group filling with Pandas.

---

## Learning Objectives
- Evaluate the trade-offs of imputing missing data versus dropping records.
- Select appropriate summary metrics: mean for symmetric data, median for skewed/outlier-prone data, and mode for categoricals.
- Implement group-specific imputation with `groupby().transform()` for context-sensitive estimates.
- Validate that imputation does not artificially bias distributions or variances.

---

## Folder Structure
- `docs/`: Conceptual documentation on imputation theory and distribution sensitivity.
- `notebooks/`:
  - `03-statistical-filling.ipynb`: Interactive notebook with code and practice exercises.
  - `messy_student_data.csv`: Sample student dataset with missing attributes.
- `src/`:
  - `StatisticalFilling.py`: Runnable Python script illustrating all concepts and solutions.
- `QUICKSTART.md`: Setup and execution guide.
- `Makefile`: Commands to launch Jupyter (`make run`) and clean up (`make clean`).
