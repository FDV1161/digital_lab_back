from pydantic import BaseModel
from typing import List, Optional
from app.api.base.shemas import OrmBaseModel
from app.api.sensor.shemas import SensorList


class RoomIn(OrmBaseModel):
    name: str
    description: str
    sensor_one_id: Optional[int]
    sensor_two_id: Optional[int]
    sensor_free_id: Optional[int]


class RoomOut(RoomIn):
    id: int


class RoomDetailOut(RoomIn):
    id: int
    sensor_list: SensorList

# class RoomEditIn()


class RoomList(OrmBaseModel):
    __root__: List[RoomOut]
