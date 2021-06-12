from flask import Blueprint
from flask_pydantic import validate
from app.models import JournalReadings
from .shemas import JournalReadingsList, JournalReadingsOut, JournalReadingsIn
from app.api.base.functions import (
    create_item
)
from database import session, db

bp = Blueprint('journal_readings', __name__)


@bp.route("", methods=["post"])
@validate(response_by_alias=True)
def create_current_readings(body: JournalReadingsIn):
    current_readings = create_item(JournalReadings, body)
    return JournalReadingsOut.from_orm(current_readings)


@bp.route("/<device_func_id>", methods=["get"])
@validate(response_by_alias=True)
def get_journal_readings(device_func_id: int):
    journal_readings = session.query(JournalReadings).filter(JournalReadings.device_func_id==device_func_id).all()
    return JournalReadingsList.from_orm(journal_readings)
