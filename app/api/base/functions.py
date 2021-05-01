from database import session, db
from app.errors.Exception import NotFoundException
from app.api.base.shemas import OrmBaseModel


def get_items(model: db.Model):
    items = session.query(model).all()
    return items


def get_item(model: db.Model, item_id: int):
    item = session.query(model).get(item_id)
    if not item:
        raise NotFoundException
    return item


def create_item(model: db.Model, data: OrmBaseModel, fk_list: dict = None):
    data = data.dict()
    if fk_list:
        data = foreignkey_verify(data, fk_list)
    item = model(**data)
    session.add(item)
    session.commit()
    return item


def delete_item(model: db.Model, item_id: int):
    item = get_item(model, item_id)
    session.delete(item)
    session.commit()
    return item


def update_item(model: db.Model, item_id: int, data: OrmBaseModel, fk_list: dict = None):
    data = data.dict()
    if fk_list:
        data = foreignkey_verify(data, fk_list)
    item = get_item(model, item_id)
    for attr, value in data.items():
        setattr(item, attr, value)
    session.add(item)
    session.commit()
    return item


def foreignkey_verify(data: dict, fk_list: dict):
    for field, model in fk_list.items():
        field_data = data.pop(field)
        item = None
        if field_data:
            item = get_item(model, field_data.get("id"))
        data[field] = item
    return data
