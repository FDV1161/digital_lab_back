from typing import List, Optional

from pydantic import Field

from app.api.base.shemas import OrmBaseModel


class DeviceFunctionIn(OrmBaseModel):
    id: Optional[int]
    id_func: int
    id_device: int
    address: int
    on_home: bool = Field(default=False)


class DeviceFunctionOut(DeviceFunctionIn):
    pass


class DeviceFunctionList(OrmBaseModel):
    __root__: List[DeviceFunctionOut]
