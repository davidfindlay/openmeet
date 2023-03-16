from sqlalchemy import Column, String, Text

from models.base import Base


class TimeType(Base):
    __tablename__ = "time_type"
    time_type_code = Column(String(10), primary_key=True)
    time_type_name = Column(String(20), nullable=False)
    description = Column(Text, nullable=True)

