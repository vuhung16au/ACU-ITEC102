# Dictionaries: Key-Value Pairs

def main():
    # Creating a dictionary for a student
    student_grades = {
        "Farshid": 85,
        "Alice": 92,
        "Bob": 78
    }
    print(f"Initial dictionary: {student_grades}")

    # Accessing data via the Key
    print(f"Alice's grade is: {student_grades['Alice']}")

    # Adding a new key-value pair
    student_grades["Charlie"] = 99
    print(f"Updated dictionary: {student_grades}")
    
    # Safely accessing a missing key
    missing_grade = student_grades.get("David", "Not Found")
    print(f"David's grade: {missing_grade}")

if __name__ == "__main__":
    main()
