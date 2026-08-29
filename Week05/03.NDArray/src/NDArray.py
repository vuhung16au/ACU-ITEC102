# The ndarray: Understanding Shape and Data Types

# Import the NumPy library
import numpy as np

# Create a 2D NumPy array (matrix) with shape (3, 3)
table = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Print the shape and data type of the array
print(f"Shape: {table.shape}")

# Expected Output: Shape: (3, 3)

# Print the data type of the array
print(f"Data type: {table.dtype}")

# Expected Output: Data type: int64

# Print the `table`` to console
print(table)

# Expected Output:
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
