from app.api.base.functions import BaseCRUD
from app.api.journal_readings.filter import JournalReadingsFilter
from app.models import JournalReadings


class JournalReadingsCRUD(BaseCRUD):
    model = JournalReadings
    filter = JournalReadingsFilter
