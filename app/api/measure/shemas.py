from pydantic import BaseModel
from typing import List
from app.api.base.shemas import OrmBaseModel


class MeasureIn(OrmBaseModel):
    name: str
    symbol: str


class MeasureOut(MeasureIn):
    id: int


class MeasureList(OrmBaseModel):
    __root__: List[MeasureOut]
