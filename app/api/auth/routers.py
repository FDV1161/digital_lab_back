from flask.json import jsonify
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from flask import Blueprint
from app.models import User
from app.errors.Exception import Unauthorized
from flask_pydantic import validate
from .shemas import User as UserScheme

bp = Blueprint('auth', __name__)

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth(scheme='Bearer')


@basic_auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(login=username).first()
    if not user:
        raise Unauthorized
    if user.check_password(password):
        return user


@basic_auth.error_handler
def basic_auth_error():
    raise Unauthorized


@token_auth.error_handler
def token_auth_error():
    raise Unauthorized


@token_auth.verify_token
def verify_token(token):
    current_user = User.check_token(token) if token else None
    return current_user


@bp.route("/token")
@basic_auth.login_required
def login():
    user = basic_auth.current_user()
    return jsonify(success=True, token=user.get_token())


@bp.route('/token', methods=['DELETE'])
@token_auth.login_required
def revoke_token():
    user = token_auth.current_user()
    user.revoke_token()
    return jsonify(success=True)


@bp.route('/get_me')
@token_auth.login_required
@validate(response_by_alias=True)
def get_me():
    user = token_auth.current_user()
    return UserScheme.from_orm(user)
