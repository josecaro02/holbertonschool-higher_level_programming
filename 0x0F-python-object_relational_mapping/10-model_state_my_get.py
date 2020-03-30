#!/usr/bin/python3
''' List all State objects from the database hbtn_0e_6_usa '''

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).filter(State.name == sys.argv[4])
    for i in result:
        print("{}".format(i.id))
    if len(result.all()) == 0:
        print("Not found")
    session.close()
