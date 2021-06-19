from app.api.base.functions import BaseCRUD
from app.models import DeviceFunction, Function, Device


class DeviceFunctionCRUD(BaseCRUD):
    model = DeviceFunction
    foreign_keys = {"id_func": Function, "id_device": Device}
