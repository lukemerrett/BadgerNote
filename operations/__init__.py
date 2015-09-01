from models import *

def print_list_of_notes():
     notes = Note.select().order_by(Note.date_created.desc())

     for note in notes:
         print(note.title)
         print(note.body)
         print(note.date_created)
         print("")

def create_new_note(title, body):
    if not isinstance(title, str):
        raise Exception("Title must be a string")
    if not isinstance(body, str):
        raise Exception("Body must be a string")

    new_note = Note.create(
        title=title,
        body=body
    )
    new_note.save()