tasks = []
print("Welcome to the To-Do List Application!")

while True:
    print("\n","Please choose an option:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. View tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")
# If user chooses to add a task
    if choice == "1":
        print("Your choice 1: ")
        task = input("Enter your addition task: ")
        tasks.append(task)
        print("Task added successfully!")
# If user chooses to remove a task
    elif choice == "2":
        print("your choice 2: ")
        if tasks:  # Check if the list is not empty  ## if task in tasks:
            task = input("Remove any value: ")
            tasks.pop()
            print("Task removed successfully!")
        else:
            print("No tasks to remove.") #########
# If user chooses to view tasks
    elif choice == "3":
        print("Your choice 3: ")
        for i, j in enumerate(tasks):  # Loop through tasks with index
            print(i, j)
# If user chooses to exit
    elif choice == "4":
        print("Your choice 4: ")
        print("Goodbye!")
        break

    else:
        print("Invalid choice")