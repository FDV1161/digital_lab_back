from flask import Blueprint, jsonify
from .Exception import NotFoundException, UniqueException, Unauthorized

bp = Blueprint('errors', __name__)


# @bp.app_errorhandler(404)
# def not_found_error_handler(_):
#     return "Anser errors"

@bp.app_errorhandler(Unauthorized)
def unauthorized(_):
    return jsonify(success=False,
                   data={'login_required': True},
                   message='Authorize please to access this page.'), 401


@bp.app_errorhandler(NotFoundException)
def not_found(_):
    return "not found", 404


@bp.app_errorhandler(UniqueException)
def not_found(_):
    return "not unique", 400
