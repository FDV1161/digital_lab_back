from typing import List, Optional
from app.api.base.shemas import OrmBaseModel
from datetime import datetime


class JournalReadingsIn(OrmBaseModel):
    value: float
    device_func_id: int


class JournalReadingsOut(JournalReadingsIn):
    id: int
    updated_at: datetime


class JournalReadingsList(OrmBaseModel):
    __root__: List[JournalReadingsOut]


class JournalReadingsFilter(OrmBaseModel):
    device_func_id: int
