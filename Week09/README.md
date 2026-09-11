# Week 09: Advanced Data Wrangling with Pandas

Welcome to **Week 09** of **ITEC102**. In real-world data science, insights rarely come from a single, static 2D table. Data is distributed across disparate database tables, recorded in varied dimensions, or formatted for human eyes rather than computational pipelines.

This week covers advanced data wrangling techniques: **Hierarchical Indexing (MultiIndex)**, **Combining & Merging Datasets**, **Relational Join Semantics**, **Key Alignment**, and **Data Reshaping (Pivot, Melt, Stack, Unstack)**.

---

## Weekly Learning Objectives

By the end of this week, students will be able to:
1. **Manipulate MultiIndex Structures**: Create, slice, index, and aggregate data across hierarchical row and column levels.
2. **Combine and Merge Datasets**: Use `pd.concat()` to stack observations and `pd.merge()` to perform relational merges across common keys.
3. **Master Relational Join Semantics**: Distinguish between Inner, Left, Right, and Outer joins, understanding why Left Joins are the standard in business analytics.
4. **Merge Across Disparate Key Names**: Join tables when primary and foreign keys have different column names (`left_on` / `right_on`) or join on indexes.
5. **Reshape Between Wide and Long Formats**: Transform presentation tables into tidy data using `pd.melt()` and construct summary matrices with `df.pivot()` and `df.pivot_table()`.
6. **Stack and Unstack Matrix Dimensions**: Pivot columns into index levels (`.stack()`) and index levels into column headers (`.unstack()`).

---

## Topic Structure

| # | Topic Folder | Focus Area | Key Functions | Real-World Context |
|---|---|---|---|---|
| **01** | [`01.Hierarchical-Indexing`](./01.Hierarchical-Indexing/) | MultiIndex creation, slicing, and level aggregation | `pd.MultiIndex`, `.loc[]`, `.xs()`, `groupby(level=...)` | Multi-city Australian climate & retail metrics |
| **02** | [`02.Combining-and-Merging-Datasets`](./02.Combining-and-Merging-Datasets/) | Concatenation along axes and relational merging | `pd.concat(axis=0/1)`, `pd.merge()`, `indicator=True` | University semester cohorts & enrolments |
| **03** | [`03.Inner-vs-Left-Join`](./03.Inner-vs-Left-Join/) | Inner, Left, Right, and Outer join behaviors | `pd.merge(how='inner'/'left'/'outer')` | Student demographics & scholarship awards |
| **04** | [`04.Merging-with-Different-Column-Names`](./04.Merging-with-Different-Column-Names/) | Joining mismatched keys and disambiguating columns | `left_on`, `right_on`, `left_index`, `suffixes` | Disparate Student Portal vs Finance databases |
| **05** | [`05.Reshaping-Data-Pivot-and-Melt`](./05.Reshaping-Data-Pivot-and-Melt/) | Tidy data: unpivoting (melt) and cross-tabulation (pivot) | `pd.melt()`, `df.pivot()`, `df.pivot_table()` | Quarterly subject marks & temperature reports |
| **06** | [`06.Stack-and-Unstack`](./06.Stack-and-Unstack/) | Pivoting between column headers and row index levels | `df.stack()`, `df.unstack(level=...)`, `fill_value` | Multi-semester academic grade matrices |

---

## Folder Organization

Each topic folder follows a standard modular layout:
```text
Topic-Folder/
├── docs/             # Conceptual guides detailing theoretical foundations
├── notebooks/        # Interactive Jupyter notebook (.ipynb)
├── src/              # Standalone, runnable Python script (.py)
├── Makefile          # Commands to run jupyter and clean caches
├── pyproject.toml    # Dependencies managed with uv
├── QUICKSTART.md     # Step-by-step setup and execution guide
└── README.md         # Topic overview and learning outcomes
```

---

## Getting Started

Refer to [QUICKSTART.md](./QUICKSTART.md) for full instructions on running the notebooks and scripts using `uv` and `make`.
