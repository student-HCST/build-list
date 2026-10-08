tasks = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append({"task": task, "done": False})
        print("Task added!")

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            for i, task in enumerate(tasks, 1):
                status = "✓" if task["done"] else " "
                print(f"{i}. [{status}] {task['task']}")

    elif choice == "3":
        if not tasks:
            print("No tasks to mark as done.")
        else:
            number = int(input("Enter task number: "))
            if 1 <= number <= len(tasks):
                tasks[number - 1]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        if not tasks:
            print("No tasks to delete.")
        else:
            number = int(input("Enter task number: "))
            if 1 <= number <= len(tasks):
                deleted = tasks.pop(number - 1)
                print(f"Deleted: {deleted['task']}")
            else:
                print("Invalid task number.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")

