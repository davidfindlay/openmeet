from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Table, Column, Integer, String, Date, DateTime, TIMESTAMP, ForeignKey

from models.base import Base
from models.meet_event import MeetEvent
from models.team_organisation import team_organisation


class Organisation(Base):
    __tablename__ = "organisation"
    organisation_id = Column(Integer, primary_key=True, autoincrement=True)
    organisation_name = Column(String(100), nullable=False)
    short_name = Column(String(50), nullable=True)
    abbreviation = Column(String, nullable=True)
    parent_id = Column(Integer, ForeignKey('organisation.organisation_id'), nullable=True)

    parent = relationship('Organisation', uselist=False)
    teams = relationship('Team', secondary=team_organisation, back_populates='organisations')
