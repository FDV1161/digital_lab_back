from flask import Blueprint
from flask_pydantic import validate
from app.models import JournalReadings
from .shemas import JournalReadingsList, JournalReadingsOut, JournalReadingsIn, JournalReadingsQuery, JournalReadingsFilter
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
def get_journal_readings(query: JournalReadingsQuery):
    filters = JournalReadingsFilter.parse_obj(query.dict())
    journal_readings, row_count = crud.get_items(
        filters=filters, page=query.paginate_page, count=query.pagination_count)
    return JournalReadingsList(values=journal_readings, row_count=row_count)
