from sqlalchemy_filter import fields, Filter
from app.models import JournalReadings


class JournalReadingsFilter(Filter):
    device_func_id = fields.Field(lookup_type="==")
    updated_at_from = fields.DateTimeField(field_name="updated_at", lookup_type=">=")
    updated_at_to = fields.DateTimeField(field_name="updated_at", lookup_type="<=")    

    class Meta:
        model = JournalReadings
