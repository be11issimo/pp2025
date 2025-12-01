students = []   
courses = []    
marks = {}      

def input_number_of_students():
    n = int(input("Enter number of students: "))
    for _ in range(n):
        input_student_information()

def input_student_information():
    student_id = input("Student ID: ")
    name = input("Student Name: ")
    dob = input("Date of Birth (dd/mm/yyyy): ")

    student = {
        "id": student_id,
        "name": name,
        "dob": dob
    }

    students.append(student)

def input_number_of_courses():
    n = int(input("Enter number of courses: "))
    for _ in range(n):
        input_course_information()


def input_course_information():
    course_id = input("Course ID: ")
    name = input("Course Name: ")

    course = {
        "id": course_id,
        "name": name
    }

    courses.append(course)

def input_marks_for_course():
    course_id = input("Enter course ID to input marks: ")
    print(f"Entering marks for course {course_id}")

    for student in students:
        mark = float(input(f"Enter mark for {student['name']}: "))
        marks[(student["id"], course_id)] = mark

def list_students():
    print("\n--- Students ---")
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, DoB: {s['dob']}")

def list_courses():
    print("\n--- Courses ---")
    for c in courses:
        print(f"ID: {c['id']}, Name: {c['name']}")

def show_student_marks():
    course_id = input("Enter course ID to show marks: ")
    print(f"\nMarks for course {course_id}:")
    for s in students:
        key = (s["id"], course_id)
        mark = marks.get(key, "N/A")
        print(f"{s['name']}: {mark}")

def main():
    while True:
        print("\n===== Student Mark Management =====")
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks for a course")
        print("4. List students")
        print("5. List courses")
        print("6. Show student marks in a course")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            input_number_of_students()
        elif choice == "2":
            input_number_of_courses()
        elif choice == "3":
            input_marks_for_course()
        elif choice == "4":
            list_students()
        elif choice == "5":
            list_courses()
        elif choice == "6":
            show_student_marks()
        elif choice == "0":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()