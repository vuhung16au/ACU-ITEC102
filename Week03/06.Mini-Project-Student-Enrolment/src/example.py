# Mini-Project: Building a Student Enrolment System

# We'll use a dictionary to act as our database.
# Keys are student IDs (immutable), Values are dictionaries of student details.
enrolment_db = {
    1001: {"name": "Alice", "courses": set(["Python", "Data Science"])},
    1002: {"name": "Bob", "courses": set(["Python"])},
}


def enrol_student(student_id, name, course):
    if student_id not in enrolment_db:
        # Create a new record using a dictionary
        enrolment_db[student_id] = {"name": name, "courses": set()}

    # Add course to the set (automatically ignores duplicates)
    enrolment_db[student_id]["courses"].add(course)
    print(f"{name} successfully enrolled in {course}.")


def drop_course(student_id, course):
    student = enrolment_db.get(student_id)
    if student:
        if course in student["courses"]:
            student["courses"].remove(course)
            print(f"Dropped {course} for {student['name']}.")
        else:
            print(f"{student['name']} is not enrolled in {course}.")
    else:
        print("Student ID not found.")


def main():
    # Enrol some students
    enrol_student(1003, "Charlie", "AI")

    # Attempt duplicate enrolment
    enrol_student(1001, "Alice", "Python")

    # Drop a course
    drop_course(1002, "Python")

    print("\n--- Final Database ---")
    for sid, data in enrolment_db.items():
        print(f"ID: {sid}, Name: {data['name']}, Courses: {list(data['courses'])}")


if __name__ == "__main__":
    main()
