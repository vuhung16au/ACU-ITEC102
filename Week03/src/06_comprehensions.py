# 06_comprehensions.py
# Comprehensions: Powerful shortcuts for generating Lists, Sets, and Dictionaries

def main():
    print("--- Comprehensions ---")

    print("\n1. List Comprehension:")
    # Traditional way to create a list of squares
    squares_loop = []
    for x in range(1, 6):
        squares_loop.append(x**2)
    print(f"Squares (traditional loop): {squares_loop}")
    
    # Using a list comprehension
    squares_comp = [x**2 for x in range(1, 6)]
    print(f"Squares (list comprehension): {squares_comp}")
    
    # List comprehension with a condition (even squares)
    even_squares = [x**2 for x in range(1, 6) if x % 2 == 0]
    print(f"Even squares: {even_squares}")

    print("\n2. Set Comprehension:")
    # Generating a set of unique characters from a string
    word = "hello"
    unique_chars = {char for char in word}
    print(f"Unique characters in '{word}': {unique_chars}")

    print("\n3. Dictionary Comprehension:")
    # Creating a dictionary of numbers and their cubes
    cubes_dict = {x: x**3 for x in range(1, 4)}
    print(f"Cubes dictionary: {cubes_dict}")
    
    # Example: Reversing keys and values in a dictionary
    original_dict = {'a': 1, 'b': 2, 'c': 3}
    reversed_dict = {value: key for key, value in original_dict.items()}
    print(f"Original dictionary: {original_dict}")
    print(f"Reversed dictionary: {reversed_dict}")

if __name__ == "__main__":
    main()
