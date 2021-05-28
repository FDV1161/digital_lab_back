from flask import Blueprint, request
from flask_pydantic import validate
from app.models import Device
from .shemas import DeviceOut, DeviceList, DeviceIn
from app.api.base.functions import (
    create_item,
    delete_item,
    update_item,
    get_item,
    get_items,
    upload_file_item
)
from ..file.utils import upload_file

bp = Blueprint('device', __name__)


@bp.route("", methods=["get"])
@validate(response_by_alias=True)
def get_devices():
    devices = get_items(Device)
    return DeviceList.from_orm(devices)


@bp.route("/<item_id>", methods=["get"])
@validate(response_by_alias=True)
def get_device(item_id: int):
    device = get_item(Device, item_id)
    return DeviceOut.from_orm(device)


@bp.route("", methods=["post"])
@validate(response_by_alias=True)
def create_device(body: DeviceIn):
    # body.icon = upload_file(request.files.get('file'))
    device = create_item(Device, body)
    return DeviceOut.from_orm(device)


@bp.route("/<item_id>", methods=["put"])
@validate(response_by_alias=True)
def update_device(item_id: int, body: DeviceIn):
    # file_name = upload_file(request.files.get('file'))
    # if file_name:
    #     body.icon = file_name
    device = update_item(Device, item_id, body)
    return DeviceOut.from_orm(device)


@bp.route("/<item_id>", methods=["delete"])
@validate(response_by_alias=True)
def delete_device(item_id: int):
    device = delete_item(Device, item_id)
    return {"object delete": device.id}


# @bp.route("/<item_id>/upload_file", methods=["post"])
# @validate(response_by_alias=True)
# def upload_file_router(item_id: int):
#     file_name = upload_file(request.files.get('file'))
#     device = upload_file_item(Device, item_id, file_name)
#     return DeviceOut.from_orm(device)  # {"file loaded": file_name}


@bp.route("/upload_file", methods=["post"])
def upload_file_router():
    file_name = upload_file(request.files.get('file'))
    return file_name
