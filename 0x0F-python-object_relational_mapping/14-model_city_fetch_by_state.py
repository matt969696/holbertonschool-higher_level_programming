#!/usr/bin/python3
"""
ists all State objects from the database hbtn_0e_6_usa
"""


import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    res1 = session.query(State, City)
    res2 = res1.filter(City.state_id == State.id).order_by(City.id)
    for state, city in res2.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
