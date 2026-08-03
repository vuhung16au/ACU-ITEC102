# Topic: Scalar Types & Type Conversion
# int, float, bool, str, bytes, and datetime.

def main():
    # Explicit Conversion (Casting)
    price_string = "45.50"
    # We cannot do math with text, so we convert it to a float
    price_float = float(price_string)
    total_with_tax = price_float * 1.10
    print(f"Total with tax: ${total_with_tax:.2f}")

    # Implicit Conversion
    # Python automatically converts an int and a float into a float
    a = 10      # int
    b = 2.5     # float
    result = a + b 
    print(f"Result type: {type(result)}") # Outputs <class 'float'>

    # Exercise 1 Solution:
    age_str = "30"
    future_age = int(age_str) + 5
    print(f"Future age: {future_age}")


    # --- ENRICHMENT ---
    # Complex Numbers and isinstance()
    # Python natively supports complex numbers (used in engineering and data science). Also, checking types should usually be done with isinstance() instead of type().
    # Complex numbers
    c = 3 + 4j
    print(f"Complex number: {c}, Real part: {c.real}, Imaginary: {c.imag}")

    # Best practice for type checking
    x = 10
    if isinstance(x, int):
        print("x is definitely an integer!")

if __name__ == "__main__":
    main()
