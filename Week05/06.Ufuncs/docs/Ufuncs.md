# NumPy Built-in Functions (ufuncs)

## Key Concepts
- np.mean(), np.sum(), np.max(), np.min() are fast ufuncs.
- np.where() is a powerful function used to categorise data based on conditions.

## Code Example
```python
import numpy as np

scores = np.array([45, 92, 55, 30, 88])
grades = np.where(scores >= 50, 'Pass', 'Fail')
print(f"Final Results: {grades}")
```
