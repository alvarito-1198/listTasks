import unittest
import datetime
from unittest.mock import MagicMock, patch

from Config import Config
from data_layer.ManagerTableTasks import ManagerTableTasks
from models_layer.Task import Task
from helpers.Enum_state import Enum_state
from helpers.Enum_is_deleted import Enum_is_delete
from controllerslayer.TaskController import TaskController

class Test_task_controller(unittest.TestCase):

    __con = Config()

    def setUp(cls):
        pass

    @patch('sqlite3.connect')
    def test_list_tasks(cls, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        cls.__name_database = cls.__con.read_value("sqlite", "test_name_db")
        # Definimos el valor que debe devolver fetchall
        mock_cursor.fetchall.return_value = [
            (1, "aprender python", Enum_state.PENDIENTE, Enum_is_delete.FALSE, "", "", ""),
            (2, "aprender java", Enum_state.PENDIENTE, Enum_is_delete.FALSE, "", "", "")
        ]

        cls.db = ManagerTableTasks(cls.__name_database)
        cls.controller = TaskController(cls.db)
        list =  cls.controller.list_tasks()
        count = len(list)
        cls.assertEqual(count, 2)

    @patch('sqlite3.connect')
    def test_diccionary_tasks(cls, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        cls.__name_database = cls.__con.read_value("sqlite", "test_name_db")
        # Definimos el valor que debe devolver fetchall
        mock_cursor.fetchall.return_value = [
            (1, "aprender python", Enum_state.PENDIENTE, Enum_is_delete.FALSE, "", "", ""),
            (2, "aprender java", Enum_state.PENDIENTE, Enum_is_delete.FALSE, "", "", "")
        ]

        cls.db = ManagerTableTasks(cls.__name_database)
        cls.controller = TaskController(cls.db)
        diccionary = cls.controller.dictionary_tasks()
        count = len(diccionary)
        cls.assertEqual(count, 2)

    @patch('sqlite3.connect')
    def test_add_task(cls, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        cls.__name_database = cls.__con.read_value("sqlite", "test_name_db")
        # Definimos el valor que debe devolver fetchall
        mock_cursor.fetchall.return_value = [
            (1, "aprender python", Enum_state.PENDIENTE, Enum_is_delete.FALSE, "", "", ""),
            (2, "aprender java", Enum_state.PENDIENTE, Enum_is_delete.FALSE, "", "", "")
        ]

        cls.db = ManagerTableTasks(cls.__name_database)
        cls.controller = TaskController(cls.db)
        result = cls.controller.add_task("nueva tarea desde controlador")
        cls.assertEqual(result, True)

    @patch('sqlite3.connect')
    def test_update_task(cls, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        cls.__name_database = cls.__con.read_value("sqlite", "test_name_db")
        # Definimos el valor que debe devolver fetchall
        mock_cursor.fetchall.return_value = [
            (1, "aprender python", Enum_state.PENDIENTE, Enum_is_delete.FALSE, "", "", ""),
            (2, "aprender java", Enum_state.PENDIENTE, Enum_is_delete.FALSE, "", "", "")
        ]
        cls.db = ManagerTableTasks(cls.__name_database)
        cls.controller = TaskController(cls.db)
        new_task = Task(1,"Actualizacion de la tarea 2")
        new_task.state = Enum_state.EN_PROCESO
        new_task.date_update = datetime.date(2025, 12, 1)
        result = cls.controller.update_task(new_task)
        cls.assertEqual(result, True)

    @patch('sqlite3.connect')
    def test_update_state_task(cls, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        cls.__name_database = cls.__con.read_value("sqlite", "test_name_db")
        # Definimos el valor que debe devolver fetchall
        mock_cursor.fetchall.return_value = [
            (1, "aprender python", Enum_state.PENDIENTE, Enum_is_delete.FALSE, "", "", ""),
            (2, "aprender java", Enum_state.PENDIENTE, Enum_is_delete.FALSE, "", "", "")
        ]
        cls.db = ManagerTableTasks(cls.__name_database)
        cls.controller = TaskController(cls.db)
        result = cls.controller.update_state(1, Enum_state.TERMINADO)
        cls.assertEqual(result, True)

    @patch('sqlite3.connect')
    def test_delete_task(cls, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        cls.__name_database = cls.__con.read_value("sqlite", "test_name_db")
        # Definimos el valor que debe devolver fetchall
        mock_cursor.fetchall.return_value = [
            (1, "aprender python", Enum_state.PENDIENTE, Enum_is_delete.FALSE, "", "", ""),
            (2, "aprender java", Enum_state.PENDIENTE, Enum_is_delete.FALSE, "", "", "")
        ]
        cls.db = ManagerTableTasks(cls.__name_database)
        cls.controller = TaskController(cls.db)
        result = cls.controller.delete_task_logical(1)
        cls.assertEqual(result, True)

    @patch('sqlite3.connect')
    def test_delete_task(cls, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        cls.__name_database = cls.__con.read_value("sqlite", "test_name_db")
        # Definimos el valor que debe devolver fetchall
        mock_cursor.fetchall.return_value = [
            (1, "aprender python", Enum_state.PENDIENTE, Enum_is_delete.FALSE, "", "", ""),
            (2, "aprender java", Enum_state.PENDIENTE, Enum_is_delete.FALSE, "", "", "")
        ]
        cls.db = ManagerTableTasks(cls.__name_database)
        cls.controller = TaskController(cls.db)
        result = cls.controller.delete_task_logical(1)
        cls.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()

#py -m unittest test\Test_task_controller.py