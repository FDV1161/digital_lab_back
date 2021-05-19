from pydantic import BaseModel
from typing import List
from app.api.base.shemas import OrmBaseModel
# from app.api.measure.shemas import MeasureOut
from app.api.controller.shemas import ControllerOut
from app.api.journal.shemas import JournalList

from typing import Optional


class DeviceIn(OrmBaseModel):
    name: Optional[str]
    description: Optional[str]
    address: Optional[int]
    on_home: Optional[bool]
    room_id: Optional[int]
    controller_id: Optional[int]


class DeviceEditIn(DeviceIn):
    measure_id: int


class DeviceOut(DeviceIn):
    id: int
    # measure: Optional[MeasureOut]
    # journal_list: JournalList
    # controller: DeviceOut


class DeviceMinOut(DeviceIn):
    id: int
    # measure: Optional[MeasureOut]


class DeviceList(OrmBaseModel):
    __root__: List[DeviceMinOut]
