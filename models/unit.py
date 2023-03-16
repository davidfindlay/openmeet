from sqlalchemy import Column, String

from models.base import Base


class Unit(Base):
    __tablename__ = "unit"
    unit_code = Column(String(10), primary_key=True)
    unit_name = Column(String(50), nullable=False)
    abbreviation = Column(String(10), nullable=False)
