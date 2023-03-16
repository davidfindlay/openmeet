from sqlalchemy.orm import  relationship
from sqlalchemy import Column, Integer, String, Boolean, DateTime, TIMESTAMP, ForeignKeyConstraint

from models.base import Base
from models.heat_result import HeatResult


class HeatLane(Base):
    __tablename__ = "heat_lane"
    __table_args__ = (
        ForeignKeyConstraint(
            ["meet_id", "program_number", "heat_number"], ["heat.meet_id", "heat.program_number", "heat.heat_number"]
        ),
    )
    meet_id = Column(Integer, primary_key=True)
    program_number = Column(String(4), primary_key=True)
    heat_number = Column(Integer, primary_key=True)
    lane = Column(Integer, primary_key=True)
    athlete_id = Column(Integer, nullable=True)
    relay_team_id = Column(Integer, nullable=True)
    place = Column(Integer, nullable=True)
    tied = Column(Boolean, nullable=True)
    updated_at = Column(TIMESTAMP)
    created_at = Column(TIMESTAMP)

    # heat = relationship("Heat",
    #                           foreign_keys="heat_lane.meet_id, heat_lane.program_number, heat_lane.heat_number",
    #                           back_populates="lanes")
    #
    results = relationship("HeatResult")
