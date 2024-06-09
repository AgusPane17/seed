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
                print("Deleted task")
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
    
    #Metodo para definir las tareas vencidas
    def get_overdue_tasks(self):
        duetask = [task for task in self.tasks if task.is_overdue()]
        print(duetask)
        return duetask
    
   #Metodo para calcular cuanto le falta a una tarea por vencer
    def time_left_before_due(self):
        if self.tasks is []:
            return "No tasks in the task manager"
        
        days_left = []
        for task in self.tasks:  
            tasks_days_left = f"Task: {task.nameTask}, Days before due date: {task.time_left_before_due()}"
            days_left.append(tasks_days_left)
        return days_left
    
#Constructor de la clase task, se llama cuando se crea una instancia de task 
#inicializa todos los atributos de la tarea
class Task:
    def __init__(self, nameTask, description=None, priority=None, due_date=None):
        self.nameTask = nameTask
        self.description = description
        self.priority = priority
        if self.priority is not None and priority not in ['A', 'B', 'C']:
            raise ValueError ("La prioridad debe ser: A, B o C")
        if due_date is not None:  # Verificar si due_date se proporcionó
            self.due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
        else:
            self.due_date = None
        self.completed = False
        print('task create')

    def complete(self):
        self.completed = True
    
    #Define si la tarea esta vencida
    def is_overdue(self):
        if self.due_date and datetime.now().date() > self.due_date:
            return True
        return False
    
    #funcion para mostrar el objeto Task en el test
    def __repr__(self):
        return f"Task(nameTask= {self.nameTask}, description= {self.description}, priority= {self.priority}, due_date= {self.due_date}, completed= {self.completed})"

    #Metodo para calcular cuanto le falta por vencer a una tarea
    def time_left_before_due(self):
        if self.due_date is None:
            return "No due date set"
        now = datetime.now().date()
        time_left = self.due_date - now
        #Busco los dias de diferencia

        return f"{time_left.days}"




