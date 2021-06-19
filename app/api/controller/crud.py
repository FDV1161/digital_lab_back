from app.api.base.functions import BaseCRUD
from app.models import Controller


class ControllerCRUD(BaseCRUD):
    model = Controller
