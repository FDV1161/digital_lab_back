from typing import List
from app.api.base.shemas import OrmBaseModel
from datetime import datetime


class CurrentReadingsIn(OrmBaseModel):
    value: float
    device_func_id: int


class CurrentReadingsOut(CurrentReadingsIn):
    id: int
    updated_at: datetime


class CurrentReadingsList(OrmBaseModel):
    __root__: List[CurrentReadingsOut]
