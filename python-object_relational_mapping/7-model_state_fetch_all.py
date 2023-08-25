#!/usr/bin/python3
"With ORM that lists all states from the database hbtn_0e_4_usa"

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    "Function that list all states from the database"
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_port = 3306
    db_host = "localhost"
    db_name = sys.argv[3]
    db_url = f"mysql+mysqldb://{db_user}:{db_password}@{db_host}:\
             {db_port}/{db_name}"

    engine = create_engine(db_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
