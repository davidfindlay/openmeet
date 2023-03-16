from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.exc import InvalidRequestError

from models.base import Base
from db.db import SessionLocal


class AgeGroupType(Base):
    __tablename__ = "age_group_type"
    age_group_type_code = Column(String(10), primary_key=True)
    age_group_type_name = Column(String(50), nullable=False)
    description = Column(Text, nullable=True)

    def __eq__(self, other):
        if isinstance(other, AgeGroupType):
            return self.type_name == other.discipline_name
        else:
            return False


class AgeGroupTypeCache(dict):
    def __missing__(self, key):
        try:
            print('finding %s' % key)
            obj = self[key] = SessionLocal.query(AgeGroupType).filter_by(age_group_type_name=key).one()
            return obj
        except InvalidRequestError:
            obj = self[key] = AgeGroupType(key)
            return obj
