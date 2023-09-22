#!/usr/bin/python3

"""
python file that contains the
class definition of a State and
an instance Base = declarative_base()
"""


from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    inherits from base and creates table
    args:
        Base:its a class
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True,
                unique=True, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
