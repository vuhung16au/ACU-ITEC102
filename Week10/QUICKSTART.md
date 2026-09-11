# Week 10: Quick Start Guide

This guide explains how to set up your environment, execute Python scripts, and launch Jupyter notebooks across Week 10.

---

## 1. Prerequisites
Ensure you have Python 3.10+ and `uv` installed, or activate the repository virtual environment:
```bash
# From the repository root
source Week10/01.GroupBy-Basics/.venv/bin/activate
```

---

## 2. Running Python Scripts
Each topic folder contains a self-contained Python script under `src/`:

```bash
# 01. GroupBy Basics
python Week10/01.GroupBy-Basics/src/GroupByBasics.py

# 02. Multi-Level Grouping
python Week10/02.Multi-Level-Grouping/src/MultiLevelGrouping.py

# 03. Advanced Aggregation
python Week10/03.Advanced-Aggregation/src/AdvancedAggregation.py

# 04. Custom Aggregation Functions
python Week10/04.Custom-Aggregation-Functions/src/CustomAggregationFunctions.py

# 05. Pivot Tables
python Week10/05.Pivot-Tables/src/PivotTables.py

# 06. Adding Margins and Totals
python Week10/06.Adding-Margins-Totals/src/AddingMarginsTotals.py
```

---

## 3. Running Jupyter Notebooks
Each topic includes a dedicated Jupyter notebook under `notebooks/`:

```bash
# Navigate to any topic directory
cd Week10/01.GroupBy-Basics

# Launch Jupyter Lab / Notebook using Makefile
make run
```
Or start Jupyter directly from the repository root:
```bash
jupyter lab Week10/
```
