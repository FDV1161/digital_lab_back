from pydantic import BaseModel
from typing import List
from app.api.base.shemas import OrmBaseModel
from app.api.measure.shemas import MeasureOut
from typing import Optional


class SensorIn(OrmBaseModel):
    name: str
    description: str
    address: int
    on_home: Optional[bool]
    room_id: Optional[int]
    measure: Optional[MeasureOut]
    # device_id


class SensorOut(SensorIn):
    id: int


class SensorList(OrmBaseModel):
    __root__: List[SensorOut]
