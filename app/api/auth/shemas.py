from typing import Optional
from app.api.base.shemas import OrmBaseModel
from pydantic import Field


class AuthIn(OrmBaseModel):
    login: str
    password: str
    remember: Optional[bool] = Field(default=False)


class AuthOut(OrmBaseModel):
    id: int
    login: str


# class AuthList(OrmBaseModel):
#     __root__: List[AuthOut]