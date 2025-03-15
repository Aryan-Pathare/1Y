# Python program to manage student records (grades and attendance)

def display_students(records):
    if not records:
        print("No student records available.")
    else:
        print("\nStudent Records:")
        for name, details in records.items():
            print(f"{name}: Grade - {details['grade']}, Attendance - {details['attendance']}%")

def add_student(records):
    name = input("Enter student name: ")
    grade = input("Enter student grade: ")
    attendance = input("Enter student attendance percentage: ")
    records[name] = {"grade": grade, "attendance": attendance}
    print("Student record added successfully!")

def update_student(records):
    name = input("Enter student name to update: ")
    if name in records:
        grade = input("Enter new grade: ")
        attendance = input("Enter new attendance percentage: ")
        records[name] = {"grade": grade, "attendance": attendance}
        print("Student record updated successfully!")
    else:
        print("Student not found!")

def remove_student(records):
    name = input("Enter student name to remove: ")
    if name in records:
        del records[name]
        print("Student record removed successfully!")
    else:
        print("Student not found!")

# Main program loop
students = {}
while True:
    print("\nStudent Records Manager")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Remove Student")
    print("4. Display Students")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_student(students)
    elif choice == "2":
        update_student(students)
    elif choice == "3":
        remove_student(students)
    elif choice == "4":
        display_students(students)
    elif choice == "5":
        print("Exiting Student Records Manager. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
