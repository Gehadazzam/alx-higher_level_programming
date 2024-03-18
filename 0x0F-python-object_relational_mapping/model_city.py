#!/usr/bin/python3
"""module to manipulate data in python using sqlalchemy"""


from sqlalchemy import Column, ForeignKey, Integer, String
from model_state import Base


class City(Base):
    """new class"""

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)
