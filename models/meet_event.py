from sqlalchemy.orm import  relationship
from sqlalchemy import Column, Integer, String, Date, DateTime, TIMESTAMP, ForeignKey

from models.base import Base
from models.meet_event_type import MeetEventType
from models.distance import Distance
from models.discipline import Discipline
from models.heat import Heat
from models.entry import Entry
from models.relay_entry import RelayEntry
from models.age_group_type import AgeGroupType


class MeetEvent(Base):
    __tablename__ = "meet_event"
    meet_id = Column(Integer, ForeignKey('meet.meet_id'), primary_key=True)
    program_number = Column(String(4), primary_key=True)
    event_name = Column(String(100), nullable=True)
    event_order = Column(Integer, nullable=False)
    event_type_code = Column(String(10), ForeignKey('meet_event_type.type_code'), nullable=False)
    discipline_code = Column(String(10), ForeignKey('discipline.discipline_code'), nullable=False)
    legs = Column(Integer, nullable=False)
    distance_code = Column(String(10), ForeignKey('distance.distance_code'), nullable=False)
    deadline = Column(DateTime, nullable=True)
    age_group_type_code = Column(String(10), ForeignKey('age_group_type.age_group_type_code'), nullable=True)
    updated_at = Column(TIMESTAMP)
    created_at = Column(TIMESTAMP)

    meet = relationship("Meet", back_populates="events")
    event_type = relationship("MeetEventType", uselist=False, lazy="joined")
    discipline = relationship("Discipline", uselist=False, lazy="joined")
    distance = relationship("Distance", uselist=False, lazy="joined")
    heats = relationship("Heat", back_populates="meet_event")

    individual_entries = relationship("Entry", back_populates="meet_event")
    relay_entries = relationship("RelayEntry", back_populates="meet_event")
