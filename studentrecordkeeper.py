#Program Title : Student Record Keeper *: Write a Python program to create, update, and manipulate a dictionary of student records, including their grades and attendance.
#Name : Gaurav
#Roll No. : 19
#Branch : Electronics Engineering
#DOP : 19/02/2026       DOS : 26/02/2026

students = {}
while True:
    print("\nStudent Record Manager")
    print("1. Add Student")
    print("2. Update Student")
    print("3. View Records")
    print("4. Delete Student")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        attendance = input("Enter attendance (%): ")
        students[name] = {"Grade": grade, "Attendance": attendance}
        print("Student added successfully!")

    elif choice == 2:
        name = input("Enter student name to update: ")
        if name in students:
            grade = input("Enter new grade: ")
            attendance = input("Enter new attendance (%): ")
            students[name]["Grade"] = grade
            students[name]["Attendance"] = attendance
            print("Record updated successfully!")
        else:
            print("Student not found.")

    elif choice == 3:
        if not students:
            print("No student records available.")
        else:
            print("\nStudent Records:")
            for name, details in students.items():
                print("Name:", name,
                      "| Grade:", details["Grade"],
                      "| Attendance:", details["Attendance"], "%")

    elif choice == 4:
        name = input("Enter student name to delete: ")
        if name in students:
            del students[name]
            print("Student record deleted.")
        else:
            print("Student not found.")

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")