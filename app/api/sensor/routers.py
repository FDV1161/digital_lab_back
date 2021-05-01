from flask import Flask, Blueprint
from flask_pydantic import validate
from app.models import Sensor
from .shemas import SensorOut, SensorList, SensorEditIn
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
    sensors = get_items(Sensor)
    return SensorList.from_orm(sensors)


@bp.route("/<item_id>", methods=["get"])
@validate()
def get_sensor(item_id: int):
    sensor = get_item(Sensor, item_id)
    return SensorOut.from_orm(sensor)


@bp.route("", methods=["post"])
@validate()
def create_sensor(body: SensorEditIn):    
    sensor = create_item(Sensor, body)
    return SensorOut.from_orm(sensor)


@bp.route("/<item_id>", methods=["put"])
@validate()
def update_sensor(item_id: int, body: SensorEditIn):    
    sensor = update_item(Sensor, item_id, body)
    return SensorOut.from_orm(sensor)


@bp.route("/<item_id>", methods=["delete"])
@validate()
def delete_sensor(item_id: int):
    sensor = delete_item(Sensor, item_id)
    return {"object delete": sensor.id}
