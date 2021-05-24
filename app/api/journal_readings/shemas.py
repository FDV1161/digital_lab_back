from typing import List
from app.api.base.shemas import OrmBaseModel
from datetime import datetime


class JournalReadingsIn(OrmBaseModel):
    value: float
    device_func_id: int


class JournalReadingsOut(JournalReadingsIn):
    id: int
    created_at: datetime


class JournalReadingsList(OrmBaseModel):
    __root__: List[JournalReadingsOut]
