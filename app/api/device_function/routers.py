from flask import Blueprint, current_app
from flask_pydantic import validate
from .shemas import DeviceFunctionCreate, DeviceFunctionUpdate, DeviceFunctionOut, DeviceFunctionRunner
from .crud import DeviceFunctionCRUD as Crud
from subprocess import Popen
from app.api.auth import token_auth

bp = Blueprint('device_function', __name__)
crud = Crud()


@bp.route("/<item_id>", methods=["get"])
@validate(response_by_alias=True)
@token_auth.login_required
def get_device_function(item_id: int):
    item = crud.get_item(item_id)
    return DeviceFunctionOut.from_orm(item)


@bp.route("", methods=["post"])
@validate(response_by_alias=True)
@token_auth.login_required
def create_device_function(body: DeviceFunctionCreate):
    device_function = crud.create_item(body)
    return DeviceFunctionOut.from_orm(device_function)


@bp.route("/<item_id>", methods=["put"])
@validate(response_by_alias=True)
@token_auth.login_required
def update_device_function(item_id: int, body: DeviceFunctionUpdate):
    device_function = crud.update_item(item_id, body)
    return DeviceFunctionOut.from_orm(device_function)


@bp.route("/<item_id>", methods=["delete"])
@validate(response_by_alias=True)
@token_auth.login_required
def delete_device_function(item_id: int):
    device_function = crud.delete_item(item_id)
    return {"object delete": device_function.id}


@bp.route("/run", methods=["post"])
@validate(response_by_alias=True)
@token_auth.login_required
def run_device_function(body: DeviceFunctionRunner):
    folder = current_app.config['SCRIPTS_FOLDER']
    interpreter = current_app.config['SCRIPTS_INTERPRETER']
    process = Popen([interpreter, folder + "script.py", str(body.id), str(body.value)])
    return body
