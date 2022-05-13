from app import app
from app import manager
from app import socketio


if __name__ == "__main__":
    app.run(host='0.0.0.0')
    # manager.run()
    # socketio.run(app, debug=True)
