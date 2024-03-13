#!/usr/bin/python3
"""Holds class State"""

import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """Representation of state"""
    if models.storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""
        cites = []

    @property
    def cities(self):
        """Getter for cities"""
        return self._cities

    @cities.setter
    def cities(self, value):
        """Setter for cities"""
        self._cities = value
