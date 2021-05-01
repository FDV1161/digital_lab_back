from flask import Flask, Blueprint
from flask_pydantic import validate
from app.models import Room
from .shemas import RoomIn, RoomOut, RoomList, RoomDetailOut
from app.api.base.functions import (
    create_item,
    delete_item,
    update_item,
    get_item,
    get_items
)

bp = Blueprint('room', __name__)


@bp.route("", methods=["get"])
@validate()
def get_rooms():
    rooms = get_items(Room)
    return RoomList.from_orm(rooms)


@bp.route("/<item_id>", methods=["get"])
@validate()
def get_room(item_id: int):
    room = get_item(Room, item_id)
    return RoomDetailOut.from_orm(room)


@bp.route("", methods=["post"])
@validate()
def create_room(body: RoomIn):
    room = create_item(Room, body, fk_list)
    return RoomOut.from_orm(room)


@bp.route("/<item_id>", methods=["put"])
@validate()
def update_room(item_id: int, body: RoomIn):
    room = update_item(Room, item_id, body, fk_list)
    return RoomOut.from_orm(room)


@bp.route("/<item_id>", methods=["delete"])
@validate()
def delete_room(item_id: int):
    room = delete_item(Room, item_id)
    return {"object delete": room.id}
