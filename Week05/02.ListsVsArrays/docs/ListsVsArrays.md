# Python Lists vs. NumPy Arrays: Speed and structure

## Key Concepts
- Python lists can hold mixed data types, but are slow for math.
- NumPy arrays only hold one data type, but they are built for blistering speed.

## Code Example
```python
import numpy as np

my_list = [10, 20, 30]
arr = np.array(my_list)
adjusted_arr = arr - 5
print(f"Adjusted: {adjusted_arr}")
```
