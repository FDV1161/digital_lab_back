from . import bp

@bp.app_errorhandler(404)
def not_found_error_handler(_):
    return "Anser errors"
