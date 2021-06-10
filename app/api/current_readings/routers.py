from flask import Blueprint
from flask_pydantic import validate
from app.models import CurrentReadings
from .shemas import CurrentReadingsList, CurrentReadingsIn, CurrentReadingsOut
from app.api.base.functions import (
    get_items, create_item
)

bp = Blueprint('current_readings', __name__)


@bp.route("", methods=["post"])
@validate(response_by_alias=True)
def create_current_readings(body: CurrentReadingsIn):
    current_readings = create_item(CurrentReadings, body)
    return CurrentReadingsOut.from_orm(current_readings)


@bp.route("", methods=["get"])
@validate(response_by_alias=True)
def get_current_readings():
    current_readings = get_items(CurrentReadings)
    return CurrentReadingsList.from_orm(current_readings)
