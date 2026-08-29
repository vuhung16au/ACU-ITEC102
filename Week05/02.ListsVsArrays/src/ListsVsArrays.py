# Python Lists vs. NumPy Arrays: Speed and structure

# Import the NumPy library
import numpy as np

# Create a Python list of numbers
my_list = [10, 20, 30]

# Convert the list to a NumPy array
arr = np.array(my_list)

# Perform element-wise operations on the NumPy array
# For example, adding 5 to each element
adjusted_arr = arr - 5

# Print the adjusted array
print(f"Adjusted: {adjusted_arr}")
