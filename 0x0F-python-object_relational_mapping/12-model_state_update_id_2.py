#!/usr/bin/python3
"""model to list State from data base"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    pas = sys.argv[2]
    data = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(username, pas, data),
        pool_pre_ping=True,
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    update = session.query(State).filter_by(id='2')
    update.name = 'New Mexico'
    session.commit()
    session.close()
