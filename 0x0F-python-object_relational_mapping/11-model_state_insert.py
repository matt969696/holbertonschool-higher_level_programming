#!/usr/bin/python3
"""
ists all State objects from the database hbtn_0e_6_usa
"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    newState = State(name='Louisiana')
    session.add(newState)

    res1 = session.query(State)
    res2 = res1.filter(State.name == 'Louisiana').order_by(State.id)
    res = res2.first()
    print("{}".format(res.id))
    session.commit()
    session.close()
