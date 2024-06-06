from datetime import datetime

# Constructor, inicializa una llamada vacia a "task" para almacenar tareas
class TaskManager:
    def __init__(self):
        self.tasks = []

#Método que toma una tarea como argumento y la añade a la lista tasks
    def add_task(self, task):
        self.tasks.append(task)

#Método que toma una tarea (task) como argumento e intenta eliminarla de la lista tasks.
    def remove_task(self, task):
        if task in self.tasks:
            if task.completed:
                self.tasks.remove(task)
            else:
                raise ValueError("Task incompleted")
        else:
            ValueError("Task no found")

#Metodo toma una tarea, si esta en la lista llama a complete para marcarla como completa, si no larga un mensaje de error
    def complete_task(self, task):
        if task in self.tasks:
            task.complete()
        else:
            raise ValueError("Task not found")
        
    #Metodo para mostrar las tareas de la lista, las enumera
    def get_tasks(self):
        for idx, task in enumerate(self.tasks, start=1):
            task_info = f"Task {idx}: {task.description}, Complete: {task.completed}"
            if hasattr(task, 'due_date'):
                task_info += f", Due date: {task.due_date}"
                print(task_info)

#Constructor de la clase task, se llama cuando se crea una instancia de task 
#inicializa todos los atributos de la tarea
class Task:
    def __init__(self, nameTag, description=None, priority=None, due_date=None):
        self.nameTag = nameTag
        self.description = description
        self.priority = priority
        if self.priority is not None and priority not in ['A', 'B', 'C']:
            raise ValueError ("La prioridad debe ser: A, B o C")
        if due_date is not None:  # Verificar si due_date se proporcionó
            self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        else:
            self.due_date = None
        self.completed = False
        print('task create')

    def complete(self):
        self.completed = True


#Crear instancia de TaskManager
task_manager = TaskManager()

# Crear instancias de Task
task1 = Task(1,"Aprender Python", "A", "2024-06-10")

task2 = Task(2, "Aprender Java", "B", "2024-06-08")

# Añadir la tarea al TaskManager
task_manager.add_task(task1)

task_manager.add_task(task2)

# Completar la tarea
task_manager.complete_task(task1)

#Marcar la tarea como completa
task1.complete()

#Traer la lista de tareas 
task_manager.get_tasks()


