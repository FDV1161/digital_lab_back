from flask import Blueprint
from flask_pydantic import validate
from .shemas import ControllerIn, ControllerOut, ControllerList
from .crud import ControllerCRUD as Crud
from app.api.auth import token_auth

bp = Blueprint('controller', __name__)
crud = Crud()


@bp.route("", methods=["get"])
@validate(response_by_alias=True)
@token_auth.login_required
def get_controllers():
    controllers, _ = crud.get_items()
    return ControllerList.from_orm(controllers)


@bp.route("/<item_id>", methods=["get"])
@validate(response_by_alias=True)
@token_auth.login_required
def get_controller(item_id: int):
    controller = crud.get_item(item_id)
    return ControllerOut.from_orm(controller)


@bp.route("", methods=["post"])
@validate(response_by_alias=True)
@token_auth.login_required
def create_controller(body: ControllerIn):
    controller = crud.create_item(body)
    return ControllerOut.from_orm(controller)


@bp.route("/<item_id>", methods=["put"])
@validate(response_by_alias=True)
@token_auth.login_required
def update_controller(item_id: int, body: ControllerIn):
    controller = crud.update_item(item_id, body)
    return ControllerOut.from_orm(controller)


@bp.route("/<item_id>", methods=["delete"])
@validate(response_by_alias=True)
@token_auth.login_required
def delete_controller(item_id: int):
    controller = crud.delete_item(item_id)
    return {"object delete": controller.id}
