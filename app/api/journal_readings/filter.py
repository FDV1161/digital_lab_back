from sqlalchemy_filter import fields, Filter
from app.models import JournalReadings


class JournalReadingsFilter(Filter):
    device_func_id = fields.Field(lookup_type="==")

    class Meta:
        model = JournalReadings
