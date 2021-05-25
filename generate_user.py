from app import app
from database import db
from app.models import User

with app.app_context():
    user = User(login="admin")
    user.set_password("admin")
    db.session.add(user)
    db.session.commit()
