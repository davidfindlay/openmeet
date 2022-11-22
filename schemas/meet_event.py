from typing import Union
from datetime import date, datetime
from pydantic import BaseModel


class MeetEventBase(BaseModel):
    event_name: Union[str, None] = None
    event_order: int
    program_number: int
    event_type: str
    discipline: str
    legs: int
    distance: str
    deadline: Union[datetime, None] = None


class MeetEventCreate(MeetEventBase):
    pass


class MeetEventResp(MeetEventBase):
    meet_id: int
    event_id: int
    updated_at: datetime
    created_at: datetime

    class Config:
        orm_mode = True
