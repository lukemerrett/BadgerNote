from models import *

def print_header(header):
    print("")
    print(header)
    print("-" * len(header))
    print("")

def setup_database(database_name):
  create_database(database_name)

def create_new_note(title, body):
  if not isinstance(title, str):
    raise TypeError("Title must be a string")
  if not isinstance(body, str):
    raise TypeError("Body must be a string")

  new_note = Note.create(
    title=title,
    body=body
  )
  new_note.save()

def update_note(noteId, title, body):
  if not isinstance(noteId, str) and not isinstance(noteId, int):
    raise TypeError("Note ID must be a string or integer")
  if not isinstance(title, str):
    raise TypeError("Title must be a string")
  if not isinstance(body, str):
    raise TypeError("Body must be a string")

  note = Note.get(Note.id == noteId)

  note.title = title;
  note.body = body;
  note.save()

def get_list_of_notes():
   notes = Note.select().order_by(Note.date_created.desc())
   return notes

def print_list_of_notes():
   notes = get_list_of_notes()
   print_header("Current Notes")

   for note in notes:
     print("Note ID: " + str(note.id))
     print(note.title)
     print(note.body)
     print(note.date_created)
     print("")

