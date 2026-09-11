# Data Sampling in Pandas

Sampling allows you to extract manageable, representative subsets from massive datasets for rapid development, hypothesis testing, and machine learning partitioning.

---

## Key Sampling Methods

### 1. Simple Random Sampling
```python
import pandas as pd

# Sample fixed count
sample_n = df.sample(n=10, random_state=42)

# Sample proportion (e.g., 20%)
sample_frac = df.sample(frac=0.20, random_state=42)
```

### 2. The Role of `random_state`
Random number generators produce pseudo-random sequences. Passing a fixed integer `random_state=42`:
- Guarantees identical sample rows across different executions.
- Enables collaborative debugging and unit test determinism.

### 3. Sampling With vs. Without Replacement
- `replace=False` (default): A row cannot be selected more than once.
- `replace=True`: A row can be chosen multiple times. Used in bootstrapping and Monte Carlo simulations.

### 4. Stratified Sampling
When groups in your dataset have unequal sizes, purely random sampling can accidentally omit minority classes.
```python
# Sample 5 rows per Status group
stratified = df.groupby("Status").sample(n=5, random_state=42)
```
Guarantees equal or proportional representation across every demographic segment.
