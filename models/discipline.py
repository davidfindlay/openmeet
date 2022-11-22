from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.exc import InvalidRequestError

from models.base import Base
from db.db import SessionLocal


class Discipline(Base):
    __tablename__ = "discipline"
    discipline_id = Column(Integer, primary_key=True, autoincrement=True)
    discipline_name = Column(String(50), nullable=False)
    abbreviation = Column(String(10), nullable=False)
    description = Column(Text, nullable=True)

    def __eq__(self, other):
        if isinstance(other, Discipline):
            return self.type_name == other.discipline_name
        else:
            return False


class DisciplineCache(dict):
    def __missing__(self, key):
        try:
            print('finding %s' % key)
            obj = self[key] = SessionLocal.query(Discipline).filter_by(discipline_name=key).one()
            return obj
        except InvalidRequestError:
            obj = self[key] = Discipline(key)
            return obj
