from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Table, Column, Integer, String, Date, DateTime, TIMESTAMP, ForeignKey

from models.base import Base
from models.athlete import Athlete


class Team(Base):
    __tablename__ = "team"
    team_id = Column(Integer, primary_key=True)
    meet_id = Column(Integer, ForeignKey('meet.meet_id'), primary_key=True)
    team_name = Column(String(100), nullable=False)
    short_name = Column(String(50), nullable=True)
    abbreviation = Column(String, nullable=True)
    updated_at = Column(DateTime, nullable=False)
    created_at = Column(DateTime, nullable=False)

    members = relationship("Athlete", uselist=True, back_populates="team")
