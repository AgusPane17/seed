from src.main import Task

def test_create_task():
    myTask = Task('Task1')
    print(myTask.description)