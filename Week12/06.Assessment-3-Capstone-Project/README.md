# Assessment 3: Capstone Synthesis Project

This module provides the capstone milestone framework for the ACU-ITEC102 unit, synthesizing data wrangling, exploratory data analysis, visual storytelling, privacy engineering, and algorithmic fairness auditing into a single end-to-end data product.

---

## Capstone Milestones
- **Milestone 1: Ingestion & Quality Audit**: Ingest heterogeneous tabular data and audit defects.
- **Milestone 2: Data Wrangling**: Clean strings, standardise categoricals, parse mixed dates and currency strings, and left-join auxiliary reference tables.
- **Milestone 3: Exploratory Data Analysis**: Calculate five-number summaries, detect outliers using Tukey's Fences, and analyze group segments.
- **Milestone 4: Visual Storytelling**: Design multi-panel figures with Matplotlib (boxplots, scatter plots) following object-oriented best practices.
- **Milestone 5: Privacy Engineering**: Implement salted SHA-256 cryptographic pseudonymisation, coarsen quasi-identifiers, and evaluate $k$-anonymity.
- **Milestone 6: Algorithmic Fairness & Governance**: Audit Automated Decision-Making (ADM) models for disparate impact under the 80% rule and document an Ethical Impact Assessment.

---

## Folder Structure
- `docs/`: Conceptual documentation and rubric criteria for Assessment 3.
- `notebooks/`:
  - `01_06.Assessment-3-Capstone-Project.ipynb`: Interactive Jupyter notebook detailing all 6 capstone milestones.
- `src/`:
  - `Assessment3CapstoneProject.py`: Full production Python pipeline running all 6 milestones end-to-end.
- `QUICKSTART.md`: Setup and run instructions.
- `Makefile`: Convenience commands (`make run`, `make test`, `make clean`).
