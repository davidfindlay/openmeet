from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Table, Column, Integer, String, Date, DateTime, TIMESTAMP

from models.base import Base
from db.db import SessionLocal


class MeetEventType(Base):
    __tablename__ = "meet_event_type"
    type_id = Column(Integer, primary_key=True, autoincrement=True)
    type_name = Column(String(50), nullable=False)

    def __eq__(self, other):
        if isinstance(other, MeetEventType):
            return self.type_name == other.type_name
        else:
            return False


class MeetEventTypeCache(dict):
    def __missing__(self, key):
        try:
            obj = self[key] = SessionLocal.query(MeetEventType).filter_by(type_name=key).one()
            return obj
        except InvalidRequestError:
            obj = self[key] = MeetEventType(key)
            return obj
