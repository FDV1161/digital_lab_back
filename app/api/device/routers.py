from flask import Blueprint, request
from flask_pydantic import validate
from .shemas import DeviceOut, DeviceList, DeviceIn
from ..file.utils import upload_file
from .crud import DeviceCRUD as Crud

bp = Blueprint('device', __name__)
crud = Crud()


@bp.route("", methods=["get"])
@validate(response_by_alias=True)
def get_devices():
    devices = crud.get_items()
    return DeviceList.from_orm(devices)


@bp.route("/<item_id>", methods=["get"])
@validate(response_by_alias=True)
def get_device(item_id: int):
    device = crud.get_item(item_id)
    return DeviceOut.from_orm(device)


@bp.route("", methods=["post"])
@validate(response_by_alias=True)
def create_device(body: DeviceIn):
    device = crud.create_item(body)
    return DeviceOut.from_orm(device)


@bp.route("/<item_id>", methods=["put"])
@validate(response_by_alias=True)
def update_device(item_id: int, body: DeviceIn):
    device = crud.update_item(item_id, body)
    return DeviceOut.from_orm(device)


@bp.route("/<item_id>", methods=["delete"])
@validate(response_by_alias=True)
def delete_device(item_id: int):
    device = crud.delete_item(item_id)
    return {"object delete": device.id}


@bp.route("/upload_file", methods=["post"])
def upload_file_router():
    file_name = upload_file(request.files.get('file'))
    return {"icon_path": file_name}
