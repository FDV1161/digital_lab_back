from .errors import bp as errors_bp
from .api import (
    room_bp,
    controller_bp,
    device_bp,
    journal_readings_bp,
    auth_bp,
    file_bp,
    function_bp,
    device_function_bp,
    home_bp,
    group_bp,
    users_bp,
)
from flask import Flask, send_from_directory, render_template
from dynaconf import FlaskDynaconf
from flask_cors import CORS

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from database import db
from flask_socketio import SocketIO
from app.soketio.sender import ReadingsSender

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="threading")

FlaskDynaconf(app, settings_files=["settings.yaml", ".secrets.yaml"])
CORS(app, support_credentials=True)

app.url_map.strict_slashes = False

db.init_app(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)

app.register_blueprint(errors_bp)
app.register_blueprint(room_bp, url_prefix="/room")
app.register_blueprint(device_bp, url_prefix="/device")
app.register_blueprint(controller_bp, url_prefix="/controller")
app.register_blueprint(journal_readings_bp, url_prefix="/journal_readings")
app.register_blueprint(device_function_bp, url_prefix="/device_functions")
app.register_blueprint(function_bp, url_prefix="/function")
app.register_blueprint(file_bp, url_prefix="/file")
app.register_blueprint(home_bp, url_prefix="/home")
app.register_blueprint(group_bp, url_prefix="/group")
app.register_blueprint(users_bp, url_prefix="/users")
app.register_blueprint(auth_bp)

socketio.on_namespace(ReadingsSender())


@app.route("/static/<filename>")
def static_files(filename: str):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename, as_attachment=True)


@app.route("/index")
def index():
    return render_template("index.html", username="asd")
