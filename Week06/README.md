# Week 06: Data Analysis with Pandas

Welcome to Week 06 of ACU-ITEC102. This week introduces **Pandas**, the premier Python library for data manipulation and tabular analysis. Students learn how 1D **Series** and 2D **DataFrames** model real-world datasets, master label-based (`.loc[]`) vs position-based (`.iloc[]`) indexing, learn how to reindex and drop observations, and perform essential data transformations including filtering, arithmetic alignment, sorting, and ranking.

---

## Learning Outcomes
By completing this week's materials, you will be able to:
1. **Master the Pandas Series**: Create 1D labelled data structures, access values via index labels and integer positions, and understand automatic index alignment.
2. **Construct and Inspect DataFrames**: Build 2D tabular DataFrames from dictionaries and lists, and inspect table geometry using `.head()`, `.shape`, `.columns`, and `.info()`.
3. **Perform Precise Indexing and Selection**: Distinguish between label-based indexing (`.loc[]`) and position-based indexing (`.iloc[]`) for rows, columns, and sub-matrices.
4. **Reindex and Drop Observations**: Align data structures using `.reindex()` and remove unwanted rows or columns with `.drop(axis=0/1)`.
5. **Apply Data Manipulations**: Execute vectorized arithmetic operations, boolean conditional filtering, and column transformations.
6. **Sort and Rank Tabular Records**: Order DataFrames by index or column values with `.sort_values()` and compute relative standings with `.rank()`.

---

## Topic Navigation

| Topic | Focus Area | Key Pandas Functions |
| :--- | :--- | :--- |
| [01. Introduction and Series](01.Introduction_and_Series/) | 1D labelled data structure, Series creation, index labels, and indexing | `pd.Series()`, `.loc[]`, `.iloc[]`, `.index`, `.values` |
| [02. Pandas DataFrames](02.Pandas_DataFrames/) | 2D tabular data structure, column extraction, metadata inspection | `pd.DataFrame()`, `.head()`, `.describe()`, `.info()`, `.shape` |
| [03. Indexing and Selection](03.Indexing_and_Selection/) | Label indexing (`.loc`) vs integer position indexing (`.iloc`), multi-axis slicing | `df.loc['row', 'col']`, `df.iloc[0:5, 1:3]` |
| [04. Reindexing and Dropping](04.Reindexing_and_Dropping/) | Modifying row/column indices, dropping dimensions, handling missing entries | `df.reindex()`, `df.drop(columns=[...])`, `axis=0/1` |
| [05. Data Manipulation](05.Data_Manipulation/) | Boolean filtering, arithmetic alignment, sorting values/index, and ranking | `df[df['Col'] > val]`, `.sort_values()`, `.sort_index()`, `.rank()` |

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
1. Work through the topics sequentially from `01` to `05`.
2. Run each script in `src/` to observe the full terminal output.
3. Open the corresponding notebook in `notebooks/` to work through the interactive explanations and solve the exercises.
