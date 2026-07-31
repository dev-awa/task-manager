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
    """
    Add a new task
    
    Usage: python task_manager.py add "Buy milk"
    """
    try:
        # Create task
        task = Task(title, description)
        # Save to file
        file_service.add_task(task.to_dict())
        print(f"Task added: {title}")
    except ValueError as e:
        print(f"Error: {e}")

def list_tasks():
    """
    List all tasks
    
    Usage tasks task_manager.py list
    """
    # Get tasks from file
    tasks = file_service.get_all_tasks()

    # Check if any tasks exist
    if not tasks:
        print("No tasks found!")
        return

    # Display tasks
    print("\nYour Tasks:")
    print("-" * 50)
    
    for i, task in enumerate(tasks, 1):
        # Show status with emoji
        status_emoji = {
            "TODO": "desert watch",
            "DOING": "refresh",
            "DONE": "tick"
        }.get(task.get("status", "TODO"), "?")
        print(f"{i}. {status_emoji} {task['title']}")
        
        # Show description if exists
        if task.get("description"):
            print(f"    {task['description']}")
        
        # Show created date (first 10 characters = YYYY-MM-DD)
        print(f"    Created: {task['created_at'][:10]}")
        print("-" * 50)