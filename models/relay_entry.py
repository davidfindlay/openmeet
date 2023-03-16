from sqlalchemy.orm import  relationship
from sqlalchemy import Column, Integer, String, Boolean, DateTime, TIMESTAMP, ForeignKeyConstraint, DECIMAL

from models.base import Base
# from models.meet_event import MeetEvent
from models.relay_member import RelayMember


class RelayEntry(Base):
    __tablename__ = "relay_entry"
    __table_args__ = (
        ForeignKeyConstraint(
            ["meet_id", "program_number"],
            ["meet_event.meet_id", "meet_event.program_number"]
        ),
    )
    relay_entry_id = Column(Integer, primary_key=True)
    meet_id = Column(Integer, nullable=False)
    program_number = Column(String(4), nullable=False)
    team_id = Column(Integer, nullable=True)
    organisation_id = Column(Integer, nullable=True)
    seed_time = Column(DECIMAL(9, 3), nullable=True)
    letter = Column(String(1), nullable=True)
    team_name = Column(String(40), nullable=True)
    status_code = Column(String(10), nullable=True)
    cancelled = Column(Boolean, nullable=True)
    scratched = Column(Boolean, nullable=True)
    exhibition = Column(Boolean, nullable=True)
    age_group_code = Column(String(10), nullable=True)
    updated_at = Column(TIMESTAMP)
    created_at = Column(TIMESTAMP)

    meet_event = relationship("MeetEvent")
    members = relationship("RelayMember",
                           back_populates="relay_entry")
