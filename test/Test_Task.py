import unittest
import datetime
from models_layer.Task import (Task as t_task)
from helpers.Enum_state import Enum_state
from helpers.Enum_is_deleted import Enum_is_delete

class Test_task(unittest.TestCase):


    def setUp(cls):
        # print("Entra setUp")
        cls.__id = 1
        cls.__state = Enum_state.PENDIENTE

        cls.__task = t_task(1, "tarea 1")
        cls.__task.state = Enum_state.PENDIENTE
        cls.__task.is_delete = Enum_is_delete.FALSE
        cls.__task.date_create = datetime.date(2025, 1, 1)
        cls.__task.date_update = datetime.date(1900, 1, 1)
        cls.__task.date_delete = datetime.date(1900, 1, 1)

    def tearDown(cls):
        # print("Entra tearDown")
        pass

    def test_value_task_id(cls):
        cls.assertEqual(cls.__task.id, cls.__id)

    def test_value_task_state(cls):
        cls.assertEqual(cls.__task.state, cls.__state)

    def test_not_value_task_state(cls):
        cls.assertNotEqual(cls.__task.state, "PENDIENTE")

if __name__ == '__main__':
    unittest.main()

#py -m unittest test\Test_Task.py
