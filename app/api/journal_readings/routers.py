from flask import Blueprint
from flask_pydantic import validate
from app.models import JournalReadings
from .shemas import JournalReadingsList, JournalReadingsOut, JournalReadingsIn, JournalReadingsFilter
from database import session
from .crud import JournalReadingsCRUD as Crud

bp = Blueprint('journal_readings', __name__)
crud = Crud()


@bp.route("", methods=["post"])
@validate(response_by_alias=True)
def create_journal_readings(body: JournalReadingsIn):
    journal_readings = crud.create_item(body)
    return JournalReadingsOut.from_orm(journal_readings)


@bp.route("/", methods=["get"])
@validate(response_by_alias=True)
def get_journal_readings(query: JournalReadingsFilter):
    journal_readings = crud.get_items(filters=query)
    # journal_readings = session.query(JournalReadings).filter(JournalReadings.device_func_id == query).all()
    return JournalReadingsList.from_orm(journal_readings)
