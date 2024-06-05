class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            raise ValueError("Task not found")

    def complete_task(self, task):
        if task in self.tasks:
            task.complete()
        else:
            raise ValueError("Task not found")

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False
        print('task create')

    def complete(self):
        self.completed = True
