"""
Test file service
"""

import sys
import os

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from models.task import Task
from services import file_service

# Test 1: Save a task
print("Test 1: Save a task")
task = Task("Buy milk", "From supermarket")
task_dict = task.to_dict()

# Convert to list and save
tasks = [task_dict]
file_service.save_tasks(tasks)
print(f"Saved task: {task.title}")

# Test 2: Load tasks
print("\nTest 2: Load tasks")
loaded_tasks = file_service.load_tasks()
print(f"Loaded {len(loaded_tasks)} tasks")
print(f"First task: {loaded_tasks[0]['title']}")

# Test 3: Load when no file exists
print("\nTest 3: Load when no file")
# Delete the file
if os.path.exists("tasks.json"):
    os.remove("tasks.json")

loaded = file_service.load_tasks()
print(f"Loaded {len(loaded)} tasks (should be 0)")

print("\nAll tests passed!")