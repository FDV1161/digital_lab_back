from pydantic import BaseModel
from typing import List
from app.api.base.shemas import OrmBaseModel


class SensorIn(OrmBaseModel):
    name: str
    description: str
    address: int
    on_home: bool
    # device_id
    # room_id
    # measure_id


class SensorOut(SensorIn):
    id: int


# class RoomList(OrmBaseModel):
#     object_list = List[RoomOut]

class SensorList(OrmBaseModel):
    __root__: List[SensorOut]
