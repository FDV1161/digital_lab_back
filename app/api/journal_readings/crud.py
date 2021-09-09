from app.api.base.functions import BaseCRUD
from app.api.journal_readings.filter import JournalReadingsFilter
from app.models import JournalReadings
from database import session


class JournalReadingsCRUD(BaseCRUD):
    model = JournalReadings
    filter = JournalReadingsFilter

    def get_items(self, filters = None, page=1, count=10):        
        stmt = self.model.query
        if self.filter:
            stmt = self.filter().filter_query(stmt, filters.dict(exclude_unset=True))        
        row_count = stmt.count()
        stmt = stmt.order_by(self.model.id.desc())
        return stmt.paginate(page, count, False).items, row_count