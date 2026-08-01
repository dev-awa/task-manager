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
    """List all tasks with better formatting"""
    tasks = file_service.get_all_tasks()

    if not tasks:
        print("No tasks found!")
        print("    Add one with: python task_manager.py add 'Buy milk'")
        return
    
    # Show task count
    total = len(tasks)
    done = sum(1 for t in tasks if t.get("status") == "DONE")
    print(f"\nYour Tasks ({done}/{total} completed)")
    print("=" * 60)
    
    for i, task in enumerate(tasks, 1):
        # Status with color/emoji
        status_map = {
            "TODO": "⏳ TODO",
            "DOING": "🔄 DOING",
            "DONE": "✅ DONE"
        }
        status = status_map.get(task.get("status", "TODO"), "? UNKNOWN")
        
        print(f"{i}. {task['title']}")
        print(f"    Status: {status}")

        if task.get("description"):
            print(f"    Description: {task['description']}")

        print(f" 📅 Created: {task['created_at'][:10]}")
        print("-" * 60)

def complete_task(index):
    """Mark a task as done"""
    tasks = file_service.get_all_tasks()

    if not tasks:
        print("No tasks found")
        return
    
    if index < 1 or index > len(tasks):
        print(f"Invalid number! Choose 1 to {len(tasks)}")
        return
    
    task = tasks[index - 1]
    
    # Don't complete already done tasks
    if task.get("status") == "DONE":
        print(f"Task already completed: {task['title']}")
        return
    
    task["status"] = "DONE"
    file_service.save_tasks(tasks)
    print(f"Task completed: {task['title']}")

def delete_task(index):
    """ Delete a task """
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

# Show help
def show_help():
    """Show all available commands"""
    print("""
Task Manager CLI - Help

COMMANDS:
    add <title> [description]   Add a new task
    list                        Show all tasks
    complete <number>           Mark task as done
    delete <number>             Delete a task
    help                        Show this help

EXAMPLES:
    python task_manager.py add "Buy milk"
    python task_manager.py add "Read book" "Finish chapter 3"
    python task_manager.py list
    python task_manager.py complete 2
    python task_manager.py delete 1

TIPS:
    - Task numbers come from the list command
    - Can't complete a task that's already done
    - All tasks are saved automatically to tasks.json
""")