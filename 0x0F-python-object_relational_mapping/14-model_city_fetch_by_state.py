#!/usr/bin/python3
"""
script 14-model_city_fetch_by_state.py
that prints all City objects
from the database hbtn_0e_14_usa
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv
from model_city import City


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost: \
                        3306/{}".format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    cn_session = sessionmaker(bind=engine)
    session = cn_session()

    query = session.query(City, State).join(State)

    for city, state in query.all():
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))
    session.commit()
    session.close()
