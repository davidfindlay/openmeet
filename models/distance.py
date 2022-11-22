from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, ForeignKey
from sqlalchemy.exc import InvalidRequestError

from db.db import SessionLocal
from models.base import Base
from models.unit import Unit
from models.course import Course


class Distance(Base):
    __tablename__ = "distance"
    distance_id = Column(Integer, primary_key=True, autoincrement=True)
    qty = Column(Integer, nullable=False)
    unit_id = Column(Integer, ForeignKey('unit.unit_id'), nullable=False)
    title = Column(String(40), nullable=False)
    splits = Column(Integer, nullable=False)
    course_id = Column(Integer, ForeignKey('course.course_id'), nullable=True)

    unit = relationship("Unit", uselist=False)
    course = relationship("Course", uselist=False)

    def __eq__(self, other):
        if isinstance(other, Unit):
            return self.type_name == other.title
        else:
            return False


class DistanceCache(dict):
    def __missing__(self, key):
        try:
            obj = self[key] = SessionLocal.query(Distance).filter_by(title=key).one()
            return obj
        except InvalidRequestError:
            obj = self[key] = Distance(key)
            return obj
