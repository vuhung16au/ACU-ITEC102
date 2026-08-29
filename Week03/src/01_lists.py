# 01_lists.py
# Introduction to Core Python Data Structures
# Lists: Ordered and mutable sequences

def main():
    print("--- Lists ---")

    # Creating a list
    fruits = ["apple", "banana", "cherry"]

    # A list of random numbers from 1 to 10 include 3 items 
    random_numbers = [5, 2, 8]

    # Try some operation on list, including indexing, slicing, appending, removing, and iterating
    print(f"Random numbers: {random_numbers}")
    print(random_numbers)

    print(f"First random number: {random_numbers[0]}")
    print(f"Last random number: {random_numbers[-1]}")
    print(f"Slice of random numbers: {random_numbers[1:3]}")

    # Print the last element for "random_numbers" using negative indexing
    print(f"Last random number (using negative indexing): {random_numbers[-1]}")

    print("-------------------")
    print(f"Original list: {fruits}")
    print("-------------------")
    print(fruits)

    # Accessing elements (Ordered)
    print(f"First fruit: {fruits[0]}")
    
    # Modifying elements (Mutable)
    fruits[1] = "blueberry"
    print(f"Modified list: {fruits}")


    # Delete the first element of the list fruits 
    del fruits[0]
    print(f"List after deleting first element: {fruits}")

    # Add new elements to the list fruits to the end of the list using append() method
    fruits.append("kiwi")
    print(f"List after adding a new element: {fruits}")

    # Adding and removing elements
    fruits.append("orange")
    fruits.remove("apple")
    print(f"List after adding and removing: {fruits}")

    print("\n--- Example: Amazon Shopping Cart ---")
    # Amazon manages customers' shopping carts using lists (or similar ordered structures)
    shopping_cart = []
    
    # Add items to cart
    shopping_cart.append("Wireless Mouse")
    shopping_cart.append("Mechanical Keyboard")
    shopping_cart.append("USB-C Cable")
    print(f"Cart after adding items: {shopping_cart}")
    
    # Customer changes their mind and removes an item
    shopping_cart.remove("Mechanical Keyboard")
    print(f"Cart after removing an item: {shopping_cart}")
    
    # View cart contents
    print("Items in your cart:")
    for i, item in enumerate(shopping_cart, 1):
        print(f"{i}.{item}")

if __name__ == "__main__":
    main()
