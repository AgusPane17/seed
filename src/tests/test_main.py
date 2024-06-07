import pytest
from src.main import Task, TaskManager

def test_create_task():
    myTask = Task('Task1', 'My task')
    print(myTask.nameTask)
    assert myTask.nameTask == 'Task1'


