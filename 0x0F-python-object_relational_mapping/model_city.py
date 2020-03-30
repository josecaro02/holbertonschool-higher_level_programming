#!/usr/bin/python3
''' Creates base model '''
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    ''' Class city to save in database '''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('State.id'))
