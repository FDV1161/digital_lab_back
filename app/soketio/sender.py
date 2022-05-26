from datetime import datetime
from threading import Thread, currentThread
from time import sleep

from database import db
from flask import copy_current_request_context, current_app
from flask_socketio import Namespace

from app.models import DeviceFunction
from .schemas import DeviceFunctionValue


def get_max_updated_at(device_functions, current_date):
    if not device_functions:
        return current_date
    max_date = max(device_functions, key=lambda df: df.updated_at)
    return max_date.updated_at or current_date


class ReadingsSender(Namespace):

    def __init__(self, namespace=None):
        super().__init__(namespace=namespace)
        self.__connected_count = 0
        self.__rs_thread = None

    def on_connect(self, *args, **kwargs):

        @copy_current_request_context
        def background_sender(socketio):
            ct = currentThread()
            last_select = datetime.now()
            Session = db.create_scoped_session()
            # Session = db.create_session({})
            while getattr(ct, "is_run", True):
                with Session() as session:
                    device_functions = session.query(DeviceFunction).filter(
                        DeviceFunction.updated_at > last_select).all()
                    last_select = get_max_updated_at(device_functions, last_select)
                    for device_function in device_functions:
                        value = DeviceFunctionValue.from_orm(device_function)
                        socketio.send(value.dict(), broadcast=True)
                    sleep(current_app.config['READINGS_SENDER_INTERVAL'])

        self.__connected_count += 1
        if self.__rs_thread is None:
            self.__rs_thread = Thread(
                target=background_sender, daemon=True, args=(self.socketio,))
            self.__rs_thread.is_run = True
            self.__rs_thread.start()

    def on_disconnect(self):
        self.__connected_count -= 1
        if not self.__connected_count and self.__rs_thread:
            self.__rs_thread.is_run = False
            self.__rs_thread = None
