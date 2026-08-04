# Indexing and Slicing Arrays (1D and 2D)

## Key Concepts
- Use array[row, column] for 2D indexing.
- The comma in slicing separates rows and columns.

## Code Example
```python
import numpy as np

table = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
top_left = table[0, 0]
first_column = table[:, 0]
print(f"Top-left: {top_left}, First column: {first_column}")
```
