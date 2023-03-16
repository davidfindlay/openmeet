from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey

from models.base import Base


class Course(Base):
    __tablename__ = "course"
    course_code = Column(String(10), primary_key=True)
    course_name = Column(String(50), nullable=False)
    course_full_name = Column(String(50), nullable=False)
    abbreviation = Column(String(4), nullable=False)
    length = Column(Integer, nullable=False)
    unit_code = Column(Integer, ForeignKey('unit.unit_code'), nullable=False)

    unit = relationship("Unit", uselist=False)
