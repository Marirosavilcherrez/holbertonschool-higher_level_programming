#!/usr/bin/python3
"With ORM that lists all states from the database hbtn_0e_4_usa"

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    "Function that list all states from the database"
    db_user = "root"
    db_password = "root"
    db_port = 3306
    db_name = "hbtn_0e_6_usa"

engine = create_engine(
    'mysql+mysqldb://{}:{}@localhost:{}/{}'.format(db_user,\
            db_password, db_port, db_name), pool_pre_ping=True)

Session = sessionmaker(bind=engine)
session = Session()
for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))
session.close()
