from flask import Flask, request, Blueprint
from flask_pydantic import validate
from database import session
from app.models import Sensor
from .shemas import SensorIn, SensorOut, SensorList
from app.errors.Exception import NotFoundException

bp = Blueprint('sensor', __name__)


@bp.route("", methods=["get"])
@validate()
def get_sensors():
    sensors = session.query(Sensor).all()
    return SensorList.from_orm(sensors)


@bp.route("/<item_id>", methods=["get"])
@validate()
def get_sensor(item_id: int):
    sensor = session.query(Sensor).get(item_id)
    if not sensor:
        raise NotFoundException
    return SensorOut.from_orm(sensor)


@bp.route("", methods=["post"])
@validate()
def create_sensor(body: SensorIn):    
    sensor = Sensor(**body.dict())
    session.add(sensor)
    session.commit()
    return SensorOut.from_orm(sensor)


@bp.route("/<item_id>", methods=["put"])
@validate()
def update_sensor(item_id: int, body: SensorIn):
    sensor = session.query(Sensor).get(item_id)
    if not sensor:
        raise NotFoundException    
    param = body.dict()
    for attr, value in param.items():
        setattr(sensor, attr, value)    
    session.add(sensor)
    session.commit()    
    return SensorOut.from_orm(sensor)


@bp.route("/<item_id>", methods=["delete"])
@validate()
def delete_sensor(item_id: int):
    session.query(Sensor).filter(Sensor.id == item_id).delete()
    session.commit()
    return {"object delete": item_id}
