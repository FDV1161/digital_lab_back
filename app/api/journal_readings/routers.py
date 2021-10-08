from flask import Blueprint, make_response, send_file
from flask_pydantic import validate
from app.models import JournalReadings
from .shemas import JournalReadingsList, JournalReadingsOut, JournalReadingsIn, JournalReadingsQuery, JournalReadingsFilter
from database import session
from .crud import JournalReadingsCRUD as Crud
from app.api.auth import token_auth
from io import StringIO
from csv import writer

bp = Blueprint('journal_readings', __name__)
crud = Crud()


@bp.route('/export_csv/', methods=["get"])
@validate(response_by_alias=True)
@token_auth.login_required
def export_csv(query: JournalReadingsQuery):
    filters = JournalReadingsFilter.parse_obj(query.dict())
    journal_readings, _ = crud.get_items(
        filters=filters, page=query.paginate_page, count=query.pagination_count)
    export_columns = ['updated_at', 'value']
    si = StringIO()
    cw = writer(si)
    cw.writerow(export_columns)
    for value in journal_readings:
        cw.writerow([str(getattr(value, col)) for col in export_columns])
    output = make_response(si.getvalue().encode())
    output.headers["Content-Disposition"] = "attachment; filename=export.csv"
    output.headers["Content-type"] = "text/csv"
    return output


@bp.route("", methods=["post"])
@validate(response_by_alias=True)
@token_auth.login_required
def create_journal_readings(body: JournalReadingsIn):
    journal_readings = crud.create_item(body)
    return JournalReadingsOut.from_orm(journal_readings)


@bp.route("/", methods=["get"])
@validate(response_by_alias=True)
@token_auth.login_required
def get_journal_readings(query: JournalReadingsQuery):
    filters = JournalReadingsFilter.parse_obj(query.dict())
    journal_readings, row_count = crud.get_items(
        filters=filters, page=query.paginate_page, count=query.pagination_count)
    return JournalReadingsList(values=journal_readings, row_count=row_count)
