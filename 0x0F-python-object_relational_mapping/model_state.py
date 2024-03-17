#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    __name__ = Column(String(128), nullable=False)


if __name__ == "__main__":
    engine = create_engine(
        "mysql://username:password@localhost:3306/database_name")
    Base.metadata.create_all(engine)
