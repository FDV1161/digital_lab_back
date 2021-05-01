from .errors import bp as errors_bp
from .api import room_bp, sensor_bp, measure_bp
from flask import Flask
from dynaconf import FlaskDynaconf
from flask_cors import CORS


from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from database import db

app = Flask(__name__)


FlaskDynaconf(app, settings_files=["settings.yaml", '.secrets.yaml'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)

db.init_app(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

app.register_blueprint(errors_bp)
app.register_blueprint(room_bp, url_prefix="/rooms")
app.register_blueprint(sensor_bp, url_prefix="/sensors")
app.register_blueprint(measure_bp, url_prefix="/measures")

