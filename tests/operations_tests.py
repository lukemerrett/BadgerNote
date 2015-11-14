test_database_name = "badgernotetest.db"

import os
import unittest
import operations

class OperationTest(object):
  def setUp(self):
    operations.setup_database(test_database_name)
  def tearDown(self):
    os.remove(test_database_name) 

class TestOperations(unittest.TestCase, OperationTest):
  def setUp(self):
    OperationTest.setUp(self)
  def tearDown(self):
    OperationTest.tearDown(self)
 
  def test_create_new_note(self):
    pass

  def test_update_note(self):
    pass

  def test_print_list_of_notes(self):
    pass

if __name__ == "__main__":
  unittest.main()


