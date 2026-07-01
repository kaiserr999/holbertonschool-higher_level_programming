#!/usr/bin/python3
"""Script that deletes all State objects with a name containing the letter a."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    session.query(State).filter(State.name.like('%a%')).delete()
    session.commit()
    session.close()
