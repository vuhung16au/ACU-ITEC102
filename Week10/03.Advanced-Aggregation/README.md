# Advanced Aggregation

This module covers computing multi-metric group summaries in Pandas using `.agg()`, applying column-specific dictionary mappings, and leveraging modern Named Aggregations for clean, flat column outputs.

---

## Learning Objectives
- Apply multiple statistical aggregation functions to a single column using lists (`.agg(['mean', 'std', 'min', 'max'])`).
- Map specific columns to distinct aggregation functions using dictionaries (`.agg({'ColA': 'sum', 'ColB': 'mean'})`).
- Avoid messy MultiIndex column hierarchies using Pandas Named Aggregations (`new_col=('target', 'func')`).
- Summarise complex real-world datasets across multiple metrics efficiently.

---

## Folder Structure
- `docs/`: Conceptual documentation on advanced aggregation patterns and named aggregations.
- `notebooks/`:
  - `01_03.Advanced-Aggregation.ipynb`: Interactive notebook with code and practice exercises.
- `src/`:
  - `AdvancedAggregation.py`: Runnable Python script illustrating all concepts and solutions.
- `QUICKSTART.md`: Setup and execution guide.
- `Makefile`: Commands to launch Jupyter (`make run`) and clean up (`make clean`).
