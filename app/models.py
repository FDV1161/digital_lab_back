from database import db
from datetime import datetime
from sqla_softdelete import SoftDeleteMixin
from sqlalchemy import Column, String, Integer, Text, DateTime, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship


class TimestampMixin:
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(),
                        onupdate=datetime.now())
    deleted_at = Column(DateTime)


class User(SoftDeleteMixin, TimestampMixin, db.Model):
    __tablename__ = "user"
    __table_args__ = {"comment": "Пользователи"}

    id = Column(Integer, primary_key=True)
    login = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String)
    name = Column(String)
    patronymic = Column(String)
    group_id = Column(ForeignKey("group.id"))


class Group(SoftDeleteMixin, TimestampMixin, db.Model):
    __tablename__ = "group"
    __table_args__ = {"comment": "Группы пользователей"}

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)


class Permission(SoftDeleteMixin, TimestampMixin, db.Model):
    __tablename__ = "permission"
    __table_args__ = {"comment": "Разрешения"}

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(Text)


class Room(SoftDeleteMixin, TimestampMixin, db.Model):
    __tablename__ = "room"
    __table_args__ = {"comment": "Аудитория"}

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(Text)

    sensor_list = relationship("Sensor")



class Device(SoftDeleteMixin, TimestampMixin, db.Model):
    __tablename__ = "device"
    __table_args__ = {"comment": "Оборудование"}

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    address = Column(Integer)
    description = Column(Text)


class Sensor(SoftDeleteMixin, TimestampMixin, db.Model):
    __tablename__ = "sensor"
    __table_args__ = {"comment": "Датчики"}

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    address = Column(Integer)
    description = Column(Text)
    on_home = Column(Boolean)
    device_id = Column(ForeignKey("device.id"))
    room_id = Column(ForeignKey("room.id"))
    measure_id = Column(ForeignKey("measure.id"))

    room =  relationship("Room", back_populates="sensor_list")
    measure = relationship("Measure")


class Journal(SoftDeleteMixin, TimestampMixin, db.Model):
    __tablename__ = "journal"
    __table_args__ = {"comment": "Показания датчиков"}

    id = Column(Integer, primary_key=True)
    value = Column(Float)
    sensor_id = Column(ForeignKey("sensor.id"))


class Function(SoftDeleteMixin, TimestampMixin, db.Model):
    __tablename__ = "function"
    __table_args__ = {"comment": "Функции оборудования"}

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    min_value = Column(Integer)
    max_value = Column(Integer)
    current_value = Column(Integer)
    sensor_id = Column(ForeignKey("sensor.id"))


class Measure(SoftDeleteMixin, TimestampMixin, db.Model):
    __tablename__ = "measure"
    __table_args__ = {"comment": "Физические величины"}

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    symbol = Column(String, nullable=False, unique=True)


class GroupPermission(db.Model):
    __tablename__ = 'group__permission'

    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey('group.id'))
    permission_id = Column(Integer, ForeignKey('permission.id'))
