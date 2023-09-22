#!/usr/bin/python3
"""
Python file similar to model_state.py
named model_city.py
that contains the
class definition of a City
"""


from sqlalchemy import Integer, String, Column, Table, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import State, Base


class City(Base):
    """
    inherits from base and creates table
    args:
        Base:its a class
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True,
                unique=True, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'),
                      nullable=False)
