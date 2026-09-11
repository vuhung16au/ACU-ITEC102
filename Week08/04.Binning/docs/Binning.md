# Data Binning (Discretisation) in Pandas

Binning transforms continuous numbers into discrete categories, simplifying analysis and reducing the impact of minor observation errors.

---

## `pd.cut()` vs `pd.qcut()`

| Feature | `pd.cut()` | `pd.qcut()` |
|---|---|---|
| **Binning Basis** | Values and numerical width | Frequencies and quantiles |
| **Bin Widths** | Can be equal or custom defined | Variable widths depending on data density |
| **Row Count per Bin** | Varies depending on data distribution | Approximately equal in every bin |
| **Typical Use Case** | Fixed grading cutoffs, age brackets | Quartiles, deciles, balanced demographic splits |

---

## Code Patterns

### 1. Custom Binning with `pd.cut()`
```python
import pandas as pd

bins = [0, 50, 65, 75, 85, 100]
labels = ["Fail", "Pass", "Credit", "Distinction", "High Distinction"]

df["Grade"] = pd.cut(df["Score"], bins=bins, labels=labels, right=False)
```

### 2. Equal-Frequency Binning with `pd.qcut()`
```python
# Discretize into 4 quartiles
df["Quartile"] = pd.qcut(df["Score"], q=4, labels=["Q1", "Q2", "Q3", "Q4"])
```
