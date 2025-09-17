students = []

def add_student_record(student_id, name, course_id, score):
    record = {
        'student_id': student_id,
        'name': name,
        'course_id': course_id,
        'score': score
    }
    
    # Insert in ascending order by student_id
    inserted = False
    for i, student in enumerate(students):
        if student['student_id'] > student_id:
            students.insert(i, record)
            inserted = True
            break
    if not inserted:
        students.append(record)

def display_all():
    if not students:
        print("No records found.")
        return
    for student in students:
        print(f"{student['student_id']} | {student['name']} | {student['course_id']} | {student['score']}")

def delete_record(student_id, course_id):
    for i, student in enumerate(students):
        if student['student_id'] == student_id and student['course_id'] == course_id:
            students.pop(i)
            print("Record deleted.")
            return
    print("Record not found.")

def display_sorted():
    if not students:
        print("No records found.")
        return
    # Sort by course_id, then by score descending
    sorted_students = sorted(students, key=lambda x: (x['course_id'], -x['score']))
    for student in sorted_students:
        print(f"{student['student_id']} | {student['name']} | {student['course_id']} | {student['score']}")

def query_student(student_id):
    found = [s for s in students if s['student_id'] == student_id]
    if not found:
        print("No records found for this student.")
        return
    for student in found:
        print(f"{student['name']} | {student['course_id']} | {student['score']}")


def printmenu():
    print("===== Student Grade Management System =====")
    print("1. Add student record")
    print("2. Display all records")
    print("3. Delete a record (by student ID and course ID)")
    print("4. Display records sorted by course ID and score (descending)")
    print("5. Query records by student ID")
    print("0. Exit\n")


def main():
    while True:
        printmenu()
        choice = input("Please select an option (0-5): ")
        
        if choice == '1':
            # Add student record
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            course_id = input("Enter Course ID: ")
            score = float(input("Enter Score: "))
            add_student_record(student_id, name, course_id, score)
            print("Record added!\n")
            
        elif choice == '2':
            # Display all records
            display_all()
            print()
            
        elif choice == '3':
            # Delete a record
            student_id = input("Enter Student ID: ")
            course_id = input("Enter Course ID: ")
            delete_record(student_id, course_id)
            print()
            
        elif choice == '4':
            # Display sorted records
            display_sorted()
            print()
            
        elif choice == '5':
            # Query student
            student_id = input("Enter Student ID: ")
            query_student(student_id)
            print()
            
        elif choice == '0':
            # Exit
            print("Goodbye.")
            break
            
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
