from sqlalchemy.orm import  relationship
from sqlalchemy import Column, Integer, String, Boolean, DateTime, TIMESTAMP, ForeignKey, DECIMAL

from models.base import Base
from models.meet_event_type import MeetEventType
from models.distance import Distance
from models.discipline import Discipline


class RelayMember(Base):
    __tablename__ = "relay_member"
    relay_entry_id = Column(Integer, ForeignKey("relay_entry.relay_entry_id"), primary_key=True)
    leg = Column(Integer, primary_key=True)
    athlete_id = Column(Integer, nullable=False)
    cancelled = Column(Boolean, nullable=True)
    seed_time = Column(DECIMAL(9, 3), nullable=True)
    updated_at = Column(TIMESTAMP)
    created_at = Column(TIMESTAMP)

    relay_entry = relationship("RelayEntry")
