from typing import List
from typing import Optional

from app.api.base.shemas import OrmBaseModel
from app.api.device_function.shemas import DeviceFunctionList


class DeviceIn(OrmBaseModel):
    name: str
    room_id: int
    controller_id: int
    description: Optional[str]
    icon: Optional[str]


class DeviceOut(DeviceIn):
    id: int
    device_functions: DeviceFunctionList
    # @validator('icon')
    # def icon_path(cls, filename):
    #     if filename:
    #         return url_for("static_files", filename=filename)
    #         # return os.path.join(os.path.abspath(os.getcwd()), current_app.config['UPLOAD_FOLDER'], filename)
    #     return filename


class DeviceList(OrmBaseModel):
    __root__: List[DeviceOut]


class DeviceFilter(OrmBaseModel):
    on_home: Optional[bool]
