#!/usr/bin/python3
"""
This module instantiates an object of class FileStorage
if the database supplied is FileStorage
And DBStorage if DBStorage is supplied
"""
from os import getenv

storage_type = getenv('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

>>>>>>> boomni
storage.reload()
