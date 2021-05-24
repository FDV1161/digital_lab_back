from typing import List
from app.api.base.shemas import OrmBaseModel

from typing import Optional


class DeviceIn(OrmBaseModel):
    name: str
    room_id: int
    controller_id: int
    description: Optional[str]
    icon: Optional[str]


class DeviceOut(DeviceIn):
    id: int


class DeviceList(OrmBaseModel):
    __root__: List[DeviceOut]
