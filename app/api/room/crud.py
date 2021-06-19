from app.api.base.functions import BaseCRUD
from app.models import Room


class RoomCRUD(BaseCRUD):
    model = Room
