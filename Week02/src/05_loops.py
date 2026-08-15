# Topic: Loops (for, while) and Loop Control
# Loops automate repetitive tasks.

def main():
    # Using a for loop with range()
    print("Countdown starting...")

    for i in range(5):
        print(i)

    print("------")        
    
    for i in range(5, 0, -1):
        print(i)
    print("Blastoff!")

    # Using a while loop with a 'break' statement
    coffee_cups_drunk = 0
    while True: # This is an infinite loop!
        coffee_cups_drunk += 1
        print(f"Drinking cup {coffee_cups_drunk}...")
        
        if coffee_cups_drunk == 3:
            print("Okay, I have had enough coffee. Stopping.")
            break # This forcefully exits the infinite loop

    # Exercise 1 Solution:
    print("Even numbers:")
    for i in range(2, 11, 2):
        print(i)


    # --- ENRICHMENT ---
    # List Comprehensions
    # Python developers often use list comprehensions to write loops in a single, highly optimized line of code.
    # Standard Loop
    squares = []
    for x in range(5):
        squares.append(x**2)

    # List Comprehension (Pythonic way)
    fast_squares = [x**2 for x in range(5)]
    print(f"List comprehension result: {fast_squares}")

if __name__ == "__main__":
    main()
