from datetime import datetime
from typing import List
from app.api.base.shemas import OrmBaseModel
from datetime import datetime


class JournalIn(OrmBaseModel):
    value: float
    sensor_id: int


class JournalOut(OrmBaseModel):
    value: float
    created_at: datetime


class JournalList(OrmBaseModel):
    __root__: List[JournalOut]
