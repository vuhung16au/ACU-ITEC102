# Week 12: Quick Start Guide

This guide explains how to set up your environment, execute Python scripts, and launch Jupyter notebooks across Week 12.

---

## 1. Prerequisites
Ensure you have Python 3.10+ installed. Activate the shared environment:
```bash
# From the repository root
source Week11/01.Why-Visualisation-Matters/.venv/bin/activate
```

---

## 2. Running Python Scripts
Each topic folder contains a self-contained Python script under `src/`:

```bash
# 01. Real-World Data Wrangling
python Week12/01.Real-World-Data-Wrangling/src/RealWorldDataWrangling.py

# 02. Exploratory Data Analysis
python Week12/02.Exploratory-Data-Analysis/src/ExploratoryDataAnalysis.py

# 03. Ethics in Data Science
python Week12/03.Ethics-in-Data-Science/src/EthicsinDataScience.py

# 04. Privacy in Action: Anonymisation
python Week12/04.Privacy-in-Action-Anonymisation/src/PrivacyinActionAnonymisation.py

# 05. Addressing Fairness and Bias
python Week12/05.Addressing-Fairness-and-Bias/src/AddressingFairnessandBias.py

# 06. Assessment 3 Capstone Project
python Week12/06.Assessment-3-Capstone-Project/src/Assessment3CapstoneProject.py
```

---

## 3. Running Jupyter Notebooks
Each topic includes a dedicated Jupyter notebook under `notebooks/`:

```bash
# Navigate to any topic directory
cd Week12/01.Real-World-Data-Wrangling

# Launch Jupyter Lab / Notebook using Makefile
make run
```
Or start Jupyter directly from the repository root:
```bash
jupyter lab Week12/
```
