#!/usr/bin/python3
"""Holds class State"""

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.base_model import BaseModel, Base
from models import storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        name = ""

        @property
        def cities(self):
            city_all = []
            for key in storage.all("City"):
                if storage.all("City")[key].state_id == self.id:
                    city_all.append(storage.all("City")[key])
            return city_all
