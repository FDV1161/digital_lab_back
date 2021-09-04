from flask_login import login_user, login_required, logout_user, current_user
from flask import Blueprint, abort
from flask_pydantic import validate
from app.models import User
from database import db
from .shemas import AuthIn, AuthOut
from app.errors.Exception import NotFoundException

bp = Blueprint('auth', __name__)


@bp.route("/login", methods=["post"])
@validate(response_by_alias=True)
def login(body: AuthIn):
    user = db.session.query(User).filter(User.login == body.login).first()
    if user and user.check_password(body.password):
        login_user(user, remember=body.remember)
        return AuthOut.from_orm(user)
    raise NotFoundException


@bp.route('/get_me')
@validate(response_by_alias=True)
@login_required
def get_me():
    return AuthOut.from_orm(current_user)


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return "logout"
