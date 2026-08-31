# Tuples: Ordered, Immutable Data


def main():
    # Creating a tuple
    student_record = ("Liam", 98765432, "Data Science Major")
    print(f"Full Student Record: {student_record}")

    # Accessing elements works exactly like lists (0-indexed)
    print(f"Student Name: {student_record[0]}")
    print(f"Student ID: {student_record[1]}")

    # Tuples are locked. The following would cause a TypeError:
    # student_record[1] = 11111111


if __name__ == "__main__":
    main()
