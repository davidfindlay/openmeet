from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Table, Column, Integer, String, ForeignKey

from models.base import Base


class Course(Base):
    __tablename__ = "course"
    course_id = Column(Integer, primary_key=True, autoincrement=True)
    course_name = Column(String(50), nullable=False)
    course_full_name = Column(String(50), nullable=False)
    length = Column(Integer, nullable=False)
    unit_id = Column(Integer, ForeignKey('unit.unit_id'), nullable=False)

    unit = relationship("Unit", uselist=False)
