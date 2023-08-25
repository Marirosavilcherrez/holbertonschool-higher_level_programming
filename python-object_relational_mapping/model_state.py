#!/usr/bin/python3
"With ORM that lists all states from the database hbtn_0e_4_usa"

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

"Define the conection to database"
db_user = "root"
db_password = "root"
db_host = "localhost"
db_port = 3306
db_name = "hbtn_0e_6_usa"
db_url = f"mysql+mysqldb://{db_user}:{db_password}@{db_host}:\
        {db_port}/{db_name}"
"Create the database engine"
engine = create_engine(db_url, pool_pre_ping=True)
Base = declarative_base()


class State(Base):
    "Inherits from Base create a new table"
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
session.commit()
session.close()
