# Reading a CSV File in Pandas

A Comma-Separated Values (CSV) file is a plain-text format where each line corresponds to a data record, and each field within that record is separated by a comma (or another delimiter).

---

## Key Concepts

### 1. The `pd.read_csv()` Function
The standard entry point for loading CSVs in Pandas:
```python
import pandas as pd

df = pd.read_csv("sample_weather.csv")
```

### 2. Essential Parameters
| Parameter | Purpose | Example |
|---|---|---|
| `filepath_or_buffer` | Local path or web URL to the CSV file | `"data.csv"` or `"https://.../data.csv"` |
| `sep` or `delimiter` | Character used to separate fields (defaults to `,`) | `sep=';'` or `sep='\t'` |
| `parse_dates` | List of column names to parse into `datetime64` | `parse_dates=['Date']` |
| `index_col` | Column to use as the row labels of the DataFrame | `index_col='Date'` or `index_col=0` |
| `usecols` | Subset of columns to read (saves RAM) | `usecols=['City', 'Temperature']` |
| `nrows` | Number of rows to read from the beginning | `nrows=100` |
| `encoding` | Text encoding standard (e.g. `'utf-8'`, `'latin-1'`) | `encoding='utf-8'` |
| `na_values` | Additional strings to recognize as `NaN` | `na_values=['NA', 'missing', '-']` |

---

## Code Examples

### Loading Specific Columns with Datetime Parsing
```python
import pandas as pd

# Load weather dataset with parsed dates
df = pd.read_csv(
    "sample_weather.csv",
    usecols=["Date", "City", "Temperature"],
    parse_dates=["Date"],
    index_col="Date",
)

print(df.info())
print(df.head())
```

---

## Common Gotchas
1. **Dates loaded as strings (`object` dtype)**: Always check `df.dtypes`. If dates are stored as objects, date filtering and plotting will not work properly until parsed.
2. **Missing Header**: If the CSV lacks a header row, pass `header=None` and supply column names via `names=['Col1', 'Col2']`.
3. **Trailing Commas / Delimiter mismatches**: European CSVs often use semicolons (`;`) because commas represent decimal points. Use `sep=';'` in those cases.
