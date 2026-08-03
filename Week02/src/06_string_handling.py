# Topic: String Handling Basics
# Slicing, formatting, and escape sequences.

def main():
    # String Slicing: string[start:stop]
    course_code = "ITEC102-Python"
    print("Unit prefix:", course_code[0:7]) # Output: ITEC102

    # Escape Sequences: \n for newline, \t for tab
    report = "Name:\tAlice\nGrade:\tHD\nStatus:\tPassed"
    print(report)

    # Exercise 1 Solution:
    title = 'Introduction to Data Science'
    word = title[16:20]
    print(f"Extracted word: {word}")


    # --- ENRICHMENT ---
    # Advanced f-String Formatting
    # f-strings can do math, format decimals, and even print variable names for debugging.
    # Advanced f-strings
    pi = 3.14159265
    print(f"Pi rounded to 2 decimals: {pi:.2f}")

    # Debugging feature (Python 3.8+)
    my_var = 100
    print(f"{my_var=}") # Prints my_var=100

if __name__ == "__main__":
    main()
