from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.exc import InvalidRequestError

from models.base import Base
from db.db import SessionLocal


class AgeGroup(Base):
    __tablename__ = "age_group"
    age_group_code = Column(String(10), primary_key=True)
    age_group_type_code = Column(String(10), ForeignKey('age_group_type.age_group_type_code'), nullable=False)
    min = Column(Integer, nullable=False)
    max = Column(Integer, nullable=False)
    sex = Column(String(1), nullable=True)
    age_group_name = Column(String(50), nullable=False)
    short_name = Column(String(20), nullable=True)

    def __eq__(self, other):
        if isinstance(other, AgeGroup):
            return self.type_name == other.discipline_name
        else:
            return False


class AgeGroupCache(dict):
    def __missing__(self, key):
        try:
            print('finding %s' % key)
            obj = self[key] = SessionLocal.query(AgeGroup).filter_by(age_group_name=key).one()
            return obj
        except InvalidRequestError:
            obj = self[key] = AgeGroup(key)
            return obj
