from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Table, Column, Integer, String, Date, DateTime, TIMESTAMP, ForeignKey

from models.base import Base
from models.meet_event import MeetEvent

team_organisation = Table(
    "team_organisation",
    Base.metadata,
    Column("team_id", ForeignKey("team.team_id")),
    Column("organisation_id", ForeignKey("organisation.organisation_id"))
)