head = None  # Points to first node

def create_node(student_record):
    return {
        'data': student_record,
        'next': None
    }

def add_student_record(student_id, name, course_id, score):
    global head
    
    record = {
        'student_id': student_id,
        'name': name,
        'course_id': course_id,
        'score': score
    }
    
    new_node = create_node(record)
    
    new_node['next'] = head
    head = new_node

def display_all():
    if not head:
        print("No records found.")
        return
    
    current = head
    while current:
        s = current['data']
        print(f"{s['student_id']} | {s['name']} | {s['course_id']} | {s['score']}")
        current = current['next']

def delete_record(student_id, course_id):
    global head
    
    # If first node matches
    if head and head['data']['student_id'] == student_id and head['data']['course_id'] == course_id:
        head = head['next']
        print("Record deleted.")
        return
    
    current = head
    while current and current['next']:
        if (current['next']['data']['student_id'] == student_id and 
            current['next']['data']['course_id'] == course_id):
            current['next'] = current['next']['next']
            print("Record deleted.")
            return
        current = current['next']
    
    print("Record not found.")

def display_sorted():
    if not head:
        print("No records found.")
        return
    
    records = []
    current = head
    while current:
        records.append(current['data'])
        current = current['next']
    
    sorted_students = sorted(records, key=lambda x: (x['course_id'], -x['score']))
    for student in sorted_students:
        print(f"{student['student_id']} | {student['name']} | {student['course_id']} | {student['score']}")

def query_student(student_id):
    found = []
    
    current = head
    while current:
        if current['data']['student_id'] == student_id:
            found.append(current['data'])
        current = current['next']
    
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
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            course_id = input("Enter Course ID: ")
            score = float(input("Enter Score: "))
            add_student_record(student_id, name, course_id, score)
            print("Record added!\n")
            
        elif choice == '2':
            display_all()
            print()
            
        elif choice == '3':
            student_id = input("Enter Student ID: ")
            course_id = input("Enter Course ID: ")
            delete_record(student_id, course_id)
            print()
            
        elif choice == '4':
            display_sorted()
            print()
            
        elif choice == '5':
            student_id = input("Enter Student ID: ")
            query_student(student_id)
            print()
            
        elif choice == '0':
            print("Goodbye.")
            break
            
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
