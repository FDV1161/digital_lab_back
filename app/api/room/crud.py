from app.api.base.functions import BaseCRUD
from app.api.room.filter import RoomFilter
from app.models import Room, Device, DeviceFunction


class RoomCRUD(BaseCRUD):
    model = Room
    filter = RoomFilter

    def _filter_items(self, stmt, filters):
        filters = filters.dict(exclude_unset=True)
        on_home = filters.pop("on_home", None)
        if on_home is not None:
            stmt = stmt.join(Device).join(DeviceFunction).filter(DeviceFunction.on_home == on_home)
        return self.filter().filter_query(stmt, filters)
