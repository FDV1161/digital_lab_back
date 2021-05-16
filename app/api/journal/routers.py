from flask import Blueprint
from flask_pydantic import validate
from app.models import Journal
from .shemas import JournalIn, JournalOut
from app.api.base.functions import create_item

bp = Blueprint('journal', __name__)


@bp.route("", methods=["post"])
@validate(response_by_alias=True)
def create_journal(body: JournalIn):
    sensor = create_item(Journal, body)
    return JournalOut.from_orm(sensor)
