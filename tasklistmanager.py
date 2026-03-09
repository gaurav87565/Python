#Program Title : Task List Manager*: Develop a Python program to manage a task list using lists and tuples, including adding, removing, updating, and sorting tasks.
#Name : Gaurav
#Roll No. : 19
#Branch : Electronics Engineering
#DOP : 19/02/2026       DOS : 26/02/2026

tasks = []   # List to store tasks

while True:
    print("\nTask List Manager")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Update Task")
    print("4. View Tasks")
    print("5. Sort Tasks")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    # Add Task
    if choice == 1:
        task_name = input("Enter task name: ")
        priority = input("Enter priority (High/Medium/Low): ")
        task = (task_name, priority)   # Task stored as tuple
        tasks.append(task)
        print("Task added successfully!")

    # Remove Task
    elif choice == 2:
        task_name = input("Enter task name to remove: ")
        for task in tasks:
            if task[0] == task_name:
                tasks.remove(task)
                print("Task removed successfully!")
                break
        else:
            print("Task not found.")

    # Update Task
    elif choice == 3:
        task_name = input("Enter task name to update: ")
        for i in range(len(tasks)):
            if tasks[i][0] == task_name:
                new_name = input("Enter new task name: ")
                new_priority = input("Enter new priority: ")
                tasks[i] = (new_name, new_priority)
                print("Task updated successfully!")
                break
        else:
            print("Task not found.")

    # View Tasks
    elif choice == 4:
        if not tasks:
            print("No tasks available.")
        else:
            print("\nTask List:")
            for task in tasks:
                print("Task:", task[0], "| Priority:", task[1])

    # Sort Tasks
    elif choice == 5:
        tasks.sort()
        print("Tasks sorted successfully!")

    # Exit
    elif choice == 6:
        print("Exiting Task Manager...")
        break

    else:
        print("Invalid choice. Try again.")