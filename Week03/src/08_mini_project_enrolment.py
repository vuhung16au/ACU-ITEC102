# 08_mini_project_enrolment.py
# Mini-Project: Building a Student Enrolment System

def main():
    print("--- Student Enrolment System ---")
    
    # Dictionary to store course enrolments (Course Code -> Set of Student IDs)
    courses = {
        "ITEC101": {"S001", "S002", "S003"},
        "ITEC102": {"S002", "S004", "S005"},
        "ITEC103": {"S001", "S003", "S005"}
    }
    
    # Dictionary to store student details
    students = {
        "S001": {"name": "Alice Smith", "major": "Computer Science"},
        "S002": {"name": "Bob Johnson", "major": "Information Technology"},
        "S003": {"name": "Charlie Brown", "major": "Computer Science"},
        "S004": {"name": "Diana Prince", "major": "Software Engineering"},
        "S005": {"name": "Evan Wright", "major": "Information Technology"}
    }
    
    # 1. View students enrolled in a specific course
    target_course = "ITEC102"
    print(f"\nStudents enrolled in {target_course}:")
    enrolled_ids = courses.get(target_course, set())
    for student_id in enrolled_ids:
        student_name = students[student_id]["name"]
        print(f"- {student_name} ({student_id})")
        
    # 2. Find students enrolled in BOTH ITEC101 and ITEC102 (Intersection)
    itec101_students = courses.get("ITEC101", set())
    itec102_students = courses.get("ITEC102", set())
    common_students = itec101_students.intersection(itec102_students)
    
    print("\nStudents taking both ITEC101 and ITEC102:")
    for student_id in common_students:
        print(f"- {students[student_id]['name']}")
        
    # 3. Add a new enrolment
    new_student_id = "S004"
    course_to_add = "ITEC101"
    if course_to_add in courses:
        courses[course_to_add].add(new_student_id)
        print(f"\nSuccessfully enrolled {students[new_student_id]['name']} into {course_to_add}.")
    
    # 4. Show updated ITEC101 enrolments
    print(f"\nUpdated students enrolled in {course_to_add}:")
    for student_id in courses[course_to_add]:
        print(f"- {students[student_id]['name']} ({student_id})")

if __name__ == "__main__":
    main()
