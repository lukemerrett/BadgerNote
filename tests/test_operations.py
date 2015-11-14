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
  def test_title_must_be_string(self):
    try:
      operations.create_new_note(34.2, "")
      self.fail("TypeError should have been thrown")
    except TypeError:
      pass

  def test_body_must_be_string(self):
    try:
      operations.create_new_note("", 34.2)
      self.fail("TypeError should have been thrown")
    except TypeError:
      pass

  def test_valid_note_is_created(self):
    operations.create_new_note("title", "body")
    notes = operations.get_list_of_notes()
    self.assertEqual(1, notes.count())
    self.assertEqual("title", notes[0].title)
    self.assertEqual("body", notes[0].body)


class TestUpdateNote(OperationTest):
  def test_noteid_must_be_string_or_int(self):
    try:
      operations.update_note(553.22, "", "")
      self.fail("TypeError should have been thrown")
    except TypeError:
      pass

  def test_title_must_be_string(self):
    try:
      operations.update_note(123, 34.2, "")
      self.fail("TypeError should have been thrown")
    except TypeError:
      pass

  def test_body_must_be_string(self):
    try:
      operations.update_note(123, "", 34.2)
      self.fail("TypeError should have been thrown")
    except TypeError:
      pass 

  def test_note_must_exist_in_db(self):
    try:
      operations.update_note(123, "", "")
      self.fail("Exception should have been thrown as note does not exist")
    except Exception:
      pass

  def test_note_correctly_updated(self):
    operations.create_new_note("title", "body")
    operations.update_note(1, "new title", "new body")
    notes = operations.get_list_of_notes()
    self.assertEqual(1, notes.count())
    self.assertEqual("new title", notes[0].title)
    self.assertEqual("new body", notes[0].body)


class TestPrintListOfNotes(OperationTest):
  def test_method_runs(self):
    operations.create_new_note("title", "body")
    operations.print_list_of_notes()


if __name__ == "__main__":
  unittest.main()

