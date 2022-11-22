from typing import Union
from pydantic import BaseModel
from schemas.athlete import AthleteCreate
from datetime import date, datetime


class TeamBase(BaseModel):
    team_id: int
    team_name: str
    abbreviation: Union[str, None] = None
    short_name: Union[str, None] = None

    members: Union[list[AthleteCreate], None] = None


class TeamCreate(TeamBase):
    pass


class TeamResp(TeamBase):
    updated_at: datetime
    created_at: datetime

    class Config:
        orm_mode = True
