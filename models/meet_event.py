from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Table, Column, Integer, String, Date, DateTime, TIMESTAMP, ForeignKey

from models.base import Base
from models.meet_event_type import MeetEventType
from models.distance import Distance
from models.discipline import Discipline


class MeetEvent(Base):
    __tablename__ = "meet_event"
    meet_id = Column(Integer, ForeignKey('meet.meet_id'), primary_key=True)
    program_number = Column(String(4), primary_key=True)
    event_name = Column(String(100), nullable=True)
    event_order = Column(Integer, nullable=False)
    event_type_id = Column(Integer, ForeignKey('meet_event_type.type_id'), nullable=False)
    discipline_id = Column(Integer, ForeignKey('discipline.discipline_id'), nullable=False)
    legs = Column(Integer, nullable=False)
    distance_id = Column(Integer, ForeignKey('distance.distance_id'), nullable=False)
    deadline = Column(DateTime, nullable=True)
    updated_at = Column(TIMESTAMP)
    created_at = Column(TIMESTAMP)

    meet = relationship("Meet", back_populates="events")
    event_type = relationship("MeetEventType", uselist=False, lazy="joined")
    discipline = relationship("Discipline", uselist=False, lazy="joined")
    distance = relationship("Distance", uselist=False, lazy="joined")
