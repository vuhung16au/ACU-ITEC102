# Week 11: Quick Start Guide

This guide explains how to set up your environment, execute Python scripts, and launch Jupyter notebooks across Week 11.

---

## 1. Prerequisites
Ensure you have Python 3.10+ installed. Activate the dedicated virtual environment that includes `matplotlib`, `pandas`, and `numpy`:
```bash
# From the repository root
source Week11/01.Why-Visualisation-Matters/.venv/bin/activate
```

---

## 2. Running Python Scripts
Each topic folder contains a self-contained Python script under `src/`:

```bash
# 01. Why Visualisation Matters
python Week11/01.Why-Visualisation-Matters/src/WhyVisualisationMatters.py

# 02. Line Plots
python Week11/02.Line-Plots/src/LinePlots.py

# 03. Bar Charts
python Week11/03.Bar-Charts/src/BarCharts.py

# 04. Pie Charts
python Week11/04.Pie-Charts/src/PieCharts.py

# 05. Histograms
python Week11/05.Histograms/src/Histograms.py

# 06. Customising and Styling
python Week11/06.Customising-and-Styling/src/CustomisingandStyling.py
```

---

## 3. Running Jupyter Notebooks
Each topic includes a dedicated Jupyter notebook under `notebooks/`:

```bash
# Navigate to any topic directory
cd Week11/01.Why-Visualisation-Matters

# Launch Jupyter Lab / Notebook using Makefile
make run
```
Or start Jupyter directly from the repository root:
```bash
jupyter lab Week11/
```
