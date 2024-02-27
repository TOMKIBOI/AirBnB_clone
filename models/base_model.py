#!/usr/bin/python3
"""
This is parent class Base model
"""

from datetime import datetime
from model import storage
import uuid

time = "%Y-%m-%dT%H:%M:%S.%f"

if models.storage_t == "datab":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """The parent class BaseModel from where other classes will be created"""
    if models.storage_t == "datab":
        id = Column(String(40), primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initialization stage of the BaseModel class"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.now()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.now()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """This is how string are represented in BaseModel"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
