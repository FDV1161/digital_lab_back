from app.api.base.functions import BaseCRUD
from app.api.journal_readings.filter import JournalReadingsFilter
from app.models import JournalReadings
from database import session
from flask_sqlalchemy import Pagination


class JournalReadingsCRUD(BaseCRUD):
    model = JournalReadings
    filter = JournalReadingsFilter

    def get_items(self, filters=None, page=None, count=None):
        stmt = self.model.query
        if self.filter:
            stmt = self.filter().filter_query(stmt, filters.dict(exclude_unset=True))
        row_count = stmt.count()
        stmt = stmt.order_by(self.model.id.desc())
        if not page and not count:
            return stmt.all(), row_count
        return stmt.paginate(page, count, False).items, row_count
