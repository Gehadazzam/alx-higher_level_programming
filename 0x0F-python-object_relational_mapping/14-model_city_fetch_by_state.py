#!/usr/bin/python3
"""model to list State from data base"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys
from model_city import City as C

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

    tab = session.query
    (C, State).filter(State.id == C.id).all()
    for row, col in tab:
        print(f"{col.name}: ({row.id}) {row.name}")
    session.commit()
    session.close()
