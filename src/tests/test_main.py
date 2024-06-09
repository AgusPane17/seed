import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.main import Task, TaskManager
import pytest
from datetime import datetime, timedelta


#PANE
#Test tarea creada
def test_create_task():
    myTask = Task('Task1')
    print(myTask.nameTask)

if __name__ == "__main__":
    test_create_task()


#PAULA
#Test tarea completada
def test_complete_task():
    myTask = Task('Completed')
    myTask.complete()
    assert myTask.completed == True
    print(myTask.completed)

#Test tareas vencidas
def test_get_overdue_tasks():
    task_manager = TaskManager()

    #Obtener las fechas para calcular cuando esta vencida o no
    now = datetime.now()
    past_date = (now - timedelta(days=1)).strftime("%Y-%m-%d")
    future_date = (now + timedelta(days=1)).strftime("%Y-%m-%d")

    #Creo instancias de task, una vencida y otra no
    overdue_task = Task(1, "Aprender Python", "A", past_date)
    not_overdue_task = Task(2, "Aprender Java", "B", future_date)

    #Agrego las tareas al administrador
    task_manager.add_task(overdue_task)
    task_manager.add_task(not_overdue_task)

    #Obtengo las tareas vencidas
    overdue_tasks = task_manager.get_overdue_tasks()

    #verifica que esten en la lista correcta(vencida o no)
    assert overdue_task in overdue_tasks
    assert not_overdue_task not in overdue_tasks

    print("Overdue tasks:")
    for task in overdue_tasks:
        print(task)

if __name__ == "__main__":
    test_get_overdue_tasks()

#Test de calcular cuanto le falta por vencer a las tareas de la lista
@pytest.mark.parametrize(
    "a, b, c, d, e, f, g, h, result",
    [
        (1, "Aprender Java", "B", "2024-06-15", 2, "Aprender JS", "B", "2024-06-09", ['Task: 1, Days before due date: 7', 'Task: 2, Days before due date: 1'])
    ]
)
def test_time_left_before_due(a, b, c, d, e, f, g, h, result):
    task1 = Task(a, b, c, d)
    task2 = Task(e, f, g, h)
    task_manager = TaskManager()
    task_manager.add_task(task1)
    task_manager.add_task(task2)

    assert task_manager.time_left_before_due() == result



    