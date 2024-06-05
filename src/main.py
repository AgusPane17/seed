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
            self.tasks.remove(task)
        else:
            raise ValueError("Task not found")

#Metodo toma una tarea, si esta en la lista llama a complete para marcarla como completa, si no larga un mensaje de error
    def complete_task(self, task):
        if task in self.tasks:
            task.complete()
        else:
            raise ValueError("Task not found")
        
    #Metodo para mostrar las tareas de la lista, las enumera
    def get_tasks(self):
        for idx, task in enumerate(self.tasks, start=1):
            print(f"Task {idx}: {task.description}")

#Constructor de la clase task, se llama cuando se crea una instancia de task 
#inicializa la descripcion de la tarea
#inicializa completed como falso e imprime el mensaje de que fue creada la tarea
class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False
        print('task create')

    def complete(self):
        self.completed = True



#Crear instancia de TaskManager
task_manager = TaskManager()

# Crear una instancia de Task
task1 = Task("Aprender Python")

task2 = Task("Aprender Java")

# Añadir la tarea al TaskManager
task_manager.add_task(task1)

# Completar la tarea
task_manager.complete_task(task1)

#Traer la lista de tareas
task_manager.get_tasks()

#Marcar la tarea como completa
task1.complete()
