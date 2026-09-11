# Customising and Styling

This module covers publication-quality formatting in Matplotlib, including theme management (`plt.style.use`), building multi-panel dashboard subplots (`plt.subplots`), custom annotations, and high-resolution figure exports.

---

## Learning Objectives
- Apply built-in aesthetic themes (e.g. `seaborn-v0_8-whitegrid`, `fivethirtyeight`).
- Construct cohesive multi-panel dashboard figures using `fig, axes = plt.subplots(nrows, ncols)`.
- Direct viewer attention to key trends and anomalies using `ax.annotate()`.
- Add benchmark threshold lines using `ax.axhline()`.
- Export high-resolution publication figures with `fig.savefig(dpi=300, bbox_inches='tight')`.

---

## Folder Structure
- `docs/`: Conceptual documentation on visual styling, subplots, and layout tuning.
- `notebooks/`:
  - `01_06.Customising-and-Styling.ipynb`: Interactive notebook with code and practice exercises.
- `src/`:
  - `CustomisingandStyling.py`: Runnable Python script illustrating all concepts and solutions.
- `QUICKSTART.md`: Setup and execution guide.
- `Makefile`: Commands to launch Jupyter (`make run`) and clean up (`make clean`).
