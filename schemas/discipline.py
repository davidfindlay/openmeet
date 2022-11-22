from typing import Union
from pydantic import BaseModel


class DisciplineBase(BaseModel):
    discipline_name: str
    abbreviation: str
    description: Union[str, None] = None


class DisciplineCreate(DisciplineBase):
    pass


class DisciplineResp(DisciplineBase):
    discipline_id: int

    class Config:
        orm_mode = True
