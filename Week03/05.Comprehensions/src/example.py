# Comprehensions: Pythonic Shortcuts

def main():
    # 1. List Comprehension (Extracting just the even numbers)
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    evens = [x for x in numbers if x % 2 == 0]
    print(f"Original numbers: {numbers}")
    print(f"Even numbers: {evens}")

    # 2. Dictionary Comprehension (Squaring numbers)
    squares_dict = {x: x**2 for x in range(1, 6)}
    print(f"Squares Dictionary: {squares_dict}")

if __name__ == "__main__":
    main()
