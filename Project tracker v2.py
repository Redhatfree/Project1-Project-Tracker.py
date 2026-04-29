# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 01:13:27 2026

@author: Rouzbeh
"""
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 01:13:27 2026
@author: Rouzbeh
"""
import json 
import os
import random

FILE_NAME = "data.json"

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
    print("\n--- TASK MANAGER ---")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Pick a random task")
    print("5. Exit")
    print("6. Search for a task")

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
            print("\n[!] No tasks to delete.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            
            try:
                val = input("\nEnter task number to delete: ")
                index = int(val) - 1
                
                if 0 <= index < len(tasks):
                    deleted = tasks.pop(index)
                    save_tasks(tasks)
                    print(f"[✓] Deleted: {deleted}")
                else:
                    print("[!] That number isn't on the list.")
            except ValueError:
                print("[!] Error: Please enter a number, not text.")

    elif choice == "4": 
        if not tasks:
            print("You have no tasks to choose from!")
        else:
            random_task = random.choice(tasks)
            print(f"✨ You should work on: {random_task}")

    elif choice == "5":
        print("Goodbye!")
        break

    elif choice == "6":
        query = input("Search for: ").lower() # Fixed the syntax here
        found = False
        for task in tasks:
            if query in task.lower():
                print(f"-> Found: {task}")
                found = True
        if not found:
            print("No matching tasks found.")

    else:
        print("Invalid choice, please try again.")
