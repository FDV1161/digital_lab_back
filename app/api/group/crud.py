from app.api.base.functions import BaseCRUD
from app.models import Group


class RoomCRUD(BaseCRUD):
    model = Group
