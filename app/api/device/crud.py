from app.api.base.functions import BaseCRUD
from app.api.device.filter import DeviceFilter
from app.models import Device, DeviceFunction, Room, Controller


class DeviceCRUD(BaseCRUD):
    model = Device
    foreign_keys = {"room_id": Room, "controller_id": Controller, "device_functions": DeviceFunction}
    filter = DeviceFilter
