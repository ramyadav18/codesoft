tasks = []

def display_menu():
    print("\n--- To-Do List Application ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Update task")
    print("4. Delete task")
    print("5. Exit")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("\n--- Tasks ---")
        for index, task in enumerate(tasks):
            print(f"{index+1}. {task}")

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully.")

def update_task():
    view_tasks()
    task_index = int(input("Enter the task number to update: "))
    if 1 <= task_index <= len(tasks):
        new_task = input("Enter new task: ")
        tasks[task_index-1] = new_task
        print("Task updated successfully.")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    task_index = int(input("Enter the task number to delete: "))
    if 1 <= task_index <= len(tasks):
        del tasks[task_index-1]
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")

def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Thank you for using the To-Do List Application!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
