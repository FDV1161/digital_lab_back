from flask import Flask, Blueprint
from flask_pydantic import validate
from app.models import Device
from .shemas import DeviceIn, DeviceOut, DeviceList
from app.api.base.functions import (
    create_item,
    delete_item,
    update_item,
    get_item,
    get_items
)

bp = Blueprint('device', __name__)


@bp.route("", methods=["get"])
@validate()
def get_devices():
    devices = get_items(Device)
    return DeviceList.from_orm(devices)


@bp.route("/<item_id>", methods=["get"])
@validate()
def get_device(item_id: int):
    device = get_item(Device, item_id)
    return DeviceOut.from_orm(device)


@bp.route("", methods=["post"])
@validate()
def create_device(body: DeviceIn):
    device = create_item(Device, body)
    return DeviceOut.from_orm(device)


@bp.route("/<item_id>", methods=["put"])
@validate()
def update_device(item_id: int, body: DeviceIn):
    device = update_item(Device, item_id, body)
    return DeviceOut.from_orm(device)


@bp.route("/<item_id>", methods=["delete"])
@validate()
def delete_device(item_id: int):
    device = delete_item(Device, item_id)
    return {"object delete": device.id}
