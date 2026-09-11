# Writing DataFrames to Files in Pandas

Exporting DataFrames allows clean, transformed datasets to be saved for reporting, machine learning training, or sharing across systems.

---

## Key Concepts

### 1. Writing to CSV (`df.to_csv`)
The most common output method:
```python
df.to_csv("clean_data.csv", index=False)
```

#### Why `index=False` is Critical
By default, `to_csv()` saves the integer index as the first column without a header:
```text
,Date,City,Temperature
0,2026-01-01,Sydney,28.5
```
When someone opens this file later with `pd.read_csv()`, Pandas assigns `Unnamed: 0` to that column. Repeating this cycle creates multiple useless `Unnamed` columns! Always pass `index=False` unless the index contains named, meaningful labels.

#### Useful `to_csv()` Parameters
- `sep`: Delimiter character (e.g. `sep=','` or `sep='\t'`).
- `float_format`: Formatting numbers (e.g. `float_format='%.2f'`).
- `columns`: Subset of columns to write (e.g. `columns=['City', 'Temperature']`).
- `compression`: Compression algorithm (e.g. `'gzip'`, `'zip'`).

---

### 2. Writing to JSON (`df.to_json`)
JSON is ideal when feeding web APIs or frontend dashboards:
```python
df.to_json("output.json", orient="records", date_format="iso", indent=2)
```
- `orient='records'`: Creates a list of JSON objects `[{"col1": val1, "col2": val2}, ...]`.
- `date_format='iso'`: Outputs standard ISO-8601 timestamps (`2026-01-01T00:00:00.000Z`).

---

### 3. Writing to Excel (`df.to_excel`)
Outputs formatted spreadsheets:
```python
df.to_excel("report.xlsx", sheet_name="Summary", index=False)
```
Requires the `openpyxl` engine.
