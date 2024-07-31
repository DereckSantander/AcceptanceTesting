import json
import os
from datetime import datetime

# File to store tasks
TASKS_FILE = 'tasks.json'

def load_tasks():
    """Load tasks from the JSON file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(description, due_date):
    """Add a new task to the to-do list."""
    tasks = load_tasks()
    task_id = len(tasks) + 1
    task = {
        'ID': task_id,
        'Description': description,
        'Due Date': due_date,
        'Completed': False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {task}")

def list_tasks():
    """List all tasks in the to-do list."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        status = "Completed" if task['Completed'] else "Pending"
        print(f"ID: {task['ID']}, Description: {task['Description']}, Due Date: {task['Due Date']}, Status: {status}")

def mark_task_complete(task_id):
    """Mark a task as completed."""
    tasks = load_tasks()    for task in tasks:
        if task['ID'] == task_id:
            task['Completed'] = True
            save_tasks(tasks)
            print(f"Task {task_id} marked as completed.")
            return
    print(f"Task with ID {task_id} not found.")

def clear_tasks():
    """Clear all tasks from the to-do list."""
    save_tasks([])
    print("All tasks cleared.")

def find_task_by_description(description):
    """Find and display tasks by their description."""
    tasks = load_tasks()
    found = False
    for task in tasks:
        if description.lower() in task['Description'].lower():
            status = "Completed" if task['Completed'] else "Pending"
            print(f"ID: {task['ID']}, Description: {task['Description']}, Due Date: {task['Due Date']}, Status: {status}")
            found = True
    if not found:
        print("No tasks found with that description.")

def main():
    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task Complete")
        print("4. Clear Tasks")
        print("5. Find Task by Description")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Ingresa la descripción de la tarea: ")
            due_date = input("Ingresa el siguiente formato (YYYY-MM-DD): ")
            try:
                datetime.strptime(due_date, '%Y-%m-%d')
                add_task(description, due_date)
            except ValueError:
                print("Formato invalido. Por favor ingresar en el siguiente formato YYYY-MM-DD")
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            try:
                task_id = int(input("Ingrese el ID de la tarea que desea completar: "))
                mark_task_complete(task_id)
            except ValueError:
                print("ID de tarea inválido. Por favor ingrese un número.")
        elif choice == '4':
            clear_tasks()
        elif choice == '5':
            description = input("Ingresar la tarea que desea buscar: ")
            find_task_by_description(description)
        elif choice == '6':
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Por favor selecciona una opción válida.")

if __name__ == '__main__':
    main()
