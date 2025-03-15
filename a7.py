tasks = []

while True:
    print("\nTask List Manager")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Display Tasks")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == "2":
        if tasks:
            print("\nTask List:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            index = int(input("Enter task number to remove: ") or -1) - 1
            if 0 <= index < len(tasks):
                print(f"Removed: {tasks.pop(index)}")
            else:
                print("Invalid number!")
        else:
            print("No tasks to remove.")
    elif choice == "3":
        if tasks:
            print("\nTask List:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks available.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")
