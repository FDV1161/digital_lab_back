from pydantic import BaseModel
from typing import List


class OrmBaseModel(BaseModel):
    class Config:
        orm_mode = True


class RoomIn(OrmBaseModel):
    name: str 
    description: str


class RoomOut(RoomIn):
    id: int


# class RoomList(OrmBaseModel):
#     object_list = List[RoomOut]

class RoomList(OrmBaseModel):
    __root__: List[RoomOut]