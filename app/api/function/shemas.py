from typing import List, Optional
from app.api.base.shemas import OrmBaseModel


class FunctionIn(OrmBaseModel):
    name: str
    min_value: int
    max_value: int
    measure_name: Optional[str]
    measure_symbol: Optional[str]
    description: Optional[str]


class FunctionOut(FunctionIn):
    id: int


class FunctionList(OrmBaseModel):
    __root__: List[FunctionOut]
