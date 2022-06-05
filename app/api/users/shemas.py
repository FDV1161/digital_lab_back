from sqlalchemy.sql.base import NO_ARG
from app.models import Group
from typing import List, Optional

from app.api.base.shemas import OrmBaseModel
from app.api.device.shemas import DeviceList
from pydantic import root_validator, validator
from re import L, match


class User(OrmBaseModel):
    name: Optional[str]
    surname: Optional[str]
    patronymic: Optional[str]
    login: str
    group_id: int

    @validator('login')
    def validate_login(cls, value):
        login = str(value).strip()
        if match(r"^[\w]{3,16}$", login) is None:
            raise ValueError('Логин не соответствует регулярному выражению')
        return value


class UserCreate(User):
    password: str
    confirm_password: str

    @root_validator
    def check_passwords_match(cls, values):
        pw1, pw2 = values.get('password'), values.get('confirm_password')        
        if len(pw1) < 6:
            raise ValueError('password is too short')
        if pw1 is not None and pw2 is not None and pw1 != pw2:
            raise ValueError('passwords do not match')
        values.pop("confirm_password")
        return values


class UserUpdate(User):
    password: Optional[str]
    confirm_password: Optional[str]

    @root_validator
    def check_passwords_match(cls, values):
        pw1, pw2 = values.get('password'), values.get('confirm_password')
        if pw1 is not None and pw1 != pw2:
            raise ValueError('passwords do not match')
        values.pop("confirm_password")
        return values


class UserOut(User):
    id: int


class UserList(OrmBaseModel):
    __root__: List[UserOut]
