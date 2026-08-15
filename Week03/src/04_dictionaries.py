# 04_dictionaries.py
# Dictionaries: Unordered key-value pairs

def main():
    print("--- Dictionaries ---")
    # Creating a dictionary
    student = {
        "name": "Alice",
        "age": 20,
        "major": "Computer Science"
    }
    print(f"Student info: {student}")
    
    # Accessing and modifying values via keys
    print(f"Student's name: {student['name']}")
    student["age"] = 21
    student["gpa"] = 3.8 # Adding a new key-value pair
    print(f"Updated student info: {student}")

    print("\n--- Example: Look up for a phone number in a phonebook ---")
    # A phonebook is a classic example of a dictionary
    phonebook = {
        "Alice": "555-1234",
        "Bob": "555-5678",
        "Charlie": "555-9012"
    }
    
    # Looking up a phone number
    search_name = "Bob"
    if search_name in phonebook:
        print(f"{search_name}'s phone number is {phonebook[search_name]}")
    else:
        print(f"{search_name} is not in the phonebook.")
        
    # Using the get() method to avoid KeyError
    search_name = "David"
    number = phonebook.get(search_name, "Number not found")
    print(f"{search_name}'s phone number: {number}")
    
    # Iterating over a dictionary
    print("\nFull Phonebook:")
    for name, phone in phonebook.items():
        print(f"{name}: {phone}")

if __name__ == "__main__":
    main()
