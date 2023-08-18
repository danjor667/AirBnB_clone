#!/usr/bin/python3
"""
base_model module
"""
import uuid
from datetime import datetime
from . import storage


class BaseModel():
    """
    class BaseModel
    """

    def __init__(self, *args, **kwargs):
        """
        instantiating new obj
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, (datetime.fromisoformat(value)))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = (datetime.now())
            storage.new(self)

    def __str__(self):
        """
        string representation of obj
        """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        update the updated_at attribute
        to the last time the obj was saved
        """
        storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        edited default dictionary
        representation of object
        Returns: dict. attribute as
        key and attribut3 values as value
        """
        my_dict = {}
        for key, value in self.__dict__.items():
            if key == "updated_at" or key == "created_at":
                my_dict[key] = value.isoformat()
            else:
                my_dict[key] = value
        my_dict["__class__"] = self.__class__.__name__
        return my_dict
