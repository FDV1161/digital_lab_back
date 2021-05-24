from flask import Blueprint
from flask_pydantic import validate
from app.models import Function
from .shemas import FunctionIn, FunctionOut, FunctionList
from app.api.base.functions import (
    create_item,
    delete_item,
    update_item,
    get_item,
    get_items
)

bp = Blueprint('function', __name__)


@bp.route("", methods=["get"])
@validate(response_by_alias=True)
def get_functions():
    functions = get_items(Function)
    return FunctionList.from_orm(functions)


@bp.route("/<item_id>", methods=["get"])
@validate(response_by_alias=True)
def get_function(item_id: int):
    function = get_item(Function, item_id)
    return FunctionOut.from_orm(function)


@bp.route("", methods=["post"])
@validate(response_by_alias=True)
def create_function(body: FunctionIn):
    function = create_item(Function, body)
    return FunctionOut.from_orm(function)


@bp.route("/<item_id>", methods=["put"])
@validate(response_by_alias=True)
def update_function(item_id: int, body: FunctionIn):
    function = update_item(Function, item_id, body)
    return FunctionOut.from_orm(function)


@bp.route("/<item_id>", methods=["delete"])
@validate(response_by_alias=True)
def delete_function(item_id: int):
    function = delete_item(Function, item_id)
    return {"object delete": function.id}
