from pydantic import BaseModel
from typing import List
from app.api.base.shemas import OrmBaseModel
from app.api.measure.shemas import MeasureOut
from app.api.device.shemas import DeviceOut
from app.api.journal.shemas import JournalList

from typing import Optional


class SensorIn(OrmBaseModel):
    name: Optional[str]
    description: Optional[str]
    address: Optional[int]
    on_home: Optional[bool]
    room_id: Optional[int]
    device_id: Optional[int]


class SensorEditIn(SensorIn):
    measure_id: int


class SensorOut(SensorIn):
    id: int
    measure: Optional[MeasureOut]
    journal_list: JournalList
    # device: DeviceOut


class SensorMinOut(SensorIn):
    id: int
    measure: Optional[MeasureOut]


class SensorList(OrmBaseModel):
    __root__: List[SensorMinOut]
