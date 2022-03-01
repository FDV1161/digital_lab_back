from typing import Dict

from sqlalchemy import or_
from sqlalchemy.sql.elements import Null

from app.api.base.shemas import OrmBaseModel
from app.errors.Exception import NotFoundException, UniqueException
from database import session, db


class BaseCRUD:
    model: db.Model = None
    use_pagination: bool = False
    foreign_keys: Dict[str, db.Model] = None
    filter = None

    @staticmethod
    def _get_item(model, item_id):
        item = session.query(model).get(item_id)
        if not item:
            raise NotFoundException(model=model)
        return item

    def _check_unique(self, data, item_id=None):
        unique_param = [
            c == data.get(c.name)
            for c in self.model.__table__.columns
            if c.unique and c.name in data.keys()
        ]
        if not unique_param:
            return
        item = session.query(self.model).filter(or_(*unique_param), self.model.id != item_id).first()
        if item:
            raise UniqueException(model=self.model)

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

    def _filter_items(self, stmt, filters):
        if self.filter:
            return self.filter().filter_query(stmt, filters.dict(exclude_unset=True))
        return stmt

    def _paginate_items(self, stmt, page=1, count=10):
        if self.use_pagination:
            return stmt.paginate(page, count, False).items, stmt.count()
        return stmt.all(), stmt.count()

    def data_verify(self, data: OrmBaseModel, item_id=Null):
        data = data.dict(exclude_unset=True)
        self._check_unique(data, item_id=item_id)
        self._check_exist_foreignkey(data)
        return data

    def get_items(self, filters: OrmBaseModel = None, page=1, count=10):
        stmt = session.query(self.model)
        stmt = self._filter_items(stmt, filters)
        return self._paginate_items(stmt, page, count)

    def get_item(self, item_id: int):
        return self._get_item(self.model, item_id)

    def create_item(self, data: OrmBaseModel):
        data = self.data_verify(data)
        item = self.model(**data)
        session.add(item)
        session.commit()
        return item

    def update_item(self, item_id: int, data: OrmBaseModel):
        data = self.data_verify(data, item_id=item_id)
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
