from sqlalchemy.orm import  relationship
from sqlalchemy import Column, Integer, String, Boolean, DateTime, TIMESTAMP, ForeignKeyConstraint, DECIMAL

from models.base import Base
# from models.heat_lane import HeatLane


class HeatResult(Base):
    __tablename__ = "heat_result"
    __table_args__ = (
        ForeignKeyConstraint(
            ["meet_id", "program_number", "heat_number", "lane"],
            ["heat_lane.meet_id", "heat_lane.program_number", "heat_lane.heat_number", "heat_lane.lane"]
        ),
    )
    meet_id = Column(Integer, primary_key=True)
    program_number = Column(String(4), primary_key=True)
    heat_number = Column(Integer, primary_key=True)
    lane = Column(Integer, primary_key=True)
    time_type_code = Column(String(10), primary_key=True)
    seconds = Column(DECIMAL(9, 3), nullable=True)
    rejected = Column(Boolean, nullable=True)
    rejected_reason = Column(String(50), nullable=True)
    updated_at = Column(TIMESTAMP)
    created_at = Column(TIMESTAMP)

    # heat_lane = relationship("HeatLane",
    #                           foreign_keys="heat_result.meet_id, heat_result.program_number, heat_result.heat_number, heat_result.lane",
    #                           back_populates="results")
