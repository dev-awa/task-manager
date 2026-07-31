"""
Task Manager CLI - Main entry point
"""

import sys
import os


sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from cli.commands import add_task, list_tasks, complete_task, delete_task

def main():
    """Main function"""
    if len(sys.argv) < 2:
        print("""
Task Manager CLI

Commands:
    add <title> [description]   Add a new task
    list                        show all tasks
    complete <number>           Mark task as done
    delete <number>             Delete a task

Examples:
    python task_manager.py add "Buy milk"
    python task_manager.py list
    python task_manager.py complete 1
    python task_manager.py delete 2
""")
        return

    command = sys.argv[1].lower()
    
    if command == "add":
        if len(sys.argv) < 3:
            print("Please provide a title")
            return
        title = sys.argv[2]
        description = sys.argv[3] if len(sys.argv) > 3 else ""
        add_task(title, description)
    
    elif command == "list":
        list_tasks()
    
    # NEW: Complete command
    elif command == "complete":
        if len(sys.argv) < 3:
            print("Please provide a number: complete 1")
            return
        try:
            index = int(sys.argv[2])
            complete_task(index)
        except ValueError:
            print("Please provide a valid number")
    
    # NEW: Delete command
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Please provide a number: delete 1")
            return
        try:
            index = int(sys.argv[2])
            delete_task(index)
        except ValueError:
            print("Please provide a valid number")
    
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()