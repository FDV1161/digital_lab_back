from flask import Blueprint
from flask_pydantic import validate
from .shemas import FunctionIn, FunctionOut, FunctionList
from .curd import FunctionCRUD as Crud

bp = Blueprint('function', __name__)
crud = Crud()


@bp.route("", methods=["get"])
@validate(response_by_alias=True)
def get_functions():
    functions, _ = crud.get_items()
    return FunctionList.from_orm(functions)


@bp.route("/<item_id>", methods=["get"])
@validate(response_by_alias=True)
def get_function(item_id: int):
    function = crud.get_item(item_id)
    return FunctionOut.from_orm(function)


@bp.route("", methods=["post"])
@validate(response_by_alias=True)
def create_function(body: FunctionIn):
    function = crud.create_item(body)
    return FunctionOut.from_orm(function)


@bp.route("/<item_id>", methods=["put"])
@validate(response_by_alias=True)
def update_function(item_id: int, body: FunctionIn):
    function = crud.update_item(item_id, body)
    return FunctionOut.from_orm(function)


@bp.route("/<item_id>", methods=["delete"])
@validate(response_by_alias=True)
def delete_function(item_id: int):
    function = crud.delete_item(item_id)
    return {"object delete": function.id}
