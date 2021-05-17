from database import db
from datetime import datetime
from sqla_softdelete import SoftDeleteMixin
from sqlalchemy import Column, String, Integer, Text, DateTime, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
# ?charset=utf8


class TimestampMixin:
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(),
                        onupdate=datetime.now())
    deleted_at = Column(DateTime)


class User(SoftDeleteMixin, TimestampMixin, db.Model):
    __tablename__ = "user"
    __table_args__ = {"comment": "Пользователи"}

    id = Column(Integer, primary_key=True)
    login = Column(String(256), nullable=False)
    password = Column(String(256), nullable=False)
    email = Column(String(256))
    name = Column(String(256))
    patronymic = Column(String(256))
    group_id = Column(ForeignKey("group.id"))


class Group(SoftDeleteMixin, TimestampMixin, db.Model):
    __tablename__ = "group"
    __table_args__ = {"comment": "Группы пользователей"}

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False, unique=True)


class GroupPermission(db.Model):
    __tablename__ = 'group__permission'

    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey('group.id'))
    permission_id = Column(Integer, ForeignKey('permission.id'))


class Permission(SoftDeleteMixin, TimestampMixin, db.Model):
    __tablename__ = "permission"
    __table_args__ = {"comment": "Разрешения"}

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False, unique=True)
    description = Column(Text)


class Device(SoftDeleteMixin, TimestampMixin, db.Model):
    __tablename__ = "device"
    __table_args__ = {"comment": "Датчики"}

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    description = Column(Text)
    icon = Column(String(256))

    controller_id = Column(ForeignKey("controller.id"))
    room_id = Column(ForeignKey("room.id"))

    controller = relationship("controller")
    room = relationship("Room", backref="device_list", foreign_keys=[room_id])


class Room(SoftDeleteMixin, TimestampMixin, db.Model):
    __tablename__ = "room"
    __table_args__ = {"comment": "Аудитория"}

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False, unique=True)
    description = Column(Text)


class Controller(SoftDeleteMixin, TimestampMixin, db.Model):
    __tablename__ = "controller"
    __table_args__ = {"comment": "Оборудование"}

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    protocol = Column(Integer)
    address = Column(Integer)
    description = Column(Text)


class Journal(SoftDeleteMixin, TimestampMixin, db.Model):
    __tablename__ = "journal"
    __table_args__ = {"comment": "Показания датчиков"}

    id = Column(Integer, primary_key=True)
    value = Column(Float, nullable=False)
    sensor_id = Column(ForeignKey("sensor.id"), nullable=False)


class Function(SoftDeleteMixin, TimestampMixin, db.Model):
    __tablename__ = "func"
    __table_args__ = {"comment": "Функции оборудования"}

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    min_value = Column(Integer)
    max_value = Column(Integer)
    description = Column(Text)
    measure_name = Column(String(256))
    measure_symbol = Column(String(32))


class DeviceFunction(SoftDeleteMixin, TimestampMixin, db.Model):
    __tablename__ = "device_func"
    __table_args__ = {"comment": "Функции оборудования"}

    id = Column(Integer, primary_key=True)
    id_func = Column(ForeignKey("func.id"))
    id_device = Column(ForeignKey("device.id"))
    address = Column(Integer)
    on_home = Column(Boolean, default=False)

