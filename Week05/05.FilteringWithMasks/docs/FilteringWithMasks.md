# Filtering Data using NumPy Masks (Boolean Arrays)

## Key Concepts
- Boolean Masks are True/False arrays used to filter out unwanted data instantly.

## Code Example
```python
import numpy as np

ages = np.array([15, 22, 14, 30, 18, 12])
adult_mask = ages >= 18
adults = ages[adult_mask]
print(f"Adult ages only: {adults}")
```
