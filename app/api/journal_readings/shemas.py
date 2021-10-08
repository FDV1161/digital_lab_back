from typing import List, Optional
from flask_sqlalchemy import Pagination
from pydantic import Field
from app.api.base.shemas import OrmBaseModel
from datetime import datetime


class JournalReadingsIn(OrmBaseModel):
    value: float
    device_func_id: int


class JournalReadingsOut(JournalReadingsIn):
    id: int
    updated_at: datetime    


class JournalReadingsList(OrmBaseModel):
    values: List[JournalReadingsOut]
    row_count: Optional[int]


class JournalReadingsFilter(OrmBaseModel):
    device_func_id: int


class JournalReadingsPagination(OrmBaseModel):
    paginate_page: Optional[int]
    pagination_count: Optional[int]


class JournalReadingsQuery(JournalReadingsFilter, JournalReadingsPagination):
    pass
  