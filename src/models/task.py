"""
Task model - define what a task model looks like
"""

class Task:
    """
    A simple task with basic attributes
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
        self.status = "TODO" # All tasks start as TODO
