from typing import List, Optional
from app.api.base.shemas import OrmBaseModel


class RoomIn(OrmBaseModel):
    name: str
    description: Optional[str]


class RoomOut(RoomIn):
    id: int


class RoomDetailOut(RoomIn):
    id: int


class RoomList(OrmBaseModel):
    __root__: List[RoomOut]
