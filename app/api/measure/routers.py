from flask import Flask, Blueprint
from flask_pydantic import validate
from app.models import Measure
from .shemas import MeasureIn, MeasureOut, MeasureList
from app.api.base.functions import (
    create_item,
    delete_item,
    update_item,
    get_item,
    get_items
)

bp = Blueprint('measure', __name__)


@bp.route("", methods=["get"])
@validate()
def get_measures():
    measures = get_items(Measure)
    return MeasureList.from_orm(measures)


@bp.route("/<item_id>", methods=["get"])
@validate()
def get_measure(item_id: int):
    measure = get_item(Measure, item_id)
    return MeasureOut.from_orm(measure)


@bp.route("", methods=["post"])
@validate()
def create_measure(body: MeasureIn):
    measure = create_item(Measure, body)
    return MeasureOut.from_orm(measure)


@bp.route("/<item_id>", methods=["put"])
@validate()
def update_measure(item_id: int, body: MeasureIn):
    measure = update_item(Measure, item_id, body)
    return MeasureOut.from_orm(measure)


@bp.route("/<item_id>", methods=["delete"])
@validate()
def delete_measure(item_id: int):
    measure = delete_item(Measure, item_id)
    return {"object delete": measure.id}
