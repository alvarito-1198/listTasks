import unittest
import datetime
from data_layer.ManagerTableTasks import ManagerTableTasks
from Config import Config
from models_layer.Task import (Task as t_task)
from helpers.Enum_state import Enum_state
from helpers.Enum_is_deleted import Enum_is_delete

from unittest import TestCase, mock
from unittest.mock import patch, MagicMock


class Test_manager_table_tasks(unittest.TestCase):

    __con = Config()

    @patch('sqlite3.connect')
    def test_add_task(cls, mock_connect):
        # Creamos mocks para conexión y cursor
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
        # # Instanciamos y usamos la clase
        db = ManagerTableTasks(cls.__name_database)
        # Ejecutamos una consulta con parámetros
        cls.__task = t_task(0, "tarea 3")
        cls.__task.state = Enum_state.PENDIENTE
        cls.__task.is_delete = Enum_is_delete.FALSE
        cls.__task.date_create = datetime.date(2025, 1, 1)
        cls.__task.date_update = datetime.date(1900, 1, 1)
        cls.__task.date_delete = datetime.date(1900, 1, 1)
        confirmation =db.add_task(cls.__task )
        cls.assertEqual(confirmation, True)


    @patch('sqlite3.connect')
    def test_create_task(cls, mock_connect):
        # Creamos mocks para conexión y cursor
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
        # # Instanciamos y usamos la clase
        db = ManagerTableTasks(cls.__name_database)
        # Ejecutamos una consulta con parámetros
        confirmation = db.create_task("tarea 4", Enum_state.PENDIENTE)
        cls.assertEqual(confirmation, True)

    @patch('sqlite3.connect')
    def test_find_task(cls, mock_connect):
        # Creamos mocks para conexión y cursor
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        cls.__name_database = cls.__con.read_value("sqlite", "test_name_db")
        # Definimos el valor que debe devolver fetchall
        mock_cursor.fetchall.return_value = [
            (1, "aprender python", Enum_state.PENDIENTE, Enum_is_delete.FALSE, "", "", "")
        ]
        # # Instanciamos y usamos la clase
        db = ManagerTableTasks(cls.__name_database)
        db.connect()
        # Ejecutamos consulta y verificamos resultado
        resultado = db.find_id('SELECT * FROM tasks where id = 1')
        mock_cursor.execute.assert_called_once_with('SELECT * FROM tasks where id = 1')
        cls.assertEqual(resultado, [
            (1, "aprender python", Enum_state.PENDIENTE, Enum_is_delete.FALSE, "", "", "")])
        mock_conn.close.assert_called_once()
        db.close()

    @patch('sqlite3.connect')
    def test_update_task(cls, mock_connect):
        # Creamos mocks para conexión y cursor
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
        # # Instanciamos y usamos la clase
        db = ManagerTableTasks(cls.__name_database)
        task = t_task(1, "tarea 1 cambiada-")
        task.state = Enum_state.EN_PROCESO
        task.is_delete = Enum_is_delete.FALSE
        task.date_create = datetime.date(2025, 1, 1)
        task.date_update = datetime.date(2025, 2, 2)
        result = db.update_task(task)
        cls.assertEqual(result, True)

    @patch('sqlite3.connect')
    def test_physical_delete_task(cls, mock_connect):
        # Creamos mocks para conexión y cursor
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
        # # Instanciamos y usamos la clase
        db = ManagerTableTasks(cls.__name_database)
        result = db.physical_delete_task(1)
        cls.assertEqual(result, True)

    @patch('sqlite3.connect')
    def test_logical_delete_task(cls, mock_connect):
        # Creamos mocks para conexión y cursor
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
        # # Instanciamos y usamos la clase
        db = ManagerTableTasks(cls.__name_database)
        result = db.logical_delete_task(2)
        cls.assertEqual(result, True)

    @patch('sqlite3.connect')
    def test_list_tasks(cls, mock_connect):
        # Creamos mocks para conexión y cursor
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
        # Instanciamos y usamos la clase
        db = ManagerTableTasks(cls.__name_database)
        list = db.list_tasks()
        count = len(list)
        cls.assertEqual(count, 2)






if __name__ == '__main__':
    unittest.main()

#py -m unittest test\Test_manager_table_tasks.py