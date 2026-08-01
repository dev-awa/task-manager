"""
Task model - define what a task model looks like
"""

from datetime import datetime
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
        # Validate title is not empty
        if not title:
            raise ValueError("Title cannot be empty")
        
        # Store the task data
        self.title = title
        self.description = description
        self.status = "TODO"    # All tasks start as TODO
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    # Mark task as done
    def mark_done(self):
        """Mark task as done"""
        self.status = "DONE"
        self.updated_at = datetime.now()    # Update the timestamp
    
    # Convert to dictionary
    def to_dict(self):
        """Convert task to dictionary for saving"""
        return {
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at.isoformat(),      # Convert to string
            "updated_at": self.updated_at.isoformat()
        }
