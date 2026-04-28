# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 01:13:27 2026

@author: Rouzbeh
"""
import json 
import os
import random
FILE_NAME ="data.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    else:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

tasks = load_tasks()

while True:
    print("\n1. Show tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Pick a random task for me!") # <--- New line
    print("5. Exit") # <--- Changed from 4 to 5

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
    save_tasks(tasks)
    print("Task added!")

    elif choice == "3":
    if not tasks:
        print("No tasks to delete.")

    elif choice == "4": 
    if not tasks:
        print("You have no tasks to choose from!")
    else:
        # This is where we use the random skill
        random_task = random.choice(tasks)
        print(f"✨ You should work on: {random_task}")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        index = int(input("Enter task number to delete: ")) - 1

        if 0 <= index < len(tasks):
            tasks.pop(index)
            save_tasks(tasks)
            print("Task deleted!")
        else:
            print("Invalid number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
