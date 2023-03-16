from sqlalchemy.orm import  relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.exc import InvalidRequestError

from db.db import SessionLocal
from models.base import Base
from models.unit import Unit
from models.course import Course


class Distance(Base):
    __tablename__ = "distance"
    distance_code = Column(String(10), primary_key=True)
    qty = Column(Integer, nullable=False)
    splits = Column(Integer, nullable=False)
    unit_code = Column(String(10), ForeignKey('unit.unit_code'), nullable=False)
    course_code = Column(String(10), ForeignKey('course.course_code'), nullable=True)
    title = Column(String(40), nullable=False)

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
