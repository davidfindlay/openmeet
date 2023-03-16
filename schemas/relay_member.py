from typing import Union
from pydantic import BaseModel
from datetime import date, datetime

class RelayMemberBase(BaseModel):
    leg: int
    athlete_id: int
    cancelled: Union[bool, None] = None
    seed_time: Union[float, None] = None

class RelayMemberCreate(RelayMemberBase):
    pass

class RelayMemberResp(RelayMemberBase):
    relay_entry_id: int
    created_at: datetime
    updated_at: datetime
