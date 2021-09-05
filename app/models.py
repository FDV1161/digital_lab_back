from database import db
from datetime import datetime
from sqla_softdelete import SoftDeleteMixin
from sqlalchemy import Column, String, Integer, Text, DateTime, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declared_attr
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from enum import IntEnum


class GroupE(IntEnum):
    admin = 1
    editor = 2
    viewer = 3


class MyTimestampMixin:
    created_at = Column(DateTime, default=lambda: datetime.now())
    updated_at = Column(DateTime, default=lambda: datetime.now(),
                        onupdate=lambda: datetime.now())
    deleted_at = Column(DateTime)


class MyUserMixin:
    @declared_attr
    def created_by(cls):
        return Column(Integer, ForeignKey("user.id"))

    @declared_attr
    def updated_by(cls):
        return Column(Integer, ForeignKey("user.id"))

    @declared_attr
    def deleted_by(cls):
        return Column(Integer, ForeignKey("user.id"))


class Group(SoftDeleteMixin, MyTimestampMixin, db.Model):
    __tablename__ = "group"
    __table_args__ = {"comment": "Группы пользователей"}

    id = Column(Integer, primary_key=True)
    name = Column(String(256), unique=True, nullable=False)


class User(SoftDeleteMixin, MyTimestampMixin, MyUserMixin, db.Model, UserMixin):
    __tablename__ = "user"
    __table_args__ = {"comment": "Пользователи"}

    id = Column(Integer, primary_key=True)
    login = Column(String(256), nullable=False, unique=True)
    password = Column(String(256), nullable=False)
    email = Column(String(256))
    name = Column(String(256))
    surname = Column(String(256))
    patronymic = Column(String(256))
    group_id = Column(
        ForeignKey("group.id"),
        nullable=False,
        server_default=str(GroupE.viewer.value),
        default=str(GroupE.viewer.value)
    )    

    group = relationship("Group")

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Room(SoftDeleteMixin, MyTimestampMixin, MyUserMixin, db.Model):
    __tablename__ = "room"
    __table_args__ = {"comment": "Аудитория"}

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False, unique=True)
    description = Column(Text)
    devices = relationship("Device")


class Device(SoftDeleteMixin, MyTimestampMixin, MyUserMixin, db.Model):
    __tablename__ = "device"
    __table_args__ = {"comment": "Датчики / исполнительные устройства"}

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    description = Column(Text)
    icon = Column(String(256))

    controller_id = Column(ForeignKey("controller.id"))
    room_id = Column(ForeignKey("room.id"))
    device_functions = relationship("DeviceFunction")


class Controller(SoftDeleteMixin, MyTimestampMixin, MyUserMixin, db.Model):
    __tablename__ = "controller"
    __table_args__ = {"comment": "Оборудование"}

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    protocol = Column(Integer)
    port = Column(String(256))
    address = Column(Integer)
    description = Column(Text)
    baudrate = Column(Integer)


class JournalReadings(SoftDeleteMixin, MyTimestampMixin, db.Model):
    __tablename__ = "journal_readings"
    __table_args__ = {"comment": "Журнал показаний датчиков"}

    id = Column(Integer, primary_key=True)
    value = Column(Float, nullable=False)
    device_func_id = Column(ForeignKey("device_func.id"), nullable=False)


class CurrentReadings(SoftDeleteMixin, MyTimestampMixin, db.Model):
    __tablename__ = "current_readings"
    __table_args__ = {"comment": "Текущие показания датчиков"}

    id = Column(Integer, primary_key=True)
    value = Column(Float, nullable=False)
    device_func_id = Column(ForeignKey("device_func.id"), nullable=False)


class Function(SoftDeleteMixin, MyTimestampMixin, MyUserMixin, db.Model):
    __tablename__ = "func"
    __table_args__ = {"comment": "Функции оборудования"}

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    min_value = Column(Integer)
    max_value = Column(Integer)
    description = Column(Text)
    measure_name = Column(String(256))
    measure_symbol = Column(String(32))


class DeviceFunction(SoftDeleteMixin, MyTimestampMixin, MyUserMixin, db.Model):
    __tablename__ = "device_func"
    __table_args__ = {"comment": "Функции оборудования"}

    id = Column(Integer, primary_key=True)
    id_func = Column(ForeignKey("func.id"))
    id_device = Column(ForeignKey("device.id"))
    address = Column(Integer)
    on_home = Column(Boolean, default=False)
    multiply = Column(Float)
    write_enable = Column(Boolean)
    cur_val = Column(Float)
    func = relationship("Function")
