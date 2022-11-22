from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Text, TIMESTAMP

from models.base import Base


class Unit(Base):
    __tablename__ = "unit"
    unit_id = Column(Integer, primary_key=True, autoincrement=True)
    unit_name = Column(String(50), nullable=False)
    abbreviation = Column(String(10), nullable=False)
