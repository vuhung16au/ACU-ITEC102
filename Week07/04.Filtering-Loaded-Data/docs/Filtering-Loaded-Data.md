# Filtering Loaded Data in Pandas

Filtering allows you to extract precise subsets of rows that satisfy specific criteria.

---

## Key Concepts

### 1. Boolean Indexing
A boolean condition applied to a Series generates a mask of `True` and `False` values:
```python
mask = df["Temperature"] > 30.0
# Returns rows where mask is True
hot_days = df[mask]
```

### 2. Compound Conditions (`&`, `|`, `~`)
In Python, standard `and` and `or` evaluate truthiness of entire objects. In Pandas, element-wise evaluations require bitwise operators:
- `&`: Element-wise AND
- `|`: Element-wise OR
- `~`: Element-wise NOT (inversion)

> **Important:** Due to Python operator precedence, bitwise operators have higher priority than comparison operators (`>`, `<`). You **must** wrap each condition in parentheses:
> ```python
> # Correct:
> subset = df[(df["City"] == "Sydney") & (df["Rainfall"] > 0)]
>
> # Incorrect (Raises ValueError or incorrect evaluation):
> subset = df[df["City"] == "Sydney" & df["Rainfall"] > 0]
> ```

### 3. Categorical Membership (`.isin()`)
Checks whether values are contained within an iterable:
```python
# Include Sydney and Brisbane
capital_cities = df[df["City"].isin(["Sydney", "Brisbane"])]

# Exclude Melbourne
not_melbourne = df[~df["City"].isin(["Melbourne"])]
```

### 4. Expressive Queries with `df.query()`
Allows passing SQL-like conditions as strings without repeating the DataFrame name:
```python
clean_query = df.query("Temperature > 25 and City == 'Sydney'")
```
