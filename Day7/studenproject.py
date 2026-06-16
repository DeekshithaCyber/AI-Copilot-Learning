def menu():
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

def add_student():
    student_id = input("Enter ID: ")
    name = input("Enter Name: ")
    branch = input("Enter Branch: ")

    with open("students.txt", "a") as file:
        file.write(f"{student_id},{name},{branch}\n")

    print("Student Added Successfully")

def view_students():
    try:
        with open("students.txt", "r") as file:
            data = file.readlines()

            for line in data:
                print(line.strip())

    except FileNotFoundError:
        print("No student records found")

def search_student():
    search_id = input("Enter Student ID: ")

    with open("students.txt", "r") as file:
        for line in file:
            student = line.strip().split(",")

            if student[0] == search_id:
                print("Student Found")
                print("ID:", student[0])
                print("Name:", student[1])
                print("Branch:", student[2])
                return

    print("Student Not Found")

def delete_student():
    delete_id = input("Enter Student ID to delete: ")

    with open("students.txt", "r") as file:
        data = file.readlines()

    with open("students.txt", "w") as file:
        for line in data:
            student = line.strip().split(",")

            if student[0] != delete_id:
                file.write(line)

    print("Student Deleted Successfully")

while True:
    menu()

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid Choice")