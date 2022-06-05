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
    values: List[JournalReadingsOut]
    row_count: Optional[int]
    max_value: Optional[float]
    avg_value: Optional[float]
    min_value: Optional[float]


class JournalReadingsFilter(OrmBaseModel):
    device_func_id: int
    updated_at_from: Optional[datetime]
    updated_at_to: Optional[datetime]


class JournalReadingsPagination(OrmBaseModel):
    paginate_page: Optional[int]
    pagination_count: Optional[int]


class JournalReadingsQuery(JournalReadingsFilter, JournalReadingsPagination):
    pass
  