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

# Test 2: Create task with description
task2 = Task("Read book", "Finish chapter 3")
print(f"Task created: {task2.title}")
print(f"Description: {task2.description}")
print(f"Status: {task2.status}")

print("\nAll tests passed!")