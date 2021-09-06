from flask import Blueprint
from flask_pydantic import validate
from .shemas import CurrentReadingsList, CurrentReadingsIn, CurrentReadingsOut
from .crud import CurrentReadingsCRUD as Crud
from app.api.auth import token_auth

bp = Blueprint('current_readings', __name__)
crud = Crud()


@bp.route("", methods=["post"])
@validate(response_by_alias=True)
@token_auth.login_required
def create_current_readings(body: CurrentReadingsIn):
    current_readings = crud.create_item(body)
    return CurrentReadingsOut.from_orm(current_readings)


@bp.route("", methods=["get"])
@validate(response_by_alias=True)
@token_auth.login_required
def get_current_readings():
    current_readings, _ = crud.get_items()
    return CurrentReadingsList.from_orm(current_readings)
