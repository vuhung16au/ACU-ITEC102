# Topic: Conditional Statements (if, elif, else)
# Conditional statements give our programs a brain.

def main():
    # Simulating a grading system
    score = 85

    if score >= 85:
        grade = "High Distinction"
        # print("Excellent work!")
        # print(f"Your grade is: {grade}")
    elif score >= 75:
        grade = "Distinction"
        # print("Good job!")
    elif score >= 65:
        grade = "Credit"
    elif score >= 50:
        grade = "Pass"
    else:
        grade = "Fail"

    print(f"Your grade is: {grade}")

    # Exercise 1 Solution:
    # color = input('Favorite color: ')
    # For automated execution, using a hardcoded value:
    color = "blue"
    if color.lower() == 'blue':
        print('The sky is blue')
        Z = color.upper()  # Converts the string to uppercase, but doesn't change the original variable
        # color.
        print(Z)
    else:
        print('Nice color!')


    # --- ENRICHMENT ---
    # Truthiness and Ternary Operators
    # Empty objects (like '', 0, [], None) evaluate to False. You can also write one-line if statements called Ternary Operators.
    # Truthiness
    user_input = ""
    if not user_input:
        print("No input provided!")

    # Ternary Operator
    score = 80
    result = "Pass" if score >= 50 else "Fail"
    print(f"Ternary result: {result}")

if __name__ == "__main__":
    main()
