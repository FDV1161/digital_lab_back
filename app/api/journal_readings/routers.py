from flask import Blueprint
from flask_pydantic import validate
from app.models import JournalReadings
from .shemas import JournalReadingsList
from app.api.base.functions import (
    get_items
)

bp = Blueprint('journal_readings', __name__)


@bp.route("", methods=["get"])
@validate(response_by_alias=True)
def get_journal_readings():
    journal_readings = get_items(JournalReadings)
    return JournalReadingsList.from_orm(journal_readings)
