import unittest
from test import *
from test.Test_Task import Test_task
from test.Test_connection_sqlite import Test_manager_database_sqlite

def suite(self):
     suite = unittest.TestSuite()
     suite.addTest(Test_task('test_value_task_id'))
     suite.addTest(Test_task('test_value_task_state'))
     self.run(suite)
     return suite
     #pass

if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    # runner.run(suite())
    pass