# 01_lists.py
# Introduction to Core Python Data Structures
# Lists: Ordered and mutable sequences

def main():
    print("--- Lists ---")
    # Creating a list
    fruits = ["apple", "banana", "cherry"]

    print("-------------------")
    print(f"Original list: {fruits}")
    print("-------------------")
    print(fruits)

    # Accessing elements (Ordered)
    print(f"First fruit: {fruits[0]}")
    
    # Modifying elements (Mutable)
    fruits[1] = "blueberry"
    print(f"Modified list: {fruits}")
    
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
        print(f"{i}. {item}")

if __name__ == "__main__":
    main()
