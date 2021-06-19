from flask import Blueprint
from flask_pydantic import validate
from .shemas import RoomIn, RoomOut, RoomList
from flask_login import login_required
from .crud import RoomCRUD as Crud

bp = Blueprint('room', __name__)
crud = Crud()


@bp.route("", methods=["get"])
@validate(response_by_alias=True)
# @login_required
def get_rooms():
    rooms = crud.get_items()
    return RoomList.from_orm(rooms)


@bp.route("/<item_id>", methods=["get"])
@validate(response_by_alias=True)
def get_room(item_id: int):
    room = crud.get_item(item_id)
    return RoomOut.from_orm(room)


@bp.route("", methods=["post"])
@validate(response_by_alias=True)
def create_room(body: RoomIn):
    room = crud.create_item(body)
    return RoomOut.from_orm(room)


@bp.route("/<item_id>", methods=["put"])
@validate(response_by_alias=True)
def update_room(item_id: int, body: RoomIn):
    room = crud.update_item(item_id, body)
    return RoomOut.from_orm(room)


@bp.route("/<item_id>", methods=["delete"])
@validate(response_by_alias=True)
def delete_room(item_id: int):
    room = crud.delete_item(item_id)
    return {"object delete": room.id}
