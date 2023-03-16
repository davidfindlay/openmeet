from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Table, Column, Integer, String, Date, DateTime, TIMESTAMP, ForeignKey

from models.base import Base


class Athlete(Base):
    __tablename__ = "athlete"
    athlete_id = Column(Integer, primary_key=True)
    surname = Column(String(100), nullable=False)
    first_name = Column(String(100), nullable=False)
    other_names = Column(String(100), nullable=True)
    preferred_name = Column(String(100), nullable=True)
    sex = Column(String(1), nullable=True)
    dob = Column(Date, nullable=True)
    age = Column(Integer, nullable=True)
    member_number = Column(String(20), nullable=True)
    team_id = Column(Integer, ForeignKey('team.team_id'), nullable=True)
    import_id = Column(Integer, nullable=True)
    updated_at = Column(DateTime, nullable=False)
    created_at = Column(DateTime, nullable=False)

    team = relationship("Team", uselist=False, back_populates="members")
