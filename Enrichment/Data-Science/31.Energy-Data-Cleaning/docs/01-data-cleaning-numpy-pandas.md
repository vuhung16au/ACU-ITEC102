# Data Cleaning with Pandas & NumPy

Data cleaning is one of the most critical parts of the data science workflow. Real-world data is often messy, missing, or improperly formatted.

## 1. Handling Sentinels
Often, missing data isn't represented by an empty string, but by special "sentinel" strings like `"N/A"`, `"-"`, or `"None"`. If left unchanged, Pandas treats the entire column as `object` (text) rather than numeric, breaking mathematical functions like `.mean()` or `.sum()`.

You can catch these at ingestion:
```python
na_sentinels = ["N/A", "-", "None", ""]
df = pd.read_csv("data.csv", na_values=na_sentinels)
```

## 2. String Normalization
Categorical columns like "Brand" often suffer from leading/trailing whitespaces or inconsistent casing (e.g., "SAMSUNG" vs " Samsung"). This fragments what should be one group into many.
Vectorized string functions fix this quickly:
```python
df["Brand"] = df["Brand"].astype(str).str.strip().str.upper()
```

## 3. Safe Type Coercion
If a numeric column is stuck as an `object` because of a single dirty string (like `"Not Tested"`), you can forcefully coerce it back to a float, converting the unparseable strings into `NaN`:
```python
df["Height"] = pd.to_numeric(df["Height"], errors="coerce")
```

## 4. NumPy Conditional Logic
NumPy's `where` and `select` functions provide incredibly fast, vectorized conditional logic for feature engineering.
```python
import numpy as np

# A simple If-Else for creating flags
df["Valid"] = np.where(df["Height"] > 0, True, False)

# Multiple conditions for categorizations
conditions = [
    df["Star2009"] >= 4.0,
    df["Star2009"] >= 2.5,
    df["Star2009"] < 2.5
]
choices = ["High", "Medium", "Low"]
df["Tier"] = np.select(conditions, choices, default="Unrated")
```
