from typing import Optional
from app.api.base.shemas import OrmBaseModel
from pydantic import Field


class Group(OrmBaseModel):
    id: int
    name: str


class User(OrmBaseModel):
    name: Optional[str]
    surname: Optional[str]
    patronymic: Optional[str]
    login: str
    group: Group


class GroupOut(OrmBaseModel):
    id: int
    name: str


class AuthIn(OrmBaseModel):
    login: str
    password: str
    remember: Optional[bool] = Field(default=False)


class AuthOut(OrmBaseModel):
    id: int
    login: str
    group: GroupOut


# class AuthList(OrmBaseModel):
#     __root__: List[AuthOut]
