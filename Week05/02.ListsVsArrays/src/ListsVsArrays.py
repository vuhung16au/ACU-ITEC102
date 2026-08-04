# Python Lists vs. NumPy Arrays: Speed and structure
import numpy as np

my_list = [10, 20, 30]
arr = np.array(my_list)
adjusted_arr = arr - 5
print(f"Adjusted: {adjusted_arr}")
