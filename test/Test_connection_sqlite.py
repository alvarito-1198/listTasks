import pathlib
import unittest
from unittest.mock import patch, MagicMock
from helpers.Enum_state import Enum_state
from helpers.Enum_is_deleted import Enum_is_delete
from data_layer.ConnectionSqlite import Connectionsqlite

from Config import Config


class Test_manager_database_sqlite(unittest.TestCase):
    __con = Config()


    def setUp(cls):
        pass

    @patch('sqlite3.connect')
    def test_execute(cls, mock_connect):
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
        db = Connectionsqlite(cls.__name_database)
        db.connect()
        # Ejecutamos una consulta con parámetros
        db.execute('INSERT INTO tasks VALUES (id, description, state, isdelete)', ('null', 'apreder c#', 1, 0))
        mock_cursor.execute.assert_called_with('INSERT INTO tasks VALUES (id, description, state, isdelete)',
                                               ('null', 'apreder c#', 1, 0))
        mock_conn.commit.assert_called()

        # Cerramos conexión y verificamos llamada
        mock_conn.close.assert_called_once()
        db.close()



    @patch('sqlite3.connect')
    def test_execute_insert(cls, mock_connect):
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
        db = Connectionsqlite(cls.__name_database)
        db.connect()
        # Ejecutamos una consulta con parámetros
        db.execute_insert(f"INSERT INTO tasks (id, description, state, is_delete,date_create,date_update,date_delete  ) "
                            f"VALUES (NULL, 'aprender linux', 1, False,"
                            f"'2025-01-01','1900-01-01','1900-01-01');" )
        mock_cursor.execute.assert_called_with(f"INSERT INTO tasks (id, description, state, is_delete,date_create,date_update,date_delete  ) "
                            f"VALUES (NULL, 'aprender linux', 1, False,"
                            f"'2025-01-01','1900-01-01','1900-01-01');")
        mock_conn.commit.assert_called()

        # Cerramos conexión y verificamos llamada
        mock_conn.close.assert_called_once()
        db.close()


    @patch('sqlite3.connect')
    def test_execute_update(cls, mock_connect):
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
        db = Connectionsqlite(cls.__name_database)
        db.connect()
        # Ejecutamos una consulta con parámetros
        db.execute_update(f"UPDATE tasks SET description='valor cambiado', state=1, is_delete=0 WHERE id = 1;")
        mock_cursor.execute.assert_called_with(f"UPDATE tasks SET description='valor cambiado', state=1, is_delete=0 WHERE id = 1;")
        mock_conn.commit.assert_called()

        # Cerramos conexión y verificamos llamada
        mock_conn.close.assert_called_once()
        db.close()

    @patch('sqlite3.connect')
    def test_execute_phisical_delete(cls, mock_connect):
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
        db = Connectionsqlite(cls.__name_database)
        db.connect()
        # Ejecutamos una consulta con parámetros
        id=1
        db.execute_delete(f"delete from task where id = {id}",id)
        mock_cursor.execute.assert_called_with(f"delete from task where id = {id}")
        mock_conn.commit.assert_called()
        # Cerramos conexión y verificamos llamada
        mock_conn.close.assert_called_once()
        db.close()

    @patch('sqlite3.connect')
    def test_execute_logical_delete(cls, mock_connect):
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
        db = Connectionsqlite(cls.__name_database)
        db.connect()
        # Ejecutamos una consulta con parámetros
        id=1
        de = True
        db.execute_delete(f"UPDATE tasks SET is_delete={de} WHERE id = {id};", id)
        mock_cursor.execute.assert_called_with(f"UPDATE tasks SET is_delete={de} WHERE id = {id};")
        mock_conn.commit.assert_called()
        # Cerramos conexión y verificamos llamada
        mock_conn.close.assert_called_once()
        db.close()

    @patch('sqlite3.connect')
    def test_execute_phisical_delete(cls, mock_connect):
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
        db = Connectionsqlite(cls.__name_database)
        db.connect()
        # Ejecutamos una consulta con parámetros
        id = 1
        db.execute_delete(f"delete from task where id = {id}", id)
        mock_cursor.execute.assert_called_with(f"delete from task where id = {id}")
        mock_conn.commit.assert_called()
        # Cerramos conexión y verificamos llamada
        mock_conn.close.assert_called_once()
        db.close()

    @patch('sqlite3.connect')
    def test_find_id(cls, mock_connect):
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
        db = Connectionsqlite(cls.__name_database)
        db.connect()

        # Ejecutamos consulta y verificamos resultado
        resultado = db.find_id(1)
        #mock_cursor.execute.assert_called_once_with('SELECT * FROM tasks where id = 1')
        cls.assertEqual(resultado, [
            (1, "aprender python", Enum_state.PENDIENTE, Enum_is_delete.FALSE, "", "", "")])
        mock_conn.close.assert_called_once()
        db.close()


    @patch('sqlite3.connect')
    def test_read(cls, mock_connect):
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
        db = Connectionsqlite(cls.__name_database)
        db.connect()

        # Ejecutamos consulta y verificamos resultado
        resultado = db.read('SELECT * FROM tasks whrere is_delete = False')
        mock_cursor.execute.assert_called_once_with('SELECT * FROM tasks whrere is_delete = False')
        cls.assertEqual(resultado, [
            (1, "aprender python", Enum_state.PENDIENTE, Enum_is_delete.FALSE, "", "", ""),
            (2, "aprender java", Enum_state.PENDIENTE, Enum_is_delete.FALSE, "", "", "")
        ])
        mock_conn.close.assert_called_once()
        db.close()


    @patch('sqlite3.connect')
    def test_connect(cls, mock_connect):
        # Creamos mocks para conexión y cursor
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        cls.__name_database = cls.__con.read_value("sqlite", "test_name_db")
        # # Instanciamos y usamos la clase
        db = Connectionsqlite(cls.__name_database)
        db.connect()
        #
        # # Verificamos que connect y cursor fueron llamados
        name_db = "TestDBTasksList2025"
        address = pathlib.Path(__file__).parent.parent.absolute().__str__()
        address = address + "\\data_layer\\database\\{}.db".format(name_db)
        mock_connect.assert_called_once_with(address)
        mock_conn.cursor.assert_called_once()
        db.close()
        mock_conn.close.assert_called_once()

    @patch('sqlite3.connect')  # Parcheamos sqlite3.connect dentro del módulo db
    def test_connect_and_sentence(cls, mock_connect):
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
        #
        # # Instanciamos y usamos la clase
        db = Connectionsqlite(cls.__name_database)
        db.connect()
        #
        # # Verificamos que connect y cursor fueron llamados
        name_db = "TestDBTasksList2025"
        address = pathlib.Path(__file__).parent.parent.absolute().__str__()
        address = address + "\\data_layer\\database\\{}.db".format(name_db)
        mock_connect.assert_called_once_with(address)
        mock_conn.cursor.assert_called_once()

        # Ejecutamos consulta y verificamos resultado
        resultado = db.read('SELECT * FROM tasks')
        mock_cursor.execute.assert_called_once_with('SELECT * FROM tasks')
        cls.assertEqual(resultado, [
            (1, "aprender python", Enum_state.PENDIENTE, Enum_is_delete.FALSE, "", "", ""),
            (2, "aprender java", Enum_state.PENDIENTE, Enum_is_delete.FALSE, "", "", "")
        ])

        # Ejecutamos una consulta con parámetros
        db.execute('INSERT INTO tasks VALUES (id, description, state, isdelete)', ('null', 'apreder c#', 1, 0))
        mock_cursor.execute.assert_called_with('INSERT INTO tasks VALUES (id, description, state, isdelete)',
                                               ('null', 'apreder c#', 1, 0))
        mock_conn.commit.assert_called()

        # Cerramos conexión y verificamos llamada
        # mock_conn.close.assert_called_once()
        db.close()


if __name__ == '__main__':
    unittest.main()

#py -m unittest test\Test_connection_sqlite.py