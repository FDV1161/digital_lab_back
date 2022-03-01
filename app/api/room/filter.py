from sqlalchemy_filter import fields, Filter
from app.models import Room


class RoomFilter(Filter):
    on_home = fields.Field(field_name="on_home", lookup_type="==", relation_model="DeviceFunction")

    class Meta:
        model = Room
