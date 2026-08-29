# Introduction to NumPy: What is it and why do we use it?

# Import the NumPy library
import numpy as np

# Create a NumPy array of raw marks
raw_marks = np.array([45, 38, 50, 22, 41])

# Calculate the percentages by multiplying the raw marks by 2
percentages = raw_marks * 2

# Print the final grades
print(f"Final Grades: {percentages}%")
# Expected Output: Final Grades: [90 76 100 44 82]%