from flask import Blueprint
from flask_pydantic import validate
from app.models import Controller
from .shemas import ControllerIn, ControllerOut, ControllerList
from app.api.base.functions import (
    create_item,
    delete_item,
    update_item,
    get_item,
    get_items
)

bp = Blueprint('controller', __name__)


@bp.route("", methods=["get"])
@validate(response_by_alias=True)
def get_controllers():
    controllers = get_items(Controller)
    return ControllerList.from_orm(controllers)


@bp.route("/<item_id>", methods=["get"])
@validate(response_by_alias=True)
def get_controller(item_id: int):
    controller = get_item(Controller, item_id)
    return ControllerOut.from_orm(controller)


@bp.route("", methods=["post"])
@validate(response_by_alias=True)
def create_controller(body: ControllerIn):
    controller = create_item(Controller, body)
    return ControllerOut.from_orm(controller)


@bp.route("/<item_id>", methods=["put"])
@validate(response_by_alias=True)
def update_controller(item_id: int, body: ControllerIn):
    controller = update_item(Controller, item_id, body)
    return ControllerOut.from_orm(controller)


@bp.route("/<item_id>", methods=["delete"])
@validate(response_by_alias=True)
def delete_controller(item_id: int):
    controller = delete_item(Controller, item_id)
    return {"object delete": controller.id}
