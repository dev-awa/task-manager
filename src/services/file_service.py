"""
File service - handles saving and loading tasks
"""

import json
import os

TASKS_FILE = "tasks.json"

def save_tasks(tasks):

    """Save task to JSON file"""
    with open(TASKS_FILE, 'w', encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)
    
    print(f"Saved {len(tasks)} tasks to {TASKS_FILE}")

def load_tasks():
    """Load tasks from JSON file"""
    if not os.path.exists(TASKS_FILE):
        print(f"No {TASKS_FILE} found, starting fresh")
        return []
    
    with open(TASKS_FILE, 'r', encoding="utf-8") as f:
        tasks = json.load(f)
    print(f"Loaded {len(tasks)} tasks from {TASKS_FILE}")
    return tasks

# NEW: Add a task
def add_task(task_dict):
    """
    Add a new task to storage
    
    Args:
        task_dict: Task as dictionary
    """
    # Load existing tasks
    tasks = load_tasks()
    # Add new task
    tasks.append(task_dict)
    # Save back to file
    save_tasks(tasks)
    print(f"Added task: {task_dict['title']}")

# NEW: Get all tasks
def get_all_tasks():
    """Get all tasks from storage"""
    return load_tasks()

# NEW: Delete all tasks (for testing)
def clear_all_tasks():
    """Delete all tasks"""
    if os.path.exists(TASKS_FILE):
        os.remove(TASKS_FILE)
        print(f"Removed {TASKS_FILE}")