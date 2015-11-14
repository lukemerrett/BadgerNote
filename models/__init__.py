from peewee import *
from datetime import datetime

db = None

def create_database(database_name):
  db = SqliteDatabase(database_name, threadlocals=True)
  db.connect()
  db.create_table(Note, True)

class BaseModel(Model):
  class Meta:
      database = db

class Note(BaseModel):
  """
  Table holding the notes
  """
  # Peewee adds primary key fields automatically as "id = int (1,1)"
  title = TextField()
  body = TextField()
  date_created = DateTimeField(default=datetime.utcnow())
  date_modified = DateTimeField(default=datetime.utcnow())


