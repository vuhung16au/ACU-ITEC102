# Pie Charts

This module covers part-to-whole proportional visualisations using Matplotlib, including pie charts with `autopct`, slice emphasis via `explode`, modern donut charts, and the cognitive perceptual reasons why sorted bar charts are often preferred.

---

## Learning Objectives
- Construct proportional pie charts using `ax.pie()` with formatted percentages.
- Emphasize priority cohorts using slice offsets (`explode=...`).
- Build modern Donut Charts using `wedgeprops=dict(width=...)` and central text annotations.
- Understand the limits of angle- and area-based visual perception compared to linear bar lengths.

---

## Folder Structure
- `docs/`: Conceptual documentation on pie charts, donut charts, and visual perception guidelines.
- `notebooks/`:
  - `01_04.Pie-Charts.ipynb`: Interactive notebook with code and practice exercises.
- `src/`:
  - `PieCharts.py`: Runnable Python script illustrating all concepts and solutions.
- `QUICKSTART.md`: Setup and execution guide.
- `Makefile`: Commands to launch Jupyter (`make run`) and clean up (`make clean`).
