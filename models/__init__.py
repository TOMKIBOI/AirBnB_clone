#!/urs/bin/python3
"""
initializing model class BaseModel packages.
"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()

