from database import session, db
from app.errors.Exception import NotFoundException, UniqueException
from app.api.base.shemas import OrmBaseModel
from sqlalchemy import or_
from app.models import Room, Device, Sensor

FK_LIST = {
    "room_id": Room,
    "device_id": Device,
    "sensor_one_id": Sensor,
    "sensor_two_id": Sensor,
    "sensor_free_id": Sensor,
}


def get_items(model: db.Model):
    items = session.query(model).all()
    return items


def get_item(model: db.Model, item_id: int):
    item = session.query(model).get(item_id)
    if not item:
        print(model, item_id)
        raise NotFoundException
    return item


def create_item(model: db.Model, data: OrmBaseModel, fk_list: dict = None):
    data = data.dict(exclude_unset=True)
    # if fk_list:
    #     data = foreignkey_verify(data, fk_list)
    check_exist_foreignkey(model, data)
    check_unique(model, data)
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
    data = data.dict(exclude_unset=True)
    # if fk_list:
    #     data = foreignkey_verify(data, fk_list)
    check_exist_foreignkey(model, data)
    check_unique(model, data, item_id)
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


def check_exist_foreignkey(model, data):
    for field in model.__table__.columns:
        if field.name in data and field.name in FK_LIST:
            field_data = data.get(field.name)
            if field_data:
                get_item(FK_LIST[field.name], field_data)


def check_unique(model, data, item_id=None):
    unique_param = [
        c == data.get(c.name)
        for c in model.__table__.columns
        if c.unique and c.name in data.keys()
    ]
    if not unique_param:
        return
    item = session.query(model).filter(or_(*unique_param),
                                       model.id != item_id).limit(1).scalar()
    if item:
        raise UniqueException
