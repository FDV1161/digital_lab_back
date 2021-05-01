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
    room_id: int
    device_id: int


class SensorEditIn(SensorIn):
    measure_id: int


class SensorOut(SensorIn):
    id: int
    measure: Optional[MeasureOut]
    # devices:


class SensorList(OrmBaseModel):
    __root__: List[SensorOut]
