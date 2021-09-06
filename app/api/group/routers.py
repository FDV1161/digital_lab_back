from flask import Blueprint
from flask_pydantic import validate
from .shemas import GroupList
from .crud import RoomCRUD as Crud
from app.api.auth import token_auth

bp = Blueprint('group', __name__)
crud = Crud()


@bp.route("", methods=["get"])
@validate(response_by_alias=True)
@token_auth.login_required
def get_groups():
    groups, _ = crud.get_items()
    return GroupList.from_orm(groups)
