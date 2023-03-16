from typing import Union, Optional
from datetime import date, datetime
from pydantic import BaseModel

class HeatResult(BaseModel):
    entry_id: int
    meet_id: int
    seconds: float
    time_type_code: str

class FinalResult(BaseModel):
    entry_id: int
    meet_id: int
    seconds: float

class ResultUpdate(BaseModel):
    entry_id: int
    meet_id: int
    final_result: Optional[FinalResult]
    heat_results: list[HeatResult]
