import datetime

from modelsLayer.Task import  Task
from helpers.Enum_state import Enum_state
from helpers.Enum_is_deleted import Enum_is_delete
from helpers.Loggin_configuration import loggin_run
from Config import Config
import sqlite3
from dataLayer.ConnectionSqlite import Connectionsqlite

class ManagerTableTasks(Connectionsqlite):
    #el CRUD a la base de datos de la tabla TASK
    # def __init__(cls, name_db="dbTasksList2025"):
    # llamar al archivo de config.
    __con = Config()

    def add_task(cls, task):
        help_task = task
        result = False
        try:
            slq_sentence = (f"INSERT INTO tasks (id, description, state, is_delete,date_create,date_update,date_delete  ) "
                            f"VALUES (NULL, '{help_task.description}', {help_task.state.value}, {help_task.is_delete.value},"
                            f"'{help_task.date_create}','{help_task.date_update}','{help_task.date_delete}');")
            cls.connect()
            last_id = cls.execute_insert(slq_sentence)
            loggin_run(2, f"Agrego el registro con el id {last_id}")
            cls.close()
            result = True
            return result
        except sqlite3.OperationalError as error:
            print("Error: ", error)
            loggin_run(4, error)
            cls.close()
            return result

    def create_task(cls,  description:str="nueva tarea",state: Enum_state= Enum_state.PENDIENTE ):
        result = False
        try:
            date_create = datetime.date
            date_update = datetime.date(1900,1,1)
            date_delete = datetime.date(1900, 1, 1)
            sql_sentence = (f"INSERT INTO tasks (id, description, state, is_delete,date_create,date_update,date_delete  ) "
                            f"VALUES (NULL, '{description}', {state.value}, False,"
                            f"'{date_create}','{date_update}','{date_delete}');")
            cls.connect()
            last_id = cls.execute_insert(sql_sentence)
            loggin_run(2, f"Agrego el registro con el id {last_id}")
            cls.close()
            result = True
            return result
        except sqlite3.OperationalError as error:
            print("Error: ", error)
            loggin_run(4, error)
            cls.close()
            return result

    def update_task(cls, task):
        result = False
        try:
            sql_sentence = (
                f"UPDATE tasks SET description='{task.description}', state={task.state}, "
                f"is_delete={task.is_delete.value}, date_create='{task.date_create}',"
                f"date_update='{task.date_update}', date_delete= '{task.date_delete}'  "
                f"WHERE id = {task.id};")
            cls.connect()
            last_id = cls.execute_update(sql_sentence)
            cls.close()
            loggin_run(2, f"Actualizado el registro con el id {last_id}")
            result = True
            return result
        except sqlite3.OperationalError as error:
            print("Error: ", error)
            cls.close()
            loggin_run(4, error)
            return result

    def physical_delete_task(cls, id):
        result = False
        try:
            sql_sentence = (f"delete from task where id = {id}")
            cls.connect()
            cls.execute_delete(sql_sentence, id)
            cls.close()
            loggin_run(2, f"El registro con id {id} fue eliminado fisicamente")
            result = True
            return result
        except sqlite3.OperationalError as error:
            print("Error: ", error)
            cls.close()
            loggin_run(4, error)
            return result

    def logical_delete_task(cls, id):
        result = False
        try:
            sql_sentence = ("UPDATE tasks SET is_delete={de} WHERE id = {i};".format(de= True,i=id))
            cls.connect()
            cls.execute_delete(sql_sentence, id)
            cls.close()
            loggin_run(2, f"Borrado logicamente el registro con el id {id}")
            result = True
            return result
        except sqlite3.OperationalError as error:
            print("Error: ", error)
            cls.close()
            loggin_run(4, error)
            return result

    def find_task(cls, id):
        try:
            sql_sentence = f"select * from tasks where id = {id} and is_delete = 0"
            cls.connect()
            task_list = cls.find_task(sql_sentence)
            cls.close()
            taskf = Task()
            task_len = len(task_list)
            if task_len == 1:
                for task in task_list:
                    taskf = Task(task[0], task[1])
                    if (task[2] == 1):
                        taskf.state = Enum_state.PENDIENTE
                    elif (task[2] == 2):
                        taskf.state = Enum_state.EN_PROCESO
                    else:
                        taskf.state = Enum_state.TERMINADO
                    # taskf.state = task[2]
                    taskf.is_delete = Enum_is_delete.FALSE
                    if (task[3] == 1):
                        taskf.is_delete = Enum_is_delete.TRUE
                    # taskf.is_delete = task[3]
                    taskf.date_create = task[4]
                    taskf.date_update = task[5]
                    taskf.date_delete = task[6]
            loggin_run(2, f"listado de tareas")
            return taskf
        except sqlite3.OperationalError as error:
            print("Error: ", error)
            cls.close()
            loggin_run(4, error)

    def list_tasks(cls):
        try:
            sql_sentence = f"select * from tasks where is_delete = 0"
            cls.connect()
            list_task_database = cls.read(sql_sentence)
            cls.close()
            list = []

            for task in list_task_database:
                taskf = Task(task[0], task[1])
                taskf.id = task[0]
                taskf.state = task[2]
                taskf.is_delete = task[3]
                taskf.date_create = task[4]
                taskf.date_update = task[5]
                taskf.date_delete = task[6]
                # print(t)
                list.append(taskf)
            cls.close()
            loggin_run(2, f"Lista de tareas de tamaño {len(list)} fue de vuelta de la base de datos")
            return list
        except sqlite3.OperationalError as error:
            print("Error: ", error)
            loggin_run(4, error)
            list = -1
            return list