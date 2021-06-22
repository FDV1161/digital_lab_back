from pydantic import Field
from typing import List, Optional
from app.api.base.shemas import OrmBaseModel
from app.api.function.shemas import FunctionOut
from datetime import datetime


class DeviceFunctionCreate(OrmBaseModel):
    id_func: int
    id_device: int
    address: int
    on_home: bool = Field(default=False)


class DeviceFunctionUpdate(OrmBaseModel):
    address: int
    on_home: bool = Field(default=False)


class DeviceFunctionOut(OrmBaseModel):
    id: int
    address: int
    id_device: int
    on_home: bool = Field(default=False)
    multiply: Optional[float]
    write_enable: Optional[bool]
    cur_val: Optional[float]
    updated_at: Optional[datetime]
    func: FunctionOut


class DeviceFunctionList(OrmBaseModel):
    __root__: List[DeviceFunctionOut]
