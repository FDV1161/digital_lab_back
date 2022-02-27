from pydantic import validator
from typing import List, Optional
from app.api.base.shemas import OrmBaseModel
from datetime import datetime


class DeviceFunctionValue(OrmBaseModel):
    id: int
    cur_val: Optional[float]
    updated_at: Optional[datetime]

    @validator('updated_at')
    def validate_updated_at(cls, value):
        if value:
            return str(value)
        return value


class DeviceFunctionValues(OrmBaseModel):
    __root__: List[DeviceFunctionValue]
