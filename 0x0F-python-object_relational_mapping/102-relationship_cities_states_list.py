#!/usr/bin/python3
"""
script 14-model_city_fetch_by_state.py
that prints all City objects
from the database hbtn_0e_14_usa
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from sys import argv
from relationship_city import City


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost: \
                        3306/{}".format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    cn_session = sessionmaker(bind=engine)
    session = cn_session()
    query = session.query(State).join(City).\
        order_by(City.id).all()
    for state in query:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
    session.commit()
    session.close()
