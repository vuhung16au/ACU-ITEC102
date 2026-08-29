# 03_sets.py
# Sets: Unordered collections of unique items
# Hands-On Activity 6: Finding Common Items in Sets

def main():
    print("--- Sets ---")
    # Creating a set
    unique_numbers = {1, 2, 3, 3, 4, 4, 5}

    # Mixed type set
    mixed_set = {1, "apple", 3.14, (1, 2), True}
    print(f"Mixed set: {mixed_set}")

    # Notice that duplicates are automatically removed
    print(f"Unique numbers: {unique_numbers}")
    
    # Sets are unordered, so indexing doesn't work:
    # print(unique_numbers[0]) # This would raise a TypeError
    

    # Verify that the order in sets are not important 

    # First set 

    set1 = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5}
    set2 = {5, 4, 3, 2, 1}

    # Check if the two sets are equal
    print(f"Set1: {set1}")
    print(f"Set2: {set2}")

    # Error 
    # print(f"Are the two sets equal? {set1 = set2}")

    print(f"Are the two sets equal? {set1 == set2}")

    # print(f"Are the two sets equal? {set1 === set2}")

    # Adding and removing items
    unique_numbers.add(6)
    unique_numbers.remove(1)
    print(f"Modified set: {unique_numbers}")

    unique_numbers.discard(10)  # Discarding a non-existent item does not raise an error


    # Demonstrate evertying in Python is an object, including sets

    number1 = 1

    number1.as_integer_ratio()

    number2 = 1.1 

    number2.as_integer_ratio()

    print("\n--- Finding Common Items in Sets ---")
    # Suppose we have two lists of students enrolled in different courses
    math_students = {"Alice", "Bob", "Charlie", "David"}
    science_students = {"Charlie", "David", "Eve", "Frank"}
    
    print(f"Math students: {math_students}")
    print(f"Science students: {science_students}")
    
    # Intersection (Finding common items)
    common_students = math_students.intersection(science_students)
    # Alternatively: math_students & science_students
    print(f"Students in both Math and Science: {common_students}")
    
    # Union (All unique items from both sets)
    all_students = math_students.union(science_students)
    print(f"All students: {all_students}")
    
    # Difference (Items in one set but not the other)
    only_math = math_students.difference(science_students)
    print(f"Students only in Math: {only_math}")

if __name__ == "__main__":
    main()
