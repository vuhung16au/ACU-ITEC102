# NumPy Built-in Functions (ufuncs)
import numpy as np

scores = np.array([45, 92, 55, 30, 88])
grades = np.where(scores >= 50, 'Pass', 'Fail')
print(f"Final Results: {grades}")
