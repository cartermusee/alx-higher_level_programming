#!/usr/bin/python3
"""script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa
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

    new = State(name="Louisiana")
    session.add(new)
    session.commit()

    query = session.query(State).order_by(State.id.desc()).first()

    print("{}".format(query.id))
    session.close()
