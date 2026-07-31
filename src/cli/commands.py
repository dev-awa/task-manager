"""
CLI commands for the task manager
"""

import sys
import os

# Add src to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.task import Task
from services import file_service

def add_task(title, description=""):
    """Add a new task"""
    try:
        task = Task(title, description)
        file_service.add_task(task.to_dict())
        print(f"Task added: {title}")
    except ValueError as e:
        print(f"Error: {e}")

def list_tasks():
    """List all tasks"""
    tasks = file_service.get_all_tasks()

    if not tasks:
        print("No tasks found!")
        return

    print("\nYour Tasks:")
    print("-" * 50)
    
    for i, task in enumerate(tasks, 1):
        status_emoji = {
            "TODO": "desert watch",
            "DOING": "refresh",
            "DONE": "tick"
        }.get(task.get("status", "TODO"), "?")
        
        print(f"{i}. {status_emoji} {task['title']}")
        if task.get("description"):
            print(f"    {task['description']}")
        print(f"    Created: {task['created_at'][:10]}")
        print("-" * 50)

# NEW: Complete a task
def complete_task(index):
    """
    Mark a task as done
    
    Usage: python task_manager.py complete 2
    """
    # Get all tasks
    tasks = file_service.get_all_tasks()

    # Check if any tasks
    if not tasks:
        print("No tasks found")
        return
    
    # Validate index
    if index < 1 or index > len(tasks):
        print(f"Invalid number! Choose 1 to {len(tasks)}")
        return
    
    # Update the task
    task = tasks[index - 1]
    task["status"] = "DONE"

    # Save back
    file_service.save_tasks(tasks)
    print(f"Task completed: {task['title']}")

# NEW: Delete a task
def delete_task(index):
    """
    Delete a task
    
    Usage: python task_manager.py delete 2
    """
    # Get all tasks
    tasks = file_service.get_all_tasks()

    if not tasks:
        print("No tasks found!")
        return
    
    if index < 1 or index > len(tasks):
        print(f"Invalid number! Choose 1 to {len(tasks)}")
        return
    
    # Remove task
    deleted = tasks.pop(index - 1)
    file_service.save_tasks(tasks)
    print(f"Task deleted: {deleted['title']}")