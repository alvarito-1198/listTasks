import unittest
from Config import Config


class Test_config(unittest.TestCase):

    def setUp(cls):
        cls.__name_database = "dbTasksList2025"

    def test_variable_name_db(cls):
        config_use = Config()
        name_database = config_use.read_value("sqlite","name_db")
        print(name_database)
        cls.assertEqual(name_database, cls.__name_database)


if __name__ == '__main__':
    unittest.main()

#py -m unittest test\Test_config.py
