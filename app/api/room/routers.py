from flask import Flask, request, Blueprint
from flask_pydantic import validate
from database import session
from app.models import Room
from .shemas import RoomIn, RoomOut, RoomList
from app.errors.Exception import NotFoundException

bp = Blueprint('room', __name__)


@bp.route("", methods=["get"])
@validate()
def get_rooms():
    rooms = session.query(Room).all()
    return RoomList.from_orm(rooms)


@bp.route("/<item_id>", methods=["get"])
@validate()
def get_room(item_id: int):
    room = session.query(Room).get(item_id)
    if not room:
        raise NotFoundException
    return RoomOut.from_orm(room)

# TODO проверка на уникальность


@bp.route("", methods=["post"])
@validate()
def create_room(body: RoomIn):
    room = Room(**body.dict())
    session.add(room)
    session.commit()
    return RoomOut.from_orm(room)

# TODO проверка на уникальность


@bp.route("/<item_id>", methods=["put"])
@validate()
def update_room(item_id: int, body: RoomIn):
    room = session.query(Room).get(item_id)
    if not room:
        raise NotFoundException
    param = body.dict()
    for attr, value in param.items():
        setattr(room, attr, value)
    session.add(room)
    session.commit()
    return RoomOut.from_orm(room)


@bp.route("/<item_id>", methods=["delete"])
@validate()
def delete_room(item_id: int):
    session.query(Room).filter(Room.id == item_id).delete()
    session.commit()
    return {"object delete": item_id}
