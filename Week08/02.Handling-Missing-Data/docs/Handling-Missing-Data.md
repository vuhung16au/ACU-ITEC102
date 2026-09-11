# Handling Missing Data in Pandas

When data collection fails or survey questions are left unanswered, Pandas records entries as `NaN` (Not a Number) or `None`.

---

## The Dropping Strategies

### 1. Default Dropping (`how='any'`)
```python
# Drops any row with 1 or more missing values
df_clean = df.dropna()
```
- **Pros:** Fast and guarantees 100% complete records.
- **Cons:** High risk of discarding too much data and introducing sample bias.

### 2. Full-Row Dropping (`how='all'`)
```python
# Drops row ONLY if every column is NaN
df_clean = df.dropna(how="all")
```

### 3. Targeted Dropping (`subset=[...]`)
```python
# Drops row only if critical analysis column is missing
df_clean = df.dropna(subset=["Score"])
```
- **Pros:** Retains secondary columns that might still be useful for other analyses.

### 4. Threshold Dropping (`thresh=k`)
```python
# Keeps rows that have at least k non-null values
df_clean = df.dropna(thresh=4)
```

---

## Measuring Data Loss
Always compute data loss before committing to a dropping strategy:
```python
loss_pct = (len(df) - len(df_clean)) / len(df) * 100
print(f"Data loss: {loss_pct:.1f}%")
```
If data loss exceeds 5-10%, investigate **imputation** (statistical filling) instead of outright deletion.
