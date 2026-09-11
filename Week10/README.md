# Week 10: Data Aggregation and Group Operations

Welcome to Week 10 of ACU-ITEC102. This week explores **Data Aggregation and Group Operations** in Pandas, centered on Hadley Wickham's foundational **Split-Apply-Combine** paradigm. Students learn how to segment datasets into logical cohorts, compute multi-metric statistical summaries, write custom statistical aggregators, reshape summaries into multidimensional pivot tables, and present reports with grand totals and margins.

---

## Learning Outcomes
By completing this week's materials, you will be able to:
1. **Understand Split-Apply-Combine**: Segment DataFrames into distinct groups using `.groupby()`.
2. **Multi-Level Grouping**: Group across multiple categorical hierarchies and navigate resulting MultiIndex structures.
3. **Advanced Multi-Metric Summaries**: Apply `.agg()` with multiple functions, dictionary mappings, and named aggregations.
4. **Author Custom Aggregation Functions**: Implement domain-specific statistical measures (e.g. data range, IQR, pass rates).
5. **Construct Multi-Dimensional Pivot Tables**: Build cross-tabulated reports with `pd.pivot_table()`.
6. **Compute Margins & Subtotals**: Add row and column grand totals with `margins=True` and analyze frequency tables using `pd.crosstab()`.

---

## Topic Navigation

| Topic | Focus Area | Key Pandas Functions |
| :--- | :--- | :--- |
| [01. GroupBy Basics](01.GroupBy-Basics/) | Split-Apply-Combine mechanics, inspecting groups, basic statistics | `df.groupby()`, `.groups`, `.get_group()`, `.mean()`, `as_index` |
| [02. Multi-Level Grouping](02.Multi-Level-Grouping/) | Multi-key grouping, MultiIndex hierarchies, unstacking dimensions | `df.groupby(['A', 'B'])`, `.loc[]`, `.unstack()` |
| [03. Advanced Aggregation](03.Advanced-Aggregation/) | Multi-metric aggregation, dictionary column mappings, named aggregations | `.agg(['min', 'max'])`, `.agg({'Col': 'mean'})`, named tuples |
| [04. Custom Aggregation Functions](04.Custom-Aggregation-Functions/) | User-defined statistical functions, lambdas, range, IQR, pass rate | `def func(s): ...`, `.agg(func)` |
| [05. Pivot Tables](05.Pivot-Tables/) | 2D summary matrices, contrasting GroupBy with Pivot Tables, missing values | `pd.pivot_table()`, `index`, `columns`, `values`, `fill_value` |
| [06. Adding Margins and Totals](06.Adding-Margins-Totals/) | Grand totals, subtotals, contingency tables, normalisation | `margins=True`, `margins_name`, `pd.crosstab(normalize=...)` |

---

## Folder Structure

Each topic folder is structured consistently:
```text
Topic-Folder/
├── notebooks/       # Interactive Jupyter notebooks with step-by-step guidance & exercises
├── src/             # Clean, runnable Python scripts containing all demonstrations
├── docs/            # Conceptual summaries and syntax reference guides
├── Makefile         # Commands to run scripts or launch Jupyter Lab
├── README.md        # Topic-level learning objectives and instructions
└── QUICKSTART.md    # Step-by-step setup and execution guide
```

---

## Recommended Learning Flow
1. Work through the topics sequentially from `01` to `06`.
2. Run each script in `src/` to observe the full terminal output.
3. Open the corresponding notebook in `notebooks/` to work through the interactive explanations and solve the exercises.
