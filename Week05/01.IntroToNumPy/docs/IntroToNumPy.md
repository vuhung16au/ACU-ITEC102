# Introduction to NumPy: What is it and why do we use it?

## Key Concepts
- NumPy provides the ndarray, which only stores one type of data but is highly optimised for numerical operations.
- Vectorisation allows you to perform mathematics on entire arrays at once without writing loops.

## Code Example
```python
import numpy as np

raw_marks = np.array([45, 38, 50, 22, 41])
percentages = raw_marks * 2
print(f"Final Grades: {percentages}%")
```
