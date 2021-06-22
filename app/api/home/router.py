from sqlalchemy.sql.expression import null
from app.api.home.shemas import RoomList
from flask import Blueprint, request
from flask_pydantic import validate
from database import session, db
from app.models import DeviceFunction, Device, Function, Room


bp = Blueprint('home', __name__)


@bp.route("/current_readings", methods=["get"])
@validate(response_by_alias=True)
def get_devices():
    on_home_query = session.query(DeviceFunction, Device, Room, Function) \
        .join(Function, DeviceFunction.id_func == Function.id) \
        .join(Device, Device.id == DeviceFunction.id_device) \
        .join(Room, Room.id == Device.room_id) \
        .filter(DeviceFunction.on_home == True) \
        .all()
    # on_home_current_values = []
    # for df, device, room, func in on_home_query:
    #     on_home_current_values.append({
    #         # "cur_val": df.cur_val,
    #         # "write_enable": df.write_enable,
    #         "measure_symbol": func.measure_symbol,
    #         "min_value": func.min_value,
    #         "max_value": func.max_value,
    #         "icon": device.icon,
    #         "room_id": room.id,
    #         "room_name": room.name
    #     })

    on_home_current_values = {}
    for df, device, room, func in on_home_query:
        room_obj = on_home_current_values.get(room.id, None)
        current_values = {
            "measure_symbol": func.measure_symbol,
            "min_value": func.min_value,
            "max_value": func.max_value,
            "icon": device.icon,
            "cur_val": df.cur_val,
            "write_enable": df.write_enable,
            "id": df.id
        }
        if room_obj:
            room_obj["current_readings"].append(current_values)
        else:
            on_home_current_values[room.id] = {
                "id": room.id,
                "name": room.name,
                "current_readings": [current_values]
            }

    # on_home_current_values2 = []
    # a.values()
    # [v for v in on_home_current_values]
    on_home_current_values = [v for v in on_home_current_values.values()]
    return RoomList.parse_obj(on_home_current_values)
