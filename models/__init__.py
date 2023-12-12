#!/urs/bin/python3
"""
initializing model class BaseModel packages.
"""

from os import getenv


storage_t = getenv("HBNB_TYPE_STORAGE")

if storage_tim == "datab":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
