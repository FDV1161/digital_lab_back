from typing import List
from app.api.base.shemas import OrmBaseModel


class ControllerIn(OrmBaseModel):
    name: str
    address: int
    description: str


class ControllerOut(ControllerIn):
    id: int


class ControllerList(OrmBaseModel):
    __root__: List[ControllerOut]
