def schedule_tasks(task_hierarchy):
    """
    Schedules tasks recursively based on priority and dependencies.

    Args:
        task_hierarchy (list of dict): List of tasks, each having potential subtasks.

    Returns:
        list: A flat list of tasks in the scheduled order.
    """
    def recursive_schedule(tasks):
        scheduled = []
        # Sort tasks by priority (higher priority first), default priority is 0
        tasks.sort(key=lambda x: x.get('priority', 0), reverse=True)
        
        for task in tasks:
            # Add the current task
            scheduled.append({'id': task['id'], 'name': task['name'], 'priority': task.get('priority', 0)})
            # Recursively process subtasks
            if 'subtasks' in task and task['subtasks']:
                scheduled.extend(recursive_schedule(task['subtasks']))
        
        return scheduled

    # If task_hierarchy is a dictionary (root node), convert to list for consistency
    if isinstance(task_hierarchy, dict):
        task_hierarchy = [task_hierarchy]
    
    # Call the recursive scheduler
    return recursive_schedule(task_hierarchy)

# Example Usage
if __name__ == "__main__":
    # Sample task hierarchy
    tasks = [
        {
            'id': 1,
            'name': 'Task 1',
            'priority': 2,
            'subtasks': [
                {'id': 2, 'name': 'Task 1.1', 'priority': 1},
                {'id': 3, 'name': 'Task 1.2', 'priority': 3},
            ]
        },
        {
            'id': 4,
            'name': 'Task 2',
            'priority': 1,
            'subtasks': [
                {'id': 5, 'name': 'Task 2.1', 'priority': 2},
                {'id': 6, 'name': 'Task 2.2'}
            ]
        }
    ]

    # Schedule tasks
    scheduled_tasks = schedule_tasks(tasks)
    print("Scheduled Tasks:")
    for task in scheduled_tasks:
        print(task)
