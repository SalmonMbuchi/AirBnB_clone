#!/usr/bin/env python3
"""this module contains the parent class that will take care of"""
"""initialization, serialization and deserialization of instances"""
import uuid
import models
from datetime import datetime
class BaseModel:
    """defines all common attributes for other classes"""

    def __init__(self, *args, **kwargs):
        """initializes public attributes"""
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                elif k != "__class__":
                    setattr(self, k, v)

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """ updates the attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
         of __dict__ of an instance """
        dictionary = self.__dict__.copy()
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary['__class__'] = self.__class__.__name__
        return dictionary

    def __str__(self):
        """ returns a readable message"""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
