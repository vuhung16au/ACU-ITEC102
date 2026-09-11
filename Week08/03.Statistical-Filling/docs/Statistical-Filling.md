# Statistical Filling (Imputation) in Pandas

Imputation replaces missing values with estimated surrogates, preserving the overall sample size and enabling complete analyses.

---

## Central Tendency Decision Matrix

| Strategy | When to Use | Pandas Syntax |
|---|---|---|
| **Mean** | Continuous data with symmetric, normal distribution and no heavy outliers | `df['Score'].fillna(df['Score'].mean())` |
| **Median** | Continuous or discrete numerical data with skewness or extreme outliers | `df['Age'].fillna(df['Age'].median())` |
| **Mode** | Categorical, boolean, or discrete codes | `df['Status'].fillna(df['Status'].mode()[0])` |
| **Group Mean** | Values that depend strongly on subgroup categories | `df.groupby('Status')['Score'].transform(lambda g: g.fillna(g.mean()))` |

---

## Group-Specific Imputation
Global averages often obscure real differences between cohorts. For instance, passing students average higher scores than failing students:

```python
# Impute Score conditionally based on Status
df["Score"] = df.groupby("Status")["Score"].transform(
    lambda grp: grp.fillna(grp.mean())
)
```

---

## Verifying Integrity
Always check `df.describe()` before and after imputation:
- Did the standard deviation drop dramatically?
- Did the minimum or maximum change inappropriately?
- Are zero missing values remaining?
