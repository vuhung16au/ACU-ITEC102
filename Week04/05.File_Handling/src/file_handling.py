"""File Handling in Python: Reading and Writing.

This script demonstrates writing (appending) to a file and safely reading
from it using the 'with' statement context manager and try-except error handling.
"""

# 1. Append mode ("a"): Appends text to the file, creating it if it doesn't exist
with open("cities.txt", "a") as file:
    file.write("Sydney\n")

# 2. Read mode ("r"): Safely opens the file to read its contents
try:
    with open("cities.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")
