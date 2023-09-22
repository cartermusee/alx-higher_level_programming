#!/usr/bin/python3
"""script that lists all State objects from
the database hbtn_0e_6_usa
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost: \
                        3306/{}".format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    cn_session = sessionmaker(bind=engine)
    session = cn_session()

    query = session.query(State).all()
    list_state = []
    for state in query:
        list_state.append(state.name)

    query = session.query(State).\
        filter(State.name == "{}".format(argv[4], )).first()

    if argv[4] not in list_state:
        print("Not found")
    else:
        print(query.id)
    session.close()