from flask import Flask, request, Blueprint
from flask_pydantic import validate
from database import session
from app.models import Sensor, Measure
from .shemas import SensorIn, SensorOut, SensorList
from app.errors.Exception import NotFoundException
from app.api.base.functions import (
    create_item,
    delete_item,
    update_item,
    get_item,
    get_items
)

bp = Blueprint('sensor', __name__)


@bp.route("", methods=["get"])
@validate()
def get_sensors():
    return get_items(Sensor)


@bp.route("/<item_id>", methods=["get"])
@validate()
def get_sensor(item_id: int):
    sensor = get_item(Sensor, item_id)
    return SensorOut.from_orm(sensor)


@bp.route("", methods=["post"])
@validate()
def create_sensor(body: SensorIn):
    fk_list = {"measure": Measure}
    sensor = create_item(Sensor, body, fk_list)
    return SensorOut.from_orm(sensor)


@bp.route("/<item_id>", methods=["put"])
@validate()
def update_sensor(item_id: int, body: SensorIn):
    fk_list = {"measure": Measure}
    sensor = update_item(Sensor, item_id, body, fk_list)
    return SensorOut.from_orm(sensor)


@bp.route("/<item_id>", methods=["delete"])
@validate()
def delete_sensor(item_id: int):
    sensor = delete_item(Sensor, item_id)
    return {"object delete": sensor.id}
