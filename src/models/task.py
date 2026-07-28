"""
Task model - define what a task model looks like
"""

from datetime import datetime   # NEW: Import datetime
class Task:
    """
    A simple task with title, status, and dates
    """
    
    def __init__(self, title, description=""):
        """
        Create a new task

        Args:
            title: Task title (required)
            description: Task description (optional)
        """
        # Store the task data
        self.title = title
        self.description = description
        self.status = "TODO"    # All tasks start as TODO

        # NEW: Add timestamps
        self.created_at = datetime.now()    # When task was created
        self.updated_at = datetime.now()    # When task was updated