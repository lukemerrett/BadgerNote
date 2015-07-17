__author__ = 'Luke Merrett'

from peewee import *
import settings
from datetime import datetime

db = SqliteDatabase(settings.sqlite_database_name, threadlocals=True)

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
