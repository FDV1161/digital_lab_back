from flask import Blueprint
from flask_pydantic import validate
from .shemas import UserList, UserOut, UserUpdate, UserCreate
from .crud import UserCRUD as Crud

bp = Blueprint('users', __name__)
crud = Crud()


@bp.route("", methods=["get"])
@validate(response_by_alias=True)
# @login_required
def get_users():
    users, _ = crud.get_items()
    return UserList.from_orm(users)


@bp.route("/<item_id>", methods=["get"])
@validate(response_by_alias=True)
# @login_required
def get_user(item_id: int):
    user = crud.get_item(item_id)
    return UserOut.from_orm(user)


@bp.route("", methods=["post"])
@validate(response_by_alias=True)
# @login_required
def create_user(body: UserCreate):
    user = crud.create_item(body)
    return UserOut.from_orm(user)


@bp.route("/<item_id>", methods=["put"])
@validate(response_by_alias=True)
# @login_required
def update_user(item_id: int, body: UserUpdate):
    user = crud.update_item(item_id, body)
    return UserOut.from_orm(user)


@bp.route("/<item_id>", methods=["delete"])
@validate(response_by_alias=True)
# @login_required
def delete_user(item_id: int):
    user = crud.delete_item(item_id)
    return {"object delete": user.id}
