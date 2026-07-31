"""
Task Manager CLI - Main entry point
"""

import sys
import os

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from cli.commands import add_task, list_tasks

def main():
    """
    Main function - handles command line arguments
    """
    # Show help if no command
    if len(sys.argv) < 2:
        print("""
Task Manager CLI

Commands:
    add <title> [description]   Add a new task
    list                        show all tasks

Examples:
    python task_manager.py add "Buy milk"
    python task_manager.py add "Read book" "Finish chapter 3"
    python task_manager.py list
""")
        return

    # Get command
    command = sys.argv[1].lower()
    
    # Handle commands
    if command == "add":
        if len(sys.argv) < 3:
            print("Please provide a title")
            return
        title = sys.argv[2]
        description = sys.argv[3] if len(sys.argv) > 3 else ""
        add_task(title, description)
    
    elif command == "list":
        list_tasks()
    
    else:
        print(f"Unknown command: {command}")
        print("Use: add or list")

if __name__ == "__main__":
    main()