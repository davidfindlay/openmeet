from sqlalchemy.orm import  relationship
from sqlalchemy import Column, Integer, String, Boolean, DateTime, TIMESTAMP, ForeignKeyConstraint

from models.base import Base
from models.heat_lane import HeatLane

class Heat(Base):
    __tablename__ = "heat"
    # Foreign key constraint meet_id and program_number to meet_event table
    __table_args__ = (
        ForeignKeyConstraint(
            ['meet_id', 'program_number'],
            ['meet_event.meet_id', 'meet_event.program_number']
        ),
    )

    meet_id = Column(Integer, primary_key=True)
    program_number = Column(String(4), primary_key=True)
    heat_number = Column(Integer, primary_key=True)
    start_dt = Column(DateTime, nullable=True)
    end_dt = Column(DateTime, nullable=True)
    skipped = Column(Boolean, nullable=True)
    skip_reason = Column(String(20), nullable=True)
    updated_at = Column(TIMESTAMP)
    created_at = Column(TIMESTAMP)

    meet_event = relationship("MeetEvent")
    lanes = relationship("HeatLane")
