#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
import os
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage


#storage = FileStorage()
#storage.reload()
if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()
    storage.reload()
