test_database_name = "badgernotetest.db"

import os
import unittest
import operations

class OperationTest(unittest.TestCase):
  def setUp(self):
    operations.setup_database(test_database_name)
  def tearDown(self):
    os.remove(test_database_name) 

class TestCreateNewNote(OperationTest):
  def test(self):
    pass

class TestUpdateNote(OperationTest):
  def test(self):
    pass

class TestPrintListOfNotes(OperationTest):
  def test(self):
    pass

if __name__ == "__main__":
  unittest.main()

