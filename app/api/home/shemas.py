# from pydantic import Field
# from typing import List, Optional
# from app.api.base.shemas import OrmBaseModel


# class OnHomeCurrentValue(OrmBaseModel):
#     room_id: int
#     room_name: str
#     min_value: int
#     max_value: int
#     write_enable: Optional[bool] = Field(default=False)
#     icon: Optional[str]
#     cur_val: Optional[int]
#     measure_symbol: Optional[str]


# class OnHomeCurrentValueList(OrmBaseModel):
#     __root__: List[OnHomeCurrentValue]

from pydantic import Field
from typing import List, Optional
from app.api.base.shemas import OrmBaseModel

class CurrentReading(OrmBaseModel):
    min_value: int
    max_value: int
    write_enable: Optional[bool] = Field(default=False)
    icon: Optional[str]
    cur_val: Optional[int]
    measure_symbol: Optional[str]
    id: int


class Room(OrmBaseModel):
    id: int
    name: str
    current_readings: List[CurrentReading]


class RoomList(OrmBaseModel):
    __root__: List[Room]
