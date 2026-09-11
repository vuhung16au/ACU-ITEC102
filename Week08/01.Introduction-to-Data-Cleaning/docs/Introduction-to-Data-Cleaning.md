# Introduction to Data Cleaning in Pandas

Data cleaning is the process of detecting, diagnosing, and correcting corrupt, inaccurate, incomplete, or incorrectly formatted records in a dataset.

---

## The Cleaning Workflow
```text
Raw Data -> [ 1. Audit ] -> [ 2. Deduplicate ] -> [ 3. Handle Nulls ] -> [ 4. Type & Bound Check ] -> Clean Data
```

---

## Key Auditing Functions

| Method | What It Audits | Example |
|---|---|---|
| `df.shape` | Total rows and columns | `(100, 5)` |
| `df.info()` | Non-null counts and memory usage | Lists column names & dtypes |
| `df.isna().sum()` | Total missing entries per column | `Score: 15` |
| `df.duplicated().sum()` | Number of duplicate rows | `1` |
| `df.describe()` | Range and distribution of values | Reveals min/max outliers |

---

## Handling Inconsistencies

### Nullable Data Types
Prior to Pandas 1.0, integer columns with `NaN` had to be cast to `float64`. Use capital `'Int64'` to retain integer semantics while allowing missing values:
```python
df["Age"] = df["Age"].astype("Int64")
```

### Removing Duplicates
```python
# Check count
num_dupes = df.duplicated().sum()

# Drop rows where all columns match
df_clean = df.drop_duplicates()

# Drop rows based on primary key
df_clean = df.drop_duplicates(subset=["StudentID"])
```

### String Sanitisation
```python
# Trim whitespace and capitalize words
df["Name"] = df["Name"].str.strip().str.title()
```
