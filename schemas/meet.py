from typing import Union
from datetime import date, datetime
from pydantic import BaseModel

from schemas.meet_event import MeetEventCreate


class MeetBase(BaseModel):
    meetname: str
    startdate: date
    enddate: date
    deadline: Union[datetime, None] = None
    max_individual_events: Union[int, None] = None
    max_relay_events: Union[int, None] = None
    max_total_events: Union[int, None] = None
    age_up_date: Union[date, None] = None
    stub: Union[str, None] = None

    events: Union[list[MeetEventCreate], None] = None


class MeetCreate(MeetBase):
    pass


class MeetResp(MeetBase):
    meet_id: int
    updated_at: datetime
    created_at: datetime

    class Config:
        orm_mode = True
