import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.main import Task

#Test tarea creada
def test_create_task():
    myTask = Task('Task1')
    print(myTask.nameTag)

if __name__ == "__main__":
    test_create_task()

#Test tarea completada s
def test_complete_task():
    myTask = Task('Completed')
    myTask.complete()
    assert myTask.completed == True
    print(myTask.completed)


# if __name__ == "__main__": 
#     test_complete_task()