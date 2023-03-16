from typing import Union
from pydantic import BaseModel
from datetime import date, datetime

class EntryBase(BaseModel):
    athlete_id: int
    meet_id: int
    program_number: str
    seed_time: Union[float, None] = None
    status_code: str
    cancelled: Union[bool, None] = None
    scratched: Union[bool, None] = None
    exhibition: Union[bool, None] = None


class EntryCreate(EntryBase):
    pass

class EntryResp(EntryBase):
    entry_id: int
    updated_at: datetime
    created_at: datetime

    class Config:
        orm_mode = True