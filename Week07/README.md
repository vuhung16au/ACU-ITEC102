# Week 07: Data Input/Output (I/O) and Exploration with Pandas

Welcome to **Week 07** of **ITEC102**. This week focuses on the foundational skills required to ingest data from external files into Pandas DataFrames, explore and summarise that data, filter it to find answers, and cleanly export results for downstream reporting.

---

## Weekly Learning Objectives

By the end of this week, students will be able to:
1. **Load Tabular Data from CSV Files**: Use `pd.read_csv()` with parameters like `parse_dates`, `index_col`, `usecols`, and `nrows`.
2. **Inspect and Summarise Data**: Assess dimensions, column types, missing values, and descriptive statistics using `.head()`, `.info()`, `.describe()`, and `.value_counts()`.
3. **Ingest Multi-Format Data (Excel & JSON)**: Extract data from specific sheets in Microsoft Excel workbooks and parse structured JSON records.
4. **Filter and Slice DataFrames**: Apply single and compound boolean conditions (`&`, `|`), `.isin()`, string accessors, and `.query()`.
5. **Export DataFrames to Files**: Write clean datasets to CSV, Excel, and JSON formats, understanding why `index=False` is essential.
6. **Handle Missing Values Before Export**: Detect null values (`isna()`), evaluate dropping vs. filling (`dropna()` / `fillna()`), and validate data hygiene prior to exporting.

---

## Topic Structure

| # | Topic Folder | Focus Area | Key Functions | Sample Dataset |
|---|---|---|---|---|
| **01** | [`01.Reading-CSV-Files`](./01.Reading-CSV-Files/) | Importing CSVs into DataFrames | `pd.read_csv`, `parse_dates`, `usecols`, `index_col` | `sample_weather.csv` (Australian weather) |
| **02** | [`02.Exploring-and-Summarising-Data`](./02.Exploring-and-Summarising-Data/) | Structural and statistical data inspection | `.head()`, `.tail()`, `.info()`, `.describe()`, `.value_counts()` | `sample_weather.csv` |
| **03** | [`03.Reading-Excel-and-JSON-Files`](./03.Reading-Excel-and-JSON-Files/) | Reading Excel sheets and API JSON formats | `pd.read_excel`, `pd.ExcelFile`, `pd.read_json` | `energy_stats.xlsx`, `sydney_airbnb.json` |
| **04** | [`04.Filtering-Loaded-Data`](./04.Filtering-Loaded-Data/) | Conditional filtering and boolean indexing | `df[condition]`, `&`, `\|`, `.isin()`, `.query()` | `sample_weather.csv` |
| **05** | [`05.Writing-DataFrames-to-Files`](./05.Writing-DataFrames-to-Files/) | Saving DataFrames to disk safely | `df.to_csv(index=False)`, `df.to_excel`, `df.to_json` | `sample_weather.csv` -> exported subsets |
| **06** | [`06.Handling-Missing-Values-Before-Exporting`](./06.Handling-Missing-Values-Before-Exporting/) | Data hygiene, imputation, and validation | `df.isna()`, `df.dropna()`, `df.fillna()`, pre-export check | `sample_weather.csv` -> clean export |

---

## Folder Organization

Each topic folder follows a standard modular layout:
```text
Topic-Folder/
├── docs/             # Markdown guides detailing theoretical concepts
├── notebooks/        # Interactive Jupyter notebook (.ipynb) and sample data
├── src/              # Standalone, runnable Python script (.py)
├── Makefile          # Commands to run jupyter and clean caches
├── pyproject.toml    # Dependencies managed with uv
├── QUICKSTART.md     # Step-by-step setup and execution guide
└── README.md         # Topic overview and learning outcomes
```

---

## Getting Started

Refer to [QUICKSTART.md](./QUICKSTART.md) for full instructions on running the notebooks and scripts using `uv` and `make`.
