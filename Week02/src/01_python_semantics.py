# Topic: Python Semantics & Readability
# Indentation, variables, and comments.

def main():
    # Variables store data. We don't need to declare their type beforehand.
    student_name = "Alex"
    age = 21

    # Comments start with a hash symbol (#) and are ignored by the computer.
    # Indentation matters! Notice the 4 spaces inside the 'if' block:
    if age >= 18:
        print(f"{student_name} is allowed to vote.")
        print("This line is also inside the if block because it is indented.")
    print("This line is outside the if block and will always run.")

    # Exercise 1 Solution:
    temperature = 25
    if temperature > 20:
        print('It is warm')


    # --- ENRICHMENT ---
    # Type Hinting and PEP 8
    # While Python doesn't require type declarations, 'type hinting' is an advanced feature often used in modern Python to make code more readable and catch errors.
    # Type hinting example
    def greet(name: str) -> str:
        return f"Hello {name}"

    age: int = 21
    print(greet("Alice"))

if __name__ == "__main__":
    main()
