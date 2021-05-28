from typing import List

from pydantic import Field

from app.api.base.shemas import OrmBaseModel


class DeviceFunctionIn(OrmBaseModel):
    id_func: int
    id_device: int
    address: int
    on_home: bool = Field(default=False)


class DeviceFunctionOut(DeviceFunctionIn):
    id: int


class DeviceFunctionList(OrmBaseModel):
    __root__: List[DeviceFunctionOut]
