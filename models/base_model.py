#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from uuid import uuid4
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from models import storage_type
Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if 'id' not in kwargs:
            self.id = str(uuid4())
        if 'created_at' not in kwargs:
            self.created_at = datetime.now()
        if 'updated_at' not in kwargs:
            self.updated_at = datetime.now()

        for k, v in kwargs.items():
            if k in ['created_at', 'updated_at']:
                setattr(self, k, datetime.fromisoformat(v))
            elif k != '__class__':
                setattr(self, k, v)

    def __str__(self):
        """Returns a string representation of the instance"""
        d = self.__dict__.copy()
        d.pop("_sa_instance_state", None)
        return "[{}] ({}) {}".format(type(self).__name__, self.id, d)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        dictionary = self.__dict__.copy()
        dictionary.update({'__class__': (
            str(type(self)).split('.')[-1]).split('\'')[0]})
        if self.created_at is not None:
            dictionary['created_at'] = self.created_at.isoformat()
        if self.updated_at is not None:
            dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary.pop("_sa_instance_state")
        return dictionary

    def delete(self):
        """Deletes an instance from the storage"""
        from models import storage
        storage.delete(self)
