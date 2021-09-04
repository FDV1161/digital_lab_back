from typing import List
from app.api.base.shemas import OrmBaseModel


class GroupOut(OrmBaseModel):
    id: int
    name: str


class GroupList(OrmBaseModel):
    __root__: List[GroupOut]
