from threading import Thread, currentThread
from time import sleep

from database import db
from flask import copy_current_request_context, current_app
from flask_socketio import Namespace

from app.models import DeviceFunction
from .schemas import DeviceFunctionValues


class ReadingsSender(Namespace):

    def __init__(self, namespace=None):
        super().__init__(namespace=namespace)
        self.__connected_count = 0
        self.__rs_thread = None

    def on_connect(self, *args, **kwargs):

        @copy_current_request_context
        def background_sender(socketio):
            ct = currentThread()
            while getattr(ct, "is_run", True):
                cur_vals = db.session.query(DeviceFunction).all()
                device_function_values = DeviceFunctionValues.from_orm(cur_vals)
                socketio.send(device_function_values.dict()["__root__"], broadcast=True)
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
