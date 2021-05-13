from flask import Blueprint
from .Exception import NotFoundException, UniqueException


bp = Blueprint('errors', __name__)


@bp.app_errorhandler(404)
def not_found_error_handler(_):
    return "Anser errors"


@bp.app_errorhandler(NotFoundException)
def not_found(_):
    return "not found"



@bp.app_errorhandler(UniqueException)
def not_found(_):
    return "not unique", 400

