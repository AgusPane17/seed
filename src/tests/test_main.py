from src.main import Task
from datetime import datetime
import pytest

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
    assert myTask.due_date == datetime.strptime(b, "%Y-%m-%d")
    assert myTask.completed == False


@pytest.mark.parametrize(
    "x, y, a, b, expected_exception, expected_message", 
[
    ("", "Descripción2", "B", "2024-01-15", ValueError, "El nombre de la tarea no puede ser una cadena vacía."),
    ("Tarea 2", "Descripción2", "D", "2024-01-15", ValueError, "La prioridad debe ser: A, B o C"),
])
def test_create_task_invalid(x, y, a, b, expected_exception, expected_message):
    with pytest.raises(expected_exception) as excinfo:
        myTask = Task(x, y, a, b)
    assert str(excinfo.value) == expected_message


#PAULA
#Test tarea completada
#pytest para probrar la funcion con parametros
def test_complete_task():
    myTask = Task('Completed')
    myTask.complete()
    print(myTask.completed)
    assert myTask.completed == True



