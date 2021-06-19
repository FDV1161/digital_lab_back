from app.api.base.functions import BaseCRUD
from app.models import Function


class FunctionCRUD(BaseCRUD):
    model = Function
