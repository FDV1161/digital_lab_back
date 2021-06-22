from database import session, db
from app.errors.Exception import NotFoundException, UniqueException
from app.api.base.shemas import OrmBaseModel
from sqlalchemy import or_


class BaseCRUD:
    model: db.Model = None
    foreign_keys = None
    filter = None

    @staticmethod
    def _get_item(model, item_id):
        item = session.query(model).get(item_id)
        if not item:
            raise NotFoundException
        return item

    def _check_unique(self, data, item_id=None):
        unique_param = [
            c == data.get(c.name)
            for c in self.model.__table__.columns
            if c.unique and c.name in data.keys()
        ]
        if not unique_param:
            return
        item = session.query(self.model).filter(or_(*unique_param),
                                                self.model.id != item_id).limit(1).scalar()
        if item:
            raise UniqueException

    def _check_exist_foreignkey(self, data):
        if not self.foreign_keys:
            return
        for foreign_key in self.foreign_keys:
            foreign_key_id = data.get(foreign_key)
            if foreign_key_id:
                foreign_key_model = self.foreign_keys[foreign_key]
                if isinstance(foreign_key_id, list):
                    for fk_id in foreign_key_id:
                        self._get_item(foreign_key_model, fk_id)
                else:
                    self._get_item(foreign_key_model, foreign_key_id)

    def data_verify(self, data: OrmBaseModel):
        data = data.dict(exclude_unset=True)
        self._check_unique(data)
        self._check_exist_foreignkey(data)
        return data

    def get_items(self, filters: OrmBaseModel = None):
        if self.filter:
            items = self.filter().filter_query(self.model.query, filters.dict(exclude_unset=True)).all()
        else:
            items = session.query(self.model).all()
        return items

    def get_item(self, item_id: int):
        return self._get_item(self.model, item_id)

    def create_item(self, data: OrmBaseModel):
        data = self.data_verify(data)
        item = self.model(**data)
        session.add(item)
        session.commit()
        return item

    def update_item(self, item_id: int, data: OrmBaseModel):
        data = self.data_verify(data)
        item = self.get_item(item_id)
        for attr, value in data.items():
            setattr(item, attr, value)
        session.add(item)
        session.commit()
        return item

    def delete_item(self, item_id: int):
        item = self.get_item(item_id)
        session.delete(item)
        session.commit()
        return item
