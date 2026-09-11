# Data Sampling

This module covers drawing random and stratified sample subsets from Pandas DataFrames using `df.sample()` and `df.groupby().sample()`.

---

## Learning Objectives
- Extract random sample subsets by row count (`n`) and proportion (`frac`).
- Enforce reproducible results using the `random_state` seed parameter.
- Understand sampling with and without replacement (`replace=True/False`).
- Implement stratified sampling to prevent subgroup representation bias.
- Construct train/test validation splits.

---

## Folder Structure
- `docs/`: Conceptual documentation on sampling theory, random seeds, and stratification.
- `notebooks/`:
  - `05-sampling.ipynb`: Interactive notebook with code and practice exercises.
  - `messy_student_data.csv`: Sample dataset of 100 student records.
- `src/`:
  - `Sampling.py`: Runnable Python script illustrating all concepts and solutions.
- `QUICKSTART.md`: Setup and execution guide.
- `Makefile`: Commands to launch Jupyter (`make run`) and clean up (`make clean`).
