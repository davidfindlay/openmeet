from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Table, Column, Integer, String, Date, DateTime, TIMESTAMP

from models.base import Base
from models.meet_event import MeetEvent


class Meet(Base):
    __tablename__ = "meet"
    meet_id = Column(Integer, primary_key=True, autoincrement=True)
    meetname = Column(String(100), nullable=False)
    startdate = Column(Date, nullable=False)
    enddate = Column(Date, nullable=False)
    deadline = Column(DateTime, nullable=True)
    max_individual_events = Column(Integer, nullable=True)
    max_relay_events = Column(Integer, nullable=True)
    max_total_events = Column(Integer, nullable=True)
    age_up_date = Column(Date, nullable=True)
    stub = Column(String(20), nullable=True)
    updated_at = Column(TIMESTAMP)
    created_at = Column(TIMESTAMP)

    events = relationship("MeetEvent", back_populates="meet")
