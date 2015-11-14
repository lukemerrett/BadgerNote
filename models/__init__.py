from peewee import *
from datetime import datetime

# Allows us to create the database after the module has initialised
# Makes this more unit testable
db_proxy = Proxy()

def create_database(database_name):
  db = SqliteDatabase(database_name, threadlocals=True)
  db_proxy.initialize(db)
  db.connect()
  db.create_table(Note, True)

class BaseModel(Model):
  class Meta:
    database = db_proxy

class Note(BaseModel):
  """
  Table holding the notes
  """
  # Peewee adds primary key fields automatically as "id = int (1,1)"
  title = TextField()
  body = TextField()
  date_created = DateTimeField(default=datetime.utcnow())
  date_modified = DateTimeField(default=datetime.utcnow())


