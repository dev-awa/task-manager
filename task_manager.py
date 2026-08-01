"""
Task Manager CLI - Main entry point
"""

import sys
import os


sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from cli.commands import add_task, list_tasks, complete_task, delete_task, show_help

def main():
    """Main function"""
    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1].lower()
    
    if command == "add":
        if len(sys.argv) < 3:
            print("Please provide a title")
            print("    Example: python task_manager.py add 'Buy milk'")
            return
        title = sys.argv[2]
        description = sys.argv[3] if len(sys.argv) > 3 else ""
        add_task(title, description)
    
    elif command == "list":
        list_tasks()
    
    elif command == "complete":
        if len(sys.argv) < 3:
            print("Please provide a task number")
            print("    Example: python task_manager.py complete 2")
            return
        try:
            index = int(sys.argv[2])
            complete_task(index)
        except ValueError:
            print("Please provide a valid number")
    
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Please provide a task number")
            print("    Example: python task_manager.py delete 1")
            return
        try:
            index = int(sys.argv[2])
            delete_task(index)
        except ValueError:
            print("Please provide a valid number")
    
    elif command == "help":
        show_help()
    
    else:
        print(f"Unknown command: {command}")
        print("    Type 'help' to see available commands")

if __name__ == "__main__":
    main()