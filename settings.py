__author__ = 'Luke Merrett'

sqlite_database_name = 'badgernote.db'

# Override with the local_settings.py file if it exists
try:
  from local_settings import *
except ImportError as e:
  pass
