from typing import Union
from pydantic import BaseModel
from datetime import date, datetime

from schemas.relay_member import RelayMemberCreate

class RelayEntryBase(BaseModel):
    meet_id: int
    program_number: str
    team_id: Union[int, None] = None
    organisation_id: Union[int, None] = None
    seed_time: Union[float, None] = None
    letter: Union[str, None] = None
    team_name: Union[str, None] = None
    status_code: str
    cancelled: Union[bool, None] = None
    scratched: Union[bool, None] = None
    exhibition: Union[bool, None] = None

    members: list[RelayMemberCreate] = []

class RelayEntryCreate(RelayEntryBase):
    pass

class RelayEntryResp(RelayEntryBase):
    relay_entry_id: int
    created_at: datetime
    updated_at: datetime
