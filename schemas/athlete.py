from typing import Union
from pydantic import BaseModel
from datetime import date, datetime


class AthleteBase(BaseModel):
    athlete_id: int
    surname: str
    first_name: str
    other_names: Union[str, None] = None
    preferred_name: Union[str, None] = None
    sex: Union[str, None] = None
    dob: Union[str, None] = None
    age: Union[int, None] = None
    member_number: Union[str, None] = None
    team_id: Union[int, None] = None


class AthleteCreate(AthleteBase):
    pass


class AthleteResp(AthleteBase):
    updated_at: datetime
    created_at: datetime

    class Config:
        orm_mode = True
