from flask import Flask, request, Blueprint
from flask_pydantic import validate
from database import session
from app.models import Measure
from .shemas import MeasureIn, MeasureOut, MeasureList
from app.errors.Exception import NotFoundException

bp = Blueprint('measure', __name__)


@bp.route("", methods=["get"])
@validate()
def get_measures():
    measures = session.query(Measure).all()
    return MeasureList.from_orm(measures)


@bp.route("/<item_id>", methods=["get"])
@validate()
def get_measure(item_id: int):
    measure = session.query(Measure).get(item_id)
    if not measure:
        raise NotFoundException
    return MeasureOut.from_orm(measure)


@bp.route("", methods=["post"])
@validate()
def create_measure(body: MeasureIn):    
    measure = Measure(**body.dict())
    session.add(measure)
    session.commit()
    return MeasureOut.from_orm(measure)


@bp.route("/<item_id>", methods=["put"])
@validate()
def update_measure(item_id: int, body: MeasureIn):
    measure = session.query(Measure).get(item_id)
    if not measure:
        raise NotFoundException    
    param = body.dict()
    for attr, value in param.items():
        setattr(measure, attr, value)    
    session.add(measure)
    session.commit()    
    return MeasureOut.from_orm(measure)


@bp.route("/<item_id>", methods=["delete"])
@validate()
def delete_measure(item_id: int):
    session.query(Measure).filter(Measure.id == item_id).delete()
    session.commit()
    return {"object delete": item_id}
