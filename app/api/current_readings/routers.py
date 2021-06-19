from flask import Blueprint
from flask_pydantic import validate
from .shemas import CurrentReadingsList, CurrentReadingsIn, CurrentReadingsOut
from .crud import CurrentReadingsCRUD as Crud

bp = Blueprint('current_readings', __name__)
crud = Crud()


@bp.route("", methods=["post"])
@validate(response_by_alias=True)
def create_current_readings(body: CurrentReadingsIn):
    current_readings = crud.create_item(body)
    return CurrentReadingsOut.from_orm(current_readings)


@bp.route("", methods=["get"])
@validate(response_by_alias=True)
def get_current_readings():
    current_readings = crud.get_items()
    return CurrentReadingsList.from_orm(current_readings)
