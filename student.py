def add_student(student_data):
    name = input("Enter student name: ")
    grade = input("Enter student grade: ")
    student_data[name] = grade
    print(f"Added {name} with grade {grade}.")

def search_student(student_data):
    name = input("Enter student name to search: ")
    grade = student_data.get(name)
    if grade:
        print(f"{name}'s grade is {grade}.")
    else:
        print(f"No record found for {name}.")

def update_student(student_data):
    name = input("Enter student name to update: ")
    if name in student_data:
        new_grade = input(f"Enter new grade for {name}: ")
        student_data[name] = new_grade
        print(f"Updated {name}'s grade to {new_grade}.")
    else:
        print(f"No record found for {name}.")

def delete_student(student_data):
    name = input("Enter student name to delete: ")
    if name in student_data:
        del student_data[name]
        print(f"Deleted record for {name}.")
    else:
        print(f"No record found for {name}.")

def main():
    student_data = {}
    while True:
        action = input("Do you want to add, search, update, delete or exit? ").lower()
        if action == 'add':
            add_student(student_data)
        elif action == 'search':
            search_student(student_data)
        elif action == 'update':
            update_student(student_data)
        elif action == 'delete':
            delete_student(student_data)
        elif action == 'exit':
            break
        else:
            print("Invalid action. Please choose add, search, update, delete, or exit.")

if __name__ == "__main__":
    main()