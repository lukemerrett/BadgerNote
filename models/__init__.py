__author__ = 'Luke Merrett'

from peewee import *
import settings

db = SqliteDatabase(settings.sqlite_database_name, threadlocals=True)

class BaseModel(Model):
    class Meta:
        database = db
