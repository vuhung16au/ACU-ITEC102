# Exploring and Summarising Data in Pandas

Exploratory Data Analysis (EDA) is the practice of investigating datasets to discover patterns, spot anomalies, test hypotheses, and verify assumptions using summary statistics and graphical representations.

---

## Key Concepts

### 1. Structural Inspection
- **`df.head(n=5)`**: Returns the first `n` rows. Essential for quick sanity checks after ingestion.
- **`df.tail(n=5)`**: Returns the last `n` rows. Useful to verify that file loading didn't truncate early.
- **`df.shape`**: Tuple indicating `(number_of_rows, number_of_columns)`.
- **`df.columns`**: Index of column header names.
- **`df.dtypes`**: Series showing the data type of each column.

### 2. Comprehensive Profiling: `df.info()`
Provides a compact summary including:
- Index range and entry count.
- Each column name, its count of non-null values, and its data type.
- Total memory usage in bytes.

### 3. Summary Statistics: `df.describe()`
For numerical columns, `.describe()` computes:
- `count`: Number of non-missing values.
- `mean`: Arithmetic average.
- `std`: Standard deviation (spread of data).
- `min`, `25%`, `50%` (median), `75%`, `max`.

To summarize categorical data as well, use:
```python
df.describe(include="all")
```

### 4. Categorical Frequency Analysis: `df['col'].value_counts()`
Counts occurrences of each distinct value in a column. Great for checking category balance.

### 5. Extreme Values Lookup: `.idxmax()` / `.idxmin()`
Returns the row index where the maximum (or minimum) value occurs:
```python
highest_temp_idx = df["Temperature"].idxmax()
record = df.loc[highest_temp_idx]
```
