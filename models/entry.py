from sqlalchemy.orm import  relationship
from sqlalchemy import Column, Integer, String, Boolean, DateTime, TIMESTAMP, ForeignKeyConstraint, DECIMAL, UniqueConstraint

from models.base import Base


class Entry(Base):
    __tablename__ = "entry"
    __table_args__ = (
        ForeignKeyConstraint(
            ["meet_id", "program_number"],
            ["meet_event.meet_id", "meet_event.program_number"]
        ),
        UniqueConstraint('athlete_id', 'meet_id', 'program_number', name='entry_unique'),
    )
    entry_id = Column(Integer, primary_key=True)
    athlete_id = Column(Integer, nullable=False)
    meet_id = Column(Integer, nullable=False)
    program_number = Column(String(4), nullable=False)
    seed_time = Column(DECIMAL(9, 3), nullable=True)
    status_code = Column(String(10), nullable=False)
    cancelled = Column(Boolean, nullable=True)
    scratched = Column(Boolean, nullable=True)
    exhibition = Column(Boolean, nullable=True)
    age_group_code = Column(String(10), nullable=True)
    updated_at = Column(TIMESTAMP)
    created_at = Column(TIMESTAMP)

    meet_event = relationship("MeetEvent")
