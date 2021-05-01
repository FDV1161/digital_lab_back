from pydantic import BaseModel
from typing import List
from app.api.base.shemas import OrmBaseModel
from app.api.sensor.shemas import SensorList


class RoomIn(OrmBaseModel):
    name: str
    description: str


class RoomOut(RoomIn):
    id: int


class RoomDetailOut(RoomIn):
    id: int
    sensor_list: SensorList

# class RoomEditIn()

class RoomList(OrmBaseModel):
    __root__: List[RoomOut]
