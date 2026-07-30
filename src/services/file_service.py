"""
File service - handles saving and loading tasks
"""

import json
import os

# Name of the file where tasks are stored
TASKS_FILE = "tasks.json"

def save_tasks(tasks):
    """
    Save tasks a JSON file
    
    Args:
        tasks: List of task dictionaries
    """
    # Open file and write tasks as JSON
    with open(TASKS_FILE, 'w', encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)
    
    print(f"Saved {len(tasks)} tasks to {TASKS_FILE}")

def load_tasks():
    """
    Load tasks from JSON file
    
    Returns:
        List of task dictionaries, or empty list if file doesn't exist
    """
    # If file doesn't exist, return empty list
    if not os.path.exists(TASKS_FILE):
        print(f"No {TASKS_FILE} found, starting fresh")
        return []
    
    # Read and return tasks from file
    with open(TASKS_FILE, 'r', encoding="utf-8") as f:
        tasks = json.load(f)
    
    print(f"Loaded {len(tasks)} tasks from {TASKS_FILE}")
    return tasks