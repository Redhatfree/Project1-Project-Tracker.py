# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 01:13:27 2026

@author: Rouzbeh
"""

tasks = []

while True:
    print("\n1. Show tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        if not tasks:
            print("No tasks yet.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == "2":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "3":
        if not tasks:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            index = int(input("Enter task number to delete: ")) - 1
            if 0 <= index < len(tasks):
                tasks.pop(index)
                print("Task deleted!")
            else:
                print("Invalid number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
