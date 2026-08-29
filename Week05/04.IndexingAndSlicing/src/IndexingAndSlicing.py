# Indexing and Slicing Arrays (1D and 2D)

# Import the NumPy library
import numpy as np

# Create a 2D NumPy array (matrix) with shape (3, 3)
table = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Print the array to console
print(table)

# Expected Output:
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]


# Print the top-left element
top_left = table[0, 0]
print(f"Top-left: {top_left}")
# Expected Output: Top-left: 1

# Print the first column
first_column = table[:, 0]
print(f"First column: {first_column}")

# Expected Output: Top-left: 1, First column: [1 4 7]

# Print the first row
first_row = table[0, :]
print(f"First row: {first_row}")

# Expected Output: First row: [1 2 3]

# Print the last row
last_row = table[-1, :]
print(f"Last row: {last_row}")

# Expected Output: Last row: [7 8 9]

# Print the last column
last_column = table[:, -1]
print(f"Last column: {last_column}")

# Expected Output: Last column: [3 6 9]
