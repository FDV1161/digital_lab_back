from flask import Blueprint
from .Exception import NotFoundException


bp = Blueprint('errors', __name__)


@bp.app_errorhandler(404)
def not_found_error_handler(_):
    return "Anser errors"


@bp.app_errorhandler(NotFoundException)
def not_found(_):
    return "not found"
