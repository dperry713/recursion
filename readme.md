# Task Scheduler

A Python-based task scheduling system that handles hierarchical tasks with priorities using recursive processing.

## Features

- Recursive task scheduling based on priority
- Support for nested subtasks
- Priority-based sorting at each level
- Flexible input structure (single task or task list)

## Usage

```python
from task import schedule_tasks

# Define your task hierarchy
tasks = [
    {
        'id': 1,
        'name': 'Main Task',
        'priority': 5,
        'subtasks': [
            {'id': 2, 'name': 'Subtask 1', 'priority': 1},
            {'id': 3, 'name': 'Subtask 2', 'priority': 4}
        ]
    }
]

# Schedule the tasks
scheduled_tasks = schedule_tasks(tasks)
