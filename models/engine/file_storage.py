#!/usr/bin/env python3
"""this module facilitates serialization and deserialization"""
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """ serializes instances to a JSON file and viceversa"""
    __file_path = "file.json"
    __objects = {}

    # public instance methods
    def all(self):
        """ returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """ serializes __objects to the JSON file"""
        a_dict = self.__objects.copy()
        new_dict = {obj: a_dict[obj].to_dict() for obj in a_dict.keys()}
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(new_dict, f)

    def reload(self):
        """ deserialize the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                a_dict = json.load(f)
                for obj in a_dict.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            pass
