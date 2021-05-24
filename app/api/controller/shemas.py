from typing import List, Optional
from app.api.base.shemas import OrmBaseModel


class ControllerIn(OrmBaseModel):
    name: str
    address: int
    protocol: int
    port: str
    description: Optional[str]


class ControllerOut(ControllerIn):
    id: int


class ControllerList(OrmBaseModel):
    __root__: List[ControllerOut]
