from modelsLayer.Task import Task
from dataLayer.ManagerTableTasks import ManagerTableTasks
from helpers.Enum_state import Enum_state
from helpers.Enum_is_deleted import Enum_is_delete
import datetime

class TaskController:

    def __init__(cls, manager_connection = ManagerTableTasks()):
        cls.__control_db = manager_connection
        cls.__load__dic_tasks()

    def list_tasks(cls):
        return cls.__control_db.list_tasks()

    def __load__dic_tasks(cls):
        cls.dic_tasks = {i: value for i, value in enumerate(cls.__control_db.list_tasks())}
        return  cls.dic_tasks

    def dictionary_tasks(cls):
        return cls.dic_tasks

    def add_task(cls,description:str="nueva tarea"):
        id=0
        my_new_task = Task(id, description)
        my_new_task.state = Enum_state.PENDIENTE
        my_new_task.is_delete = Enum_is_delete.FALSE
        my_new_task.date_create = datetime.date.today()
        my_new_task.date_update = datetime.date(1900, 1, 1)
        my_new_task.date_delete = datetime.date(1900, 1, 1)
        result = cls.__control_db.add_task(my_new_task)
        return  result

    def update_task(cls, task):
        value = False
        id = task['id']
        # Check if key exists and update
        for item in cls.__control_db.list_tasks():
            if id == str(item.id):
                item.date_update = datetime.datetime.now()
                item.description = task['description']
                item.state = task['state']
                result = cls.__control_db.update_task(item)
                value = result
                return value
        return None

    def update_state(cls, id: int=0, new_state: Enum_state =Enum_state.PENDIENTE):
        value = False
        if isinstance(new_state, Enum_state):
            # Check if key exists and update
            if cls.dic_tasks.get(id) is not None:
                task = cls.dic_tasks[id]
                if id in cls.dic_tasks:
                    task.date_update = datetime.datetime.now()
                    task.state = new_state
                    cls.dic_tasks[id] = task  # Directly update the value
                    result = cls.__control_db.update_task(task)
                    value = True
        return value


    def delete_task_phisical(cls, id):
        value =False
        if cls.__tasks_internal.get(id) is not None:
           del cls.__tasks_internal[id]
           value = True
        return value

    def delete_task_logical(cls, id):
        value = False
        # Check if key exists and update
        for task in cls.__control_db.list_tasks():
            if id == str(task.id):
                task.is_delete = True
                task.date_delete = datetime.datetime.now()
                result = cls.__control_db.update_task(task)
                value = result
                return value
        return None

    def search_task_by_id(cls, id):
        task = None
        if cls.dic_tasks.get(id) is not None:
            task = cls.dic_tasks[id]
        return task









