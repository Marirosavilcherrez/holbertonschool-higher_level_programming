#!/usr/bin/python3
"Script lists all State objects contain letter a from the database"

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    "Function list all states from the database 3 arguments"
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_port = 3306
    db_host = "localhost"
    db_name = sys.argv[3]
    db_url = f"mysql+mysqldb://{db_user}:{db_password}@{db_host}:\
             {db_port}/{db_name}"

    engine = create_engine(db_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        a_state = session.query(State).filter(State.name.like('%a%'))\
                .order_by(State.id).all()
        for state in a_state:
            print("{}: {}".format(state.id, state.name))
    session.close()
