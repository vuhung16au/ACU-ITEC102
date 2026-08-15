# Topic: Arithmetic, Comparison, and Logical Operators
# Operators allow us to manipulate and compare data.

def main():
    # Modulus is incredibly useful for finding even/odd numbers
    number = 14
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
    
    # Logical Operators
    is_weekend = True
    is_sunny = False

    if is_weekend and is_sunny:
        print("Let's go to Bondi Beach!")
    elif is_weekend and not is_sunny:
        print("Let's stay indoors and code in Python.")

    # Exercise 1 Solution:
    num = 25
    if num % 2 == 1:
        print('Odd')


    # --- ENRICHMENT ---
    # The Walrus Operator (:=)
    # Introduced in Python 3.8, the walrus operator allows you to assign and evaluate a variable in a single expression.
    # Walrus operator example
    sample_data = [1, 2, 3, 4, 5]
    # Assigns n and evaluates if n > 3 simultaneously
    if (n := len(sample_data)) > 3:
        print(f"List is long enough, it has {n} elements.")

if __name__ == "__main__":
    main()
