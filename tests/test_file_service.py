"""
Test file service
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from models.task import Task
from services import file_service

# Clear existing tasks
file_service.clear_all_tasks()

# Test 1: Add a task
print("Test 1: Add a task")
task = Task("Buy milk", "From supermarket")
file_service.add_task(task.to_dict())

# Test 2: Get all tasks
print("\nTest 2: Get all tasks")
tasks = file_service.get_all_tasks()
print(f"Found {len(tasks)} tasks")
for task in tasks:
    print(f"    - {task['title']} ({task['status']})")

# Test 3: Add another task
print("\nTest 3: Add another task")
task2 = Task("Read book", "Finish chapter 3")
file_service.add_task(task2.to_dict())

# Test 4: Get all tasks again
print("\nTest 4: Get all tasks again")
tasks = file_service.get_all_tasks()
print(f"Found {len(tasks)} tasks")
for task in tasks:
    print(f"    - {task['title']}")

print("\nAll tests passed!")