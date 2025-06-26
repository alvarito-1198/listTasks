import sqlite3
import pathlib
from helpers.Loggin_configuration import loggin_run
from Config import Config



class Connectionsqlite:
    # llamar al archivo de config.
    __con = Config()

    def __init__(cls, name_db=__con.read_value("sqlite", "name_db")):
        try:
            cls._name_db = name_db
            cls._address = pathlib.Path(__file__).parent.absolute().__str__()
            cls._address = cls._address + "/database/{}.db".format(cls._name_db)
            cls._conn = None
            cls._cursor = None
        except Exception as e:
            loggin_run(4, e)

    def connect(cls):
        try:
            cls._conn = sqlite3.connect(cls._address)
            cls._cursor = cls._conn.cursor()
        except Exception as e:
            loggin_run(4, e)

    def execute(cls, sentence, parameters=()):
        result = False
        try:
            cls.connect()
            cls._cursor.execute(sentence, parameters)
            cls._conn.commit()
            cls.close()
            result = True
            return result
        except Exception as e:
            loggin_run(4, e)
            cls.close()
            return result

    def execute_delete(cls, sentence, id):
        result = False
        try:
            cls.connect()
            cls._cursor.execute(sentence)
            cls._conn.commit()
            loggin_run(2, f"Eliminada de forma fisica la tarea con id {id}")
            cls.close()
            result = True
            return result
        except Exception as e:
            loggin_run(4, e)
            cls.close()
            return result

    def execute_update(cls, sentence):
        try:
            cls.connect()
            cls._cursor.execute(sentence)
            cls._conn.commit()
            last_id = cls._cursor.lastrowid
            loggin_run(2, f"Atualizada la tarea con id {last_id}")
            cls.close()
            return last_id
        except Exception as e:
            loggin_run(4, e)
            cls.close()

    def execute_insert(cls, sentence):
        try:
            cls.connect()
            cls._cursor.execute(sentence)
            cls._conn.commit()
            last_id = cls._cursor.lastrowid
            loggin_run(2, f"Creada la tarea con id {last_id}")
            cls.close()
            return last_id
        except Exception as e:
            loggin_run(4, e)
            cls.close()

    def read(cls, sentence):
        try:
            cls._cursor.execute(sentence)
            result = cls._cursor.fetchall()
            cls.close()
            return result
        except Exception as e:
            loggin_run(4, e)
            cls.close()

    def find_id(cls, sentence):
        try:
            cls._cursor.execute(sentence)
            result = cls._cursor.fetchall()
            cls.close()
            return result
        except Exception as e:
            loggin_run(4, e)
            cls.close()
            return None

    def close(cls):
        try:
            if cls._conn:
                cls._conn.close()
        except Exception as e:
            loggin_run(4, e)