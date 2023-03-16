from sqlalchemy.orm import  relationship
from sqlalchemy import Column, Integer, String, Boolean, DateTime, TIMESTAMP, ForeignKeyConstraint, DECIMAL

from models.base import Base
# from models.heat_lane import HeatLane


class OfficialResult(Base):
    __tablename__ = "official_result"
    __table_args__ = (
        ForeignKeyConstraint(
            ["meet_id", "program_number"],
            ["meet_event.meet_id", "meet_event.program_number"]
        ),
    )
    result_id = Column(Integer, primary_key=True)
    meet_id = Column(Integer)
    program_number = Column(String(4))
    entry_id = Column(Integer, nullable=True)
    relay_entry_id = Column(Integer, nullable=True)
    age_group_code = Column(String(4), nullable=True)
    team_id = Column(Integer, nullable=True)
    seconds = Column(DECIMAL(9, 3), nullable=True)
    distance = Column(Integer, nullable=True)
    unit_id = Column(Integer, nullable=True)
    place = Column(Integer, nullable=True)
    tied = Column(Boolean, nullable=True)
    no_start = Column(Boolean, nullable=True)
    no_finish = Column(Boolean, nullable=True)
    updated_at = Column(TIMESTAMP)
    created_at = Column(TIMESTAMP)

    # heat_lane = relationship("HeatLane",
    #                           foreign_keys="heat_result.meet_id, heat_result.program_number, heat_result.heat_number, heat_result.lane",
    #                           back_populates="results")
