from pydantic import BaseModel
from typing import List
from app.api.base.shemas import OrmBaseModel


class DeviceIn(OrmBaseModel):
    name: str
    address: int
    description: str


class DeviceOut(DeviceIn):
    id: int


class DeviceList(OrmBaseModel):
    __root__: List[DeviceOut]
