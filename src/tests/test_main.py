import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.main import Task, TaskManager
import pytest
from datetime import datetime, timedelta


#PANE
#Test tarea creada
@pytest.mark.parametrize("x, y, a, b", [
    ("Tarea 1", "Descripción", "A", "2023-12-31"),
])
def test_create_task(x, y, a, b):
    myTask = Task(x, y, a, b)
    assert myTask is not None
    assert myTask.nameTask == x
    assert myTask.description == y
    assert myTask.priority == a
    assert myTask.due_date == datetime.strptime(b, "%Y-%m-%d").date()
    assert myTask.completed == False


@pytest.mark.parametrize(
    # "x, y, a, b, expected_exception, expected_message", 
[
    ("", "Descripción2", "B", "2024-01-15", ValueError, "El nombre de la tarea no puede estar vacío"),
    ("Tarea 2", "Descripción2", "A", "24-01-15", ValueError, "Formato de fecha incorrecto, debe ser AAAA-MM-DD"),
])
def test_create_task_invalid(x, y, a, b, expected_exception, expected_message):
    with pytest.raises(expected_exception) as excinfo:
        myTask = Task(x, y, a, b)
    assert str(excinfo.value) == expected_message

#PAULA
#Test tarea completada
def test_complete_task():
    myTask = Task('Completed')
    myTask.complete()
    print(myTask.completed)
    assert myTask.completed == True

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


#Test de calcular cuanto le falta por vencer a las tareas de la lista
@pytest.mark.parametrize(
    "a, b, c, d, e, f, g, h, result",
    [
        (1, "Aprender Java", "B", "2024-06-15", 2, "Aprender JS", "B", "2024-06-10", ['Task: 1, Days before due date: 6', 'Task: 2, Days before due date: 1'])
    ]
)
def test_time_left_before_due(a, b, c, d, e, f, g, h, result):
    task1 = Task(a, b, c, d)
    task2 = Task(e, f, g, h)
    task_manager = TaskManager()
    task_manager.add_task(task1)
    task_manager.add_task(task2)
    print(task_manager.time_left_before_due())
    assert task_manager.time_left_before_due() == result

#GIULI
# Test para contar todas las tareas
def test_count_tasks():
    # Crea una instancia de TaskManager
    task_manager = TaskManager()

    # Añade tareas
    task1 = Task(1, "Aprender Python", "A", "2024-06-10")
    task2 = Task(2, "Aprender Java", "B", "2024-06-08")
    task_manager.add_task(task1)
    task_manager.add_task(task2)

    # Cuenta las tareas
    num_tasks = len(task_manager.tasks)
    print(f"Cantidad de tareas: {num_tasks}", flush=True)

    # Muestra detalles de cada tarea
    print("Detalles de las tareas:", flush=True)
    for task in task_manager.tasks:
        print(f"ID: {task.nameTask}, Descripción: {task.description}, Prioridad: {task.priority}, Fecha: {task.due_date}", flush=True)

#Para ordenar por la prioridad
def test_task_priority_order():
    # Crear instancia de TaskManager
    task_manager = TaskManager()

    # Crear instancias de Task con diferentes prioridades
    task4 = Task(4, "Cargar repositorio de proyecto Ing y Calidad", "A", "2024-06-7")
    task5 = Task(5, "Definir casos de uso", "B", "2024-05-21")
    task6 = Task(6, "Captura de requisitos", "C", "2024-05-20")

    # Añadir las tareas al TaskManager
    task_manager.add_task(task4)
    task_manager.add_task(task5)
    task_manager.add_task(task6)

    task_manager.complete_task(task4)


    # Obtener las tareas del TaskManager
    tasks = task_manager.tasks

    # Verificar que las tareas están ordenadas por prioridad
    print("-----------------------------------------", flush=True)

    print("Prioridad de las tareas:", flush=True)
    assert tasks[0].priority == "A"
    assert tasks[1].priority == "B"
    assert tasks[2].priority == "C"

    task_manager.get_tasks()

#TEST PARA CONTAR LAS TAREAS INCOMPLETAS
def test_count_incomplete_tasks():
    # Crear instancia de TaskManager
    task_manager = TaskManager()

    # Crear instancias de Task con diferentes prioridades
    task1 = Task(10, "Terminar front del proyecto 1", "A", "2024-06-7")
    task2 = Task(11, "Listar historias de usuario", "B", "2024-06-15")
    task3 = Task(12, "Elegir colorimetria", "C", "2024-06-21")

   # Añadir las tareas al TaskManager
    task_manager.add_task(task1)
    task_manager.add_task(task2)
    task_manager.add_task(task3)

    # Completar algunas tareas
    task_manager.complete_task(task1)

    # Contar las tareas incompletas
    incomplete_tasks = sum(1 for task in task_manager.tasks if not task.completed)

    # Imprimir tareas incompletas
    print("Tareas incompletas:")
    for task in task_manager.tasks:
        if not task.completed:
            print(f"ID: {task.nameTask}, Descripción: {task.description}, Prioridad: {task.priority}")

    assert incomplete_tasks == 2

if __name__ == "__main__":
    pytest.main()

#Sara
# Prueba para establecer una prioridad inválida
def test_invalid_priority():
    with pytest.raises(ValueError, match="La prioridad debe ser: A, B o C"):
        Task(7, "Tarea con prioridad inválida", "D", "2024-06-15")
    print("Prioridad inválida detectada correctamente.")
# Prueba para eliminar una tarea que no existe
def test_remove_nonexistent_task():
    task_manager = TaskManager()
    tarea = Task(3, "Tarea inexistente", "C", "2024-06-12")
    
    with pytest.raises(ValueError, match="Task no found"):
        task_manager.remove_task(tarea)
    print("No se puede eliminar tarea inexistente.")

def test_create_task_without_description():
    tarea = Task(1, None, "A", "2024-06-10")
    assert tarea.description is None
    print("Tarea creada sin descripción correctamente.")


if __name__ == "__main__":
    pytest.main()
    
