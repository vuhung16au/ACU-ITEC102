# NumPy Built-in Functions (ufuncs)

# Import the NumPy library
import numpy as np

# Create a NumPy array of scores
scores = np.array([45, 92, 55, 30, 88])

# Use the `np.where()` function to assign 'Pass' or 'Fail' based on the scores
grades = np.where(scores >= 50, 'Pass', 'Fail')

# Print the final results
print(f"Final Results: {grades}")

# Expected Output: Final Results: ['Fail' 'Pass' 'Pass' 'Fail' 'Pass']

# TODO: Try np.min(), np.max(), np.mean(), np.median(), and np.std() on the scores array and print the results.
# print(f"Minimum score: {np.min(scores)}")
# print(f"Maximum score: {np.max(scores)}")
# print(f"Mean score: {np.mean(scores)}")
# print(f"Median score: {np.median(scores)}")
# print(f"Standard deviation: {np.std(scores)}")
c
# TODO: Use np.add(), np.subtract(), np.multiply(), and np.divide() on two arrays of your choice and print the results.
# arr1 = np.array([1, 2, 3, 4, 5])
# arr2 = np.array([6, 7, 8, 9, 10])
# print(f"Addition: {np.add(arr1, arr2)}")
# print(f"Subtraction: {np.subtract(arr1, arr2)}")
# print(f"Multiplication: {np.multiply(arr1, arr2)}")
# print(f"Division: {np.divide(arr1, arr2)}")
