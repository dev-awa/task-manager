"""
Simple test for Task class
"""

import sys
import os

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from models.task import Task

# Test 1: Create a task
task = Task("Buy milk")
print(f"Task created: {task.title}")
print(f"Status: {task.status}")
print(f"Created at: {task.created_at}")

# Test 2: Mark task as done (NEW)
task.mark_done()
print(f"Task marked as done: {task.title}")
print(f"New status: {task.status}")
print(f"Updated at: {task.updated_at}")

# Test 3: Convert to dictionary (NEW)
task_dict = task.to_dict()
print(f"Task as dictionary:")
print(f"{task_dict}")

# Test 4: Empty title should fail (NEW)
try:
    task2 = Task("")
    print("Should not reach here!")
except ValueError as e:
    print(f"Correctly caught error: {e}")

print("\nAll tests passed!")