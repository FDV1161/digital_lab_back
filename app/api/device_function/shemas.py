from typing import List, Optional

from pydantic import Field

from app.api.base.shemas import OrmBaseModel


# class FunctionOut(OrmBaseModel):
#     id: int
#     name: str
#     measure_symbol: str
from app.api.function.shemas import FunctionOut


class DeviceFunctionIn(OrmBaseModel):
    id: Optional[int]
    id_func: int
    id_device: Optional[int]
    address: int
    on_home: bool = Field(default=False)


class DeviceFunctionOut(OrmBaseModel):
    id: int
    func: FunctionOut
    id_device: int
    address: int
    on_home: bool = Field(default=False)


class DeviceFunctionList(OrmBaseModel):
    __root__: List[DeviceFunctionOut]
