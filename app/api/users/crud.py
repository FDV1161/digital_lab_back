from app.api.base.functions import BaseCRUD
from app.models import User
from database import session

class UserCRUD(BaseCRUD):
    model = User

    def create_item(self, data):
        data = self.data_verify(data)
        item = self.model(**data)
        item.set_password(data.get("password"))
        session.add(item)
        session.commit()
        return item

    def update_item(self, item_id: int, data):
        data = self.data_verify(data, item_id=item_id)
        item = self.get_item(item_id)
        for attr, value in data.items():
            setattr(item, attr, value)
        if data.get("password"):
            item.set_password(data.get("password"))
        session.add(item)
        session.commit()
        return item
