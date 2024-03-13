#!/usr/bin/python3
"""Holds class State"""

import models
from models import storage
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """Representation of state"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            """City property for state reference"""
            city_all = []
            for city_ex in models.storage.all(City).values():
                if city_ex.state_id == self.id:
                    city_all.append(city_ex)
            return city_all
