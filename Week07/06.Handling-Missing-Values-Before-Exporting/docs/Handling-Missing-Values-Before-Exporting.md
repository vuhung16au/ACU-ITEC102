# Handling Missing Values Before Exporting in Pandas

Missing values are represented as `NaN` (Not a Number) for floating point numbers or `None` for generic Python objects.

---

## Key Concepts

### 1. Detecting Missing Values
```python
import pandas as pd

# Check each cell for null
df.isna()

# Count of nulls per column
df.isna().sum()

# Percentage of nulls per column
(df.isna().mean() * 100).round(2)
```

### 2. Strategy A: Dropping Missing Values (`df.dropna()`)
- **`df.dropna()`**: Removes any row with at least one missing value.
- **`df.dropna(how='all')`**: Only removes rows where *all* columns are null.
- **`df.dropna(subset=['Temperature'])`**: Removes rows only if `'Temperature'` is missing.

> **Caution:** Dropping rows reduces your sample size and may bias statistical findings if data is not missing completely at random.

### 3. Strategy B: Imputing Missing Values (`df.fillna()`)
- **Constant Value**: e.g. `df['Rainfall'].fillna(0.0)`.
- **Mean / Median**:
  ```python
  df["Temperature"] = df["Temperature"].fillna(df["Temperature"].median())
```
- **Forward Fill / Backward Fill**:
  ```python
  # Propagate previous valid observation forward
  df["Temperature"] = df["Temperature"].ffill()
```

### 4. Validation Before Export
Before calling `to_csv()` or `to_json()`, verify that all required columns are clean:
```python
assert df.isna().sum().sum() == 0, "Cleanliness check failed: NaN values remain!"
df.to_csv("clean_output.csv", index=False)
```
