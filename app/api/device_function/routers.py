from flask import Blueprint
from flask_pydantic import validate
from .shemas import DeviceFunctionCreate, DeviceFunctionUpdate, DeviceFunctionOut
from .crud import DeviceFunctionCRUD as Crud

bp = Blueprint('device_function', __name__)
crud = Crud()


@bp.route("", methods=["post"])
@validate(response_by_alias=True)
def create_device_function(body: DeviceFunctionCreate):
    device_function = crud.create_item(body)
    return DeviceFunctionOut.from_orm(device_function)


@bp.route("/<item_id>", methods=["put"])
@validate(response_by_alias=True)
def update_device_function(item_id: int, body: DeviceFunctionUpdate):
    device_function = crud.update_item(item_id, body)
    return DeviceFunctionOut.from_orm(device_function)


@bp.route("/<item_id>", methods=["delete"])
@validate(response_by_alias=True)
def delete_device_function(item_id: int):
    device_function = crud.delete_item(item_id)
    return {"object delete": device_function.id}
