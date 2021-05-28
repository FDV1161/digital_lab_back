from typing import List, Optional

from app.api.base.shemas import OrmBaseModel
from app.api.device.shemas import DeviceList


class RoomIn(OrmBaseModel):
    name: str
    description: Optional[str]


class RoomOut(RoomIn):
    id: int
    devices: DeviceList


class RoomDetailOut(RoomIn):
    id: int


class RoomList(OrmBaseModel):
    __root__: List[RoomOut]
