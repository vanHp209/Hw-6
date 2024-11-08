class Task:
    def __init__(self, name, description, deadline, status=False):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.status = status

    def mark_completed(self):
        self.status = True

    def __str__(self):
        status_str = "виконано" if self.status else "не виконано"
        return f"Назва: {self.name}, Опис: {self.description}, Дедлайн: {self.deadline}, Стан: {status_str}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task_name):
        self.tasks = [task for task in self.tasks if task.name != task_name]

    def mark_task_completed(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.mark_completed()

    def display_tasks(self):
        for task in self.tasks:
            print(task)


manager = TaskManager()