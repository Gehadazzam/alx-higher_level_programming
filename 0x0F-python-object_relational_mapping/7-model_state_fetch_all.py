#!/usr/bin/python3
"""model to list State from data base"""


from sqlalchemy import create_engine
from sqlalchemy.orm sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    if sys.argv != 4:
        sys.exit(1)

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

    tab = session.query(State).order_by(State.id).all()
    for row in tab:
        print(f"{_.id}: {_.name}")
    session.close()
